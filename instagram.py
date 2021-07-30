import configparser
from functions import upload
from follow_bot import bot
from configparser import RawConfigParser
import sys
from art import *
import os
import glob
from time import sleep
import datetime
import shutil

# Import config preferences
file = 'config.ini'
config = RawConfigParser()
config.read(file)

# Clear cookies for login
cookie_del = glob.glob("/*/*/*/Automated_Instagram-master/config/*cookie.json")
if cookie_del:
    os.remove(cookie_del[0])

# Config Setup Function
def config_setup():
    os.system('clear')

    input('Press ENTER to Begin Initial Setup: ')
    os.system('clear')

    user = input('Instagram Username: ')
    config.set('login', 'username', user)
    os.system('clear')

    passw = input('Instagram Password: ')
    config.set('login', 'password', passw)
    os.system('clear')

    source = ''

    while source != 'instagram' and source != 'reddit':
        source = input('What Platform to Source from (Instagram or Reddit): ').lower()
        config.set('preferences', 'source', source)
        os.system('clear')

    if source == 'instagram':
        hashtag = input('Hashtag to Scrape Posts From (DO NOT INCLUDE POUND SYMBOL): ')
        config.set('preferences', 'hashtag', hashtag.replace('#', '')) 
        os.system('clear')

    elif source == 'reddit':
        subreddit = input('Subreddit to pull posts from: ')
        config.set('preferences', 'subreddit', subreddit)
        os.system('clear')

    caption = input('Paste List of Hashtags for Caption Template: ')
    config.set('preferences', 'caption_tags', caption)
    os.system('clear')

    acc = input('Account to Pull Follow List From (Choose from similar niche): ')
    config.set('preferences', 'follow_account', acc.replace('@', ''))
    os.system('clear')

    # Write config preferences
    with open(file, 'w') as configfile:
        config.write(configfile)


# Initial Config Setup
if config['preferences']['follow_account'] == '':
    config_setup()


# Menu Design
def console():
    tprint('AutoInsta', font='larry3d') 

    print('''
    1. Config  -  Change your configuration settings
    2. Upload  -  Automatically upload from hashtag scraper
    3. Follow  -  Automatically follow accounts from different account
    4. Exit    -  Exit the terminal
    5. Clear   -  Clear the terminal
    6. Fix     -  Fix DS_User Error
    ''')

if len(sys.argv) < 2:
    console()
    # Menu Input Interface
    while True:

        # Clear cookies for login
        cookie_del = glob.glob("/*/*/*/Automated_Instagram-master/config/*cookie.json")
        if cookie_del:
            os.remove(cookie_del[0])

        
        command = input('Enter Command: ')
        
        if command.lower() in ['config', '1']:
            config_setup()
            console()
        elif command.lower() in ['upload', '2']:
            upload()
            None
        elif command.lower() in ['follow', '3']:
            bot()
            None
        elif command.lower() in ['exit', '4']:
            os.system('clear')
            break
        elif command.lower() in ['clear', '5']:
            os.system('clear')
            console()
        elif command.lower() in ['fix', '6']:
            shutil.rmtree('config')
            os.system('clear')
            console()
        else:
            print('Command Not Recognized') 
else:
    if sys.argv[1] == '-cli':
        if sys.argv[2] == '-up':
            upload()
        elif sys.argv[2] == '-fol':
            bot()
        elif sys.argv[2] == '-con':
        
            while True:
                time = datetime.datetime.now()
                hr = time.hour
                min = time.minute

                if min == 0:
                    try:
                        upload()
                        sleep(60)
                    except:
                        print('Upload Failed.')
                else:
                    os.system('clear')
                    print(f'Current Time: {hr}:{min}')
        
        elif sys.argv[2] == '-confol':
            while True:
                time = datetime.datetime.now()
                hr = time.hour
                min = time.minute

                if hr == 21 and min == 3:
                    try:
                        bot()
                        sleep(60)
                    except:
                        print('Follow Script Failed. Trying again tomorrow.')
                else:
                    os.system('clear')
                    print(f'Current Time: {hr}')
            
        else:
            None

