from setuptools import find_packages, version
from setuptools import setup

setup(
    name='AutomatedInstagram',
    version='1.0.0',
    description='Instagram Theme Page Automation Kit',
    author='Branin Podolski',
    author_email='marshallbranin@gmail.com',
    url='https://github.com/braninpodolski/Automated_Instagram',
    install_requires=['instabot', 'instaloader', 'configparser', 'art', 'praw']
)