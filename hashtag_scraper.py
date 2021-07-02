from instaloader import Instaloader, Profile
import datetime
from instaloader.structures import Hashtag, JsonExportable

def main(hashtag):
    loader = Instaloader()
    loader.login('', '')
    loader.post_metadata_txt_pattern = ""
    loader.download_geotags = False
    loader.save_metadata = False
    loader.save_metadata_json = False
    loader.download_comments = False
    loader.download_hashtag(hashtag, max_count=1, profile_pic=False)
# hashtag = input('Hashtag: ')
# main(hashtag)