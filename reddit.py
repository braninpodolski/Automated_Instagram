import urllib.request
import praw
from praw import reddit
from praw.models.listing.mixins import submission


def download_subreddit(sub):
    reddit = praw.Reddit(client_id='oFOYuOd31vUb4UstBWDhnQ',
                    client_secret='0W_86zufGFCJlSE4lK3CwF_0UEQEQw',
                    username='MarshallBranin',
                    password='#Marshall2',
                    user_agent='macos:com.example.text_app:v1.0.0 (by /u/MarshallBranin)')  
    
    reddit.read_only=True

    # Iterate through top submissions
    for submission in praw.reddit.Subreddit(reddit, display_name=f"{sub}").hot(limit=None):

        # Get the link of the submission
        url = str(submission.url)

        # Check if the link is an image
        if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):

            # Retrieve the image and save it in current folder
            urllib.request.urlretrieve(url, "instagram/INSTAGRAM.jpg")
            break




