import sys
import praw
from praw import Reddit


def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        print('Connected to reddit!')
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)


def extract_posts(instance: Reddit, subreddit: str, timefilter: str, limit):
    subreddit = instance.subreddit(subreddit)
    posts = subreddit.top(timefilter=timefilter, limit=limit)

    post_lists = []
    print(posts)
    print(len(posts))

    # for post in posts:
    #     print
