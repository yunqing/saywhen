# Saywhen

SayWhen sends sound and desktop notification to you when job finishes.

Tested on Ubuntu 16.04.


Usage: saywhen command [args...]

Example: saywhen echo helloworld

Example: saywhen "echo -n hello && echo world"


The returncode of saywhen is the same as the command.

## Installation
`sudo ln -s $(readlink -f saywhen) /usr/local/bin`

## Unstallation
`sudo rm -f /usr/local/bin/saywhen`

## About audio
Audios are from freesound.org.
