##store lines function to  import file and store each line into a list
def store_lines():
    ##list creation
    st_list= []
    print('Normal Text:')
    ##open sample tect as variable text
    with open('sample.txt') as text:
        #loop to iterate through sample.txt lines and store them to list
        while True:
            ##store lines in the sample text to variable called lines
            lines = text.readline()
            ##strip white space at begining and end
            lines.strip()
            ##print the original document
            print(lines)
            #insert the lines from sample.txt at st_list at pointer 0 to reverse list
            st_list.insert(0, lines)
            #break case
            if not lines:
                break
    #return st_list to print_story function
    print_story(st_list)

##print story function to return function 
def print_story(st_list):
    ##reverse string created with no entry
    reverse = ''
    ##for loop to iterate over st_list to join list to string
    for i in st_list:
                line=str(i)
                ##enter new line for spacing
                reverse += "\n"
                ##compound the line to the reverse string variable to make one string
                reverse += line
    ## print the reversed string
    print("Reversed Text:")
    print(reverse)

##call first function
store_lines()
