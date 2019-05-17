import praw
import time
import requests
import re

reddit = praw.Reddit(client_id='EXMmU0DXWt6Kyw',
                     client_secret='V6MB8LZHkQdBsp801ZphbubrImM',
                     password='1q2w3e',
                     user_agent='testscript by /u/fakebot3',
                     username='zipp_1')

count = 0

day = 86400 #seconds
days_10 = day * 10

###############################################
links = ['https://www.reddit.com/r/AskReddit/',
         'https://www.reddit.com/r/funny/'
        ]
###############################################

categories = list()
categories.append(links)

for item in categories:
    for link in item:
        subreddit = link.split("/r/")[1]
        subreddit = subreddit[:-1]
        print(subreddit)

        after = 1420070400
        before = after + days_10

        while before < 1543842157:
            count += 1
            print("Count ", count)
            before += days_10
            after += days_10
            r = requests.get('https://api.pushshift.io/reddit/submission/search/?after={}&before={}&sort_type=score&sort=desc&subreddit={}&limit=1500'.format(after, before, subreddit))

            print(len(r.json()['data']))
            data = r.json()['data']

            for d in data:
                if 'selftext' in d:
                    print(d)
                    f = open(subreddit + '.txt', 'a')
                    text = re.sub(r"http\S+", "", d['selftext'])
                    f.write('\n" ' + text + ' "\n')

