import argparse
import json
import sys 

import requests  # pip install requests

    
def post_to_slack(url, text, channel, user, emoji): 
    headers = {'content-type':'application/json'}
    payload = json.dumps({
            'channel' : channel,
            'username' : user,
            'text' : text,
            'icon_emoji' : emoji, 
    })
    request = requests.post(url, headers=headers, data=payload)
    print "Response: %s - %s" % (request.status_code, request.reason)
    

def parse_args():
    parser = argparse.ArgumentParser(description='Talk to Slack')
    parser.add_argument('-u','--url', help='Slack Incoming Webhooks integration webhook URL', required=False, 
        default='https://pzelnip.slack.com/services/hooks/incoming-webhook?token=Ta4BRUMStaB5ahT4Y76eT1Hi')
    parser.add_argument('-c','--channel', help='Channel to post to', required=True)
    parser.add_argument('-n','--user', help='Name of the user to post as', required=False, default='CmdLine')
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
