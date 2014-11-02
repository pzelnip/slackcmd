slackcmd
========

A Python script for piping output from the command line to a Slack channel

```
Usage:

$ python slackcmd.py  -h
usage: slackcmd.py [-h] [-u URL] -c CHANNEL [-n USER] [-e EMOJI]

Talk to Slack

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Slack Incoming Webhooks integration webhook URL
  -c CHANNEL, --channel CHANNEL
                        Channel to post to
  -n USER, --user USER  Name of the user to post as
  -e EMOJI, --emoji EMOJI
                        Emoji to use for the message
```

To find your webhooks URL, in Slack add the "Incoming Webhooks" integration, and in 
the instructions will be given a "Webhook URL".  This is the URL to use.
