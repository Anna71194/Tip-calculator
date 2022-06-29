##import urllib
from urllib.request import urlopen

##function to print robot text
def robot():
    ##assign site to urlopen capella.com/robot.txt
    site = urlopen("https://www.capella.edu/robots.txt")
    ##Print the downloaded file by reading and decode it with UTF-8
    print(site.read().decode("utf-8"))

##call robot function
robot()