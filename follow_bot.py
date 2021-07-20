from instabot import Bot
import glob
import os
from configparser import RawConfigParser

def bot():
     # Config
    config = RawConfigParser()
    config.read('config.ini')
    acc = config['preferences']['account']

    # Clear cookies for login
    cookie_del = glob.glob("/*/*/*/AutomatedInstagram/config/*cookie.json")
    if cookie_del:
        os.remove(cookie_del[0])

    bot = Bot(
        max_follows_per_day=100
    )
    bot.login(username=config['login']['username'], password=config['login']['password'])

    followers = bot.get_user_followers(acc)

    bot.follow_users(followers)