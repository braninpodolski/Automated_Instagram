import configparser
from functions import upload
from follow_bot import bot
from configparser import RawConfigParser
import sys
from art import *
import os

# Import config preferences
file = 'config.ini'
config = RawConfigParser()
config.read(file)

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

    hashtag = input('Hashtag to Scrape Posts From (DO NOT INCLUDE POUND SYMBOL): ')
    config.set('preferences', 'hashtag', hashtag.replace('#', '')) 
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
    ''')

console()

# Menu Input Interface
while True:
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
    else:
        print('Command Not Recognized') 