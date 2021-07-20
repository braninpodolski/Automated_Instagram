from instabot import Bot
import instabot
import instaloader
import hashtag_scraper
import os 
import glob
from instaloader import Instaloader, Profile
import json
import shutil
from PIL import Image
from configparser import RawConfigParser

def upload():
    # Config
    config = RawConfigParser()
    config.read('config.ini')
    hashtag = config['preferences']['hashtag']
    acc = config['login']['username']

    # Clear cookies for login
    cookie_del = glob.glob("/*/*/*/Automated_Instagram-master/config/*cookie.json")
    if cookie_del:
        os.remove(cookie_del[0])

    # Create bot and login
    bot = Bot()
    bot.login(username=config['login']['username'], password=config['login']['password'])

    # Download Image
    hashtag_scraper.main(hashtag)

    # Caption
    caption = f'''\n
    -------------------
    \n
    Follow @{acc} for Daily Posts🏠
    \n
    -------------------
    Follow @{acc} 🏠
    Follow @{acc} 🏠
    Follow @{acc} 🏠
    -------------------
    \n
    \n
    {config['preferences']['caption_tags']}'''
    
    # Fetch filename and profile username
    path = ('#' + hashtag + '/')
    for file in glob.glob('/*/*/*/Automated_Instagram-master/*/*.json'):
        if file != f'/*/*/*/Automated_Instagram-master/#{hashtag}/#{hashtag}.json' and '_uuid_and_cookie' not in file:
            with open(file, 'r') as file:
                data = json.load(file)
                profileid = str(data['node']['owner']['id'])
                instaload = Instaloader()
                profile = Profile.from_id(instaload.context,profile_id= profileid)

            
    # Upload and Delete directory
    for file in glob.glob('/*/*/*/Automated_Instagram-master/*/*.jpg'):
        im = Image.open(file)
        newsize = (1080, 1080)
        im1 = im.resize(newsize)
        im1.save(f'#{hashtag}.jpg')
        bot.upload_photo(f'#{hashtag}.jpg', caption='Source: @' + profile.username + caption)
        shutil.rmtree(f'/*/*/*/Automated_Instagram-master/#{hashtag}')
        os.remove(f'#{hashtag}.jpg.REMOVE_ME')
        break