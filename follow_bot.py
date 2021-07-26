from instabot import Bot
import glob
import os
from configparser import RawConfigParser

def bot():
     # Config
    config = RawConfigParser()
    config.read('config.ini')
    acc = config['preferences']['follow_account']

    # Clear cookies for login
    cookie_del = glob.glob("/*/*/*/Automated_Instagram-master/config/*cookie.json")
    if cookie_del:
        os.remove(cookie_del[0])

    bot = Bot(
        max_follows_per_day=100,
        follow_delay=30
    )
    bot.login(username=config['login']['username'], password=config['login']['password'])

    followers = bot.get_user_followers(acc)

    bot.follow_users(followers)