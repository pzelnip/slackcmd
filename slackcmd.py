import argparse
import json
import os
import sys 

import requests # pip install requests if you don't have it


DEFAULT_USER_NAME = 'CmdLine'
WEBHOOK_ENV_VAR_NAME = 'SLACK_WEBHOOK_URL'


def post_to_slack(url, text, channel, user, emoji): 
    headers = {'content-type':'application/json'}
    payload = json.dumps({
            'channel' : channel,
            'username' : user,
            'text' : text,
            'icon_emoji' : emoji, 
    })

    # if you don't want the dependency on the requests library, you can use the
    # standard library here:
    # import urllib2
    #request = urllib2.Request(url, payload, headers) 
    #f = urllib2.urlopen(request)
    #response = f.read()
    #f.close() 
    # print response

    # but requests is much nicer, particulary if there's an error
    request = requests.post(url, headers=headers, data=payload)
    print "Response: %s - %s" % (request.status_code, request.reason)


def parse_args():
    # try getting Webhook url from env variable
    webhook_url = os.environ.get(WEBHOOK_ENV_VAR_NAME, None)

    parser = argparse.ArgumentParser(description='Talk to Slack')
    parser.add_argument('-u','--url', 
        help='Slack Incoming Webhooks integration webhook URL.  If the environment variable %s is set, will read this value from there' % WEBHOOK_ENV_VAR_NAME, required=webhook_url is None, 
        default=webhook_url) 
    parser.add_argument('-c','--channel', help='Channel to post to', required=True)
    parser.add_argument('-n','--user', help='Name of the user to post as, defaults to "%s"' % DEFAULT_USER_NAME, 
        required=False, default=DEFAULT_USER_NAME)
    parser.add_argument('-e','--emoji', help='Emoji to use for the message', 
        required=False, default=':rocket:')

    args = vars(parser.parse_args())

    # ensure emoji has starting/ending colon
    if not args['emoji'].startswith(':'):
        args['emoji'] = ":" + args['emoji'] 
    if not args['emoji'].endswith(':'):
        args['emoji'] = args['emoji'] + ":" 

    # ensure channel has pound sign
    if args['channel'][0] not in ['#', '@']:
        args['channel'] = '#' + args['channel']

    return args


def main():
    args = parse_args()
    text = sys.stdin.read()
    post_to_slack(args['url'], text, args['channel'], args['user'], args['emoji'])


if __name__ == "__main__":
    main()
