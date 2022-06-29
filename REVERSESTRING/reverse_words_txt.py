class reverse_list:
    #define function within class taking self and reverse argument self is itself and reverse is argument provided by text file 
    def reverse_words(self, line):
        # backwards splits the reverse arg provided by text and then reverses the list 
        backwards = reversed(line.split())
        #joins the list into a string rather then a list for easy reading
        end= " ".join(backwards)
        #return the end variable 
        return end

def store_lines():
    #create f_list list to seperate lines in text
    f_list = []
    with open('sample.txt') as text:
        #loop to iterate through sample.txt lines and store them to list
        while True:
            ##store lines in the sample text to variable called lines
            lines = text.readline()
            ##add lines of text to list to seperate lines
            f_list.append(lines)
            #break case
            if not lines:
                break
    #call reverse list function
    reverse_l(f_list)

def reverse_l(f_list):
    #reverse list created
    reverse = []
    #iterate through original line list
    for i in f_list:
        x=str(i)
        #remove the periods, they look weird
        line = x.replace(".","")
        #call the reverse list class and reverse words function providing the line iteration as an argument
        reverse.append(reverse_list().reverse_words(line))
    #call list to string which will combine back the reverse list into a string
    list_to_string(reverse)

def list_to_string(reverse):
    #create final veriable string
    final = ''
    #iterate through reverse list to combine to readable string
    for i in reverse:
        line=str(i)
        ##enter new line for spacing
        final += "\n"
        ##compound the line to the reverse string variable to make one string
        final += line
    #call to print string
    print_string(final)

def print_string(final):
    #open file to read orignal contents
    f=open('sample.txt', 'r')
    #read file to user
    read_only=f.read()
    print("This is the normal file content:\n")
    print(read_only)
    #print the reversed string
    print("\nReversed text file line by line:")
    print(final)
    #close file
    f.close()

#call store_lines to start program
store_lines()