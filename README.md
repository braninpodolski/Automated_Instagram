# Automated_Instagram
# Status
Due to updates to Instagram's website, this project no longer functions and is not being actively maintained.

# Installation
To install AutoInsta, run the following commands:

`git clone https://github.com/braninpodolski/Automated_Instagram`

`cd Automated_Instagram-master`

`sudo python3 setup.py install`

# How to Use
To get started, run `python3 instagram.py` within the AutomatedInstagram directory.


# Run Modes
## Default
Run `python3 instagram.py` to open the Command Line Graphical Menu.

## CLI Mode
CLI modes allows you to use command line arguments to specifiy functions without using the menu. Useful to automation through CronTab or Cloud Hosting.

### UP
Running `python3 instagram.py -cli -up` will scrape and upload a post using a single command

### FOL
Running `python3 instagram.py -cli -fol` will invoke the automated follow for follow function

### CON
Running `python3 instagram.py -cli -con` will start an indefinitely running instance of the script. Rather than uploading when told, it checks the time repeatedly and posts at predetermined times. Best used with cloud hosting services.


# Roadmap
- Allow for custom configuration of upload times when running via `-con`

