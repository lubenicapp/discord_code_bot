### Discord Code BOT

usage: attach the `CodeBot.on_message()` method to your bot's `on_message`

```python

from code_bot import CodeBot, PYTHON

python_bot = CodeBot(*PYTHON)

async def on_message(self, message):
    if message.author == self.user:
        return
    
    python_bot.on_message(message)
```

