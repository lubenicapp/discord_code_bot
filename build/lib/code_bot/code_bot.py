import re
import docker
from typing import List

PYTHON = ['python', 'python:3.11', ['python', '-c']]
RUBY = ['ruby', 'ruby:3.2', ['ruby', '-e']]
PHP = ['php', 'php:8.1-rc-zts-alpine3.16', ['php', '-r']]


async def message_container_evaluation(container, message, timeout=8, size=1500):
    try:
        container.wait(timeout=timeout)
        out = container.logs(stdout=True, stderr=True)
        await message.channel.send(f"```\n{out.decode()[0:size]}\n```")
    except Exception as exc:
        await message.channel.send(f'{type(exc)}')
    finally:
        container.stop()


def extract_code_from_markdown(markdown, language):
    code_block = re.search(fr"```{language}\n(.*?)```", markdown, re.DOTALL)
    if code_block:
        code = code_block.group(1)
        return code
    else:
        return None


class CodeBot:
    """
        Bot that evaluate interpreted code
    """
    MAX_SIZE = 1500  # max message length

    def __init__(self, language: str, image: str, command: List[str], timeout=8):
        self.language = language
        self.image = image
        self.command = command
        self.timeout = timeout

    async def on_message(self, message):
        code = extract_code_from_markdown(message.content, self.language)
        if code is None:
            return

        docker_client = docker.from_env()
        container = docker_client.containers.run(self.image, [*self.command, code], detach=True)
        await message_container_evaluation(container, message, self.timeout, self.MAX_SIZE)


__all__ = ['PYTHON', 'PHP', 'RUBY', 'CodeBot']
