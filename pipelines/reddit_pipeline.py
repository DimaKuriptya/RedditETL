from utils.constants import CLIENT_ID, SECRET
from etls.reddit_etl import connect_reddit, extract_posts


def reddit_pipeline(file_name: str, subreddit: str, timefilter: str = 'day', limit=None):
    # connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    # extraction
    posts = extract_posts(instance, subreddit, timefilter, limit)
