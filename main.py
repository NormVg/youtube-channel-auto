import praw
import numpy as np
import random
import video
import upl
import time
from better_profanity import profanity
profanity.load_censor_words()


def reddit():
    reddit = praw.Reddit(client_id='T0cozH9DKJuwOyl-vPPm9A',
                     client_secret='C8OIu_6OS2Uu-r1WlU7jdUEVjXx4cw', user_agent='python-script')
    subreddit = reddit.subreddit('lifeprotip+Thetruthishere+Trueofmychest')
    posts = subreddit.top(time_filter="all")

    data = []

    for post in posts:
        data.append({
        'title':  profanity.censor(post.title) ,
        'content': profanity.censor(post.selftext)
        })

    
    random.shuffle(data)

    
    return data[0]



while True:
    try:
        reply = reddit()
        video.create_video(reply['title'],reply['content'])
        upl.upload()
        time.sleep(43200)
    except: 
        pass


