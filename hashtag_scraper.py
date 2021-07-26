from instaloader import Instaloader, Profile
import datetime
import instaloader
import instaloader.structures
from datetime import date
from random import randrange

def main(hashtag):
    loader = Instaloader()
    # loader.login('adorable.catclub', '#Marshall2')
    # loader.post_metadata_txt_pattern = ""
    # loader.download_geotags = False
    # loader.save_metadata = True
    # loader.save_metadata_json = True
    # loader.download_comments = False
    loader.compress_json = False
    hashtag1 = instaloader.Hashtag.from_name(loader.context, hashtag)
    for post in hashtag1.get_top_posts():
        rando = randrange(0,8)
        curdate = date.today()
        if rando == 1:
            loader.download_post(post, target=f'#{hashtag}')
            print(post.date)
            break
        
# hashtag = input('Hashtag: ')
#main('portrait')