from instabot import Bot
import hashtag_scraper
import os 
import glob

# Clear cookies for login
cookie_del = glob.glob("config/*cookie.json")
if cookie_del:
    os.remove(cookie_del[0])


# Input hashtag to scrape
hashtag = input("Hashtag: ")

# Create bot and login
bot = Bot()
bot.login(username='', password='')

# Download Image
hashtag_scraper.main(hashtag)

# Fetch filename
path = ('#' + hashtag + '/')
filename = glob.glob('*/*.jpg')
for file in glob.glob('*/*.jpg'):
    print(file)
print(filename)
print(path)

#bot.upload_photo()

