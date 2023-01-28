import praw
import numpy as np
import random
import video
import upl
import time
reddit = praw.Reddit(client_id='T0cozH9DKJuwOyl-vPPm9A',
                     client_secret='C8OIu_6OS2Uu-r1WlU7jdUEVjXx4cw', user_agent='python-script')

def reddit():
    
    subreddit = reddit.subreddit('Trueofmychest')
    posts = subreddit.hot(limit=10)

    data = []


    for post in posts:
        data.append({
        'title': post.title,
        'content': post.selftext,
        'url': post.url,
        'score': post.score,
        'author': post.author.name
        })
    main = []
    
    for i in data:
        if i['content'] != "":
            main.append(i)
    on = random.shuffle(main)
    
    return on[0]
        
while True:
    try:
        reply = reddit()
        video.create_video(reply['title'],reply['content'])
        upl.upload()
        time.sleep(10)
    except: 
        pass


