slackcmd
========

A Python script for piping output from the command line to a Slack channel

An example:

```
ls | python slackcmd.py -c '#myChannel' 
```

Would pipe the contents of the current directory to the channel ```#myChannel```.

```
usage: slackcmd.py [-h] [-u URL] -c CHANNEL [-n USER] [-e EMOJI]

Talk to Slack

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Slack Incoming Webhooks integration webhook URL. If
                        the environment variable SLACK_WEBHOOK_URL is set,
                        will read this value from there
  -c CHANNEL, --channel CHANNEL
                        Channel to post to
  -n USER, --user USER  Name of the user to post as, defaults to "CmdLine"
  -e EMOJI, --emoji EMOJI
                        Emoji to use for the message
```

To find your webhooks URL, in Slack add the "Incoming Webhooks" integration, and in 
the instructions will be given a "Webhook URL".  This is the URL to use.

You can either specify this URL on the command-line via the -u switch, but it's much 
more convenient to set the ```SLACK_WEBHOOK_URL``` environment variable.  On a *nix
environment adding something like:

```
SLACK_WEBHOOK_URL="https://pzelnip.slack.com/services/hooks/incoming-webhook?token=Ta4BRUMStaB5ahT4Y76eT1Hi"
export SLACK_WEBHOOK_URL
```

To your ```.bashrc``` would do the trick.
