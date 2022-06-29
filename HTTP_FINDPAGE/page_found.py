##import urllib

import urllib.request

##function for getting requested page from user
def get_page():
    ##site input for what website the user wants to search
    site = input("What site do you want to search? ex. amazon.com: ")
    ##what page are they looking for?
    request = input("What page are you looking for?: ")
    ##if user enters http://www. then no need to add it to the input
    if (site.find('http://www.') != -1):
        ##Call stat function to find page
        ##combine both inputs for functioning url
        new = site + '/' + request
        stat(new)
    ##else then add the http:// to the users input
    else:
        ##add to user input
        site = 'http://www.' + site
        new = site + '/' + request
        ##call stat function
        stat(new)

##stat function to find status
def stat(new):
    ##try except for errors to get page status try to open page 
    try:
        status = urllib.request.urlopen(new)
    ##if HTTP error occurs print error message with error code
    except urllib.error.HTTPError as error:
        code = error.code
        print("Sorry, page is down HTTP Error for {} is {}." .format(new, code))
    ## if no HTTP error then print a success message with status code of page
    else: 
        code = status.code
        print("Looks good {} returns a {} code." .format(new, code))

##call get page to start the program
get_page()
