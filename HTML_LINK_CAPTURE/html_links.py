##import requests and Beautiful soup
import requests
from bs4 import BeautifulSoup

##get_html function to get html document from the site we are requesting urls from
def get_HTML(site):
    ##assign html variable to requests.get(url we are using) to get html document text
    html = requests.get(site)
    ##return html document
    return html.text

##get url to get url for the html document
def get_url():
    ##scrape to take url 
    scrape="https://www.capella.edu"
    ##code to assign the html document from the get html 
    code= get_HTML(scrape)
    ##call parse code to actually get the urls from the assigned site
    parse(code)

##parse gets code that holds the html document of the url we requested
def parse(code):
    ## soup variable called from beautiful soup parser as control
    soup = BeautifulSoup(code,'html.parser')
    ##for loop over the link from beautiful soup find all <a> attributes
    for link in soup.find_all('a'):
        ##print results to console, every a field, get the line that starts with href (url assign in HTML) and display/
        print(link.get('href'))

##call get url to start program
get_url()

