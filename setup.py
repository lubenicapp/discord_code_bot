from setuptools import setup

VERSION = '0.1.2'
DESCRIPTION = 'Package to add code evaluation to discord bot'

setup(
    name='discord_code_bot',
    version=VERSION,
    description=DESCRIPTION,
    url='https://https://github.com/lubenicapp/discord_code_bot',
    author='Lubenica#3872',
    author_email='lubenicapp@tutanota.com',
    license='BSD 2-clause',
    install_requires=['docker>=2'],
    keywords=['python', 'discord', 'bot'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
    ],
)
