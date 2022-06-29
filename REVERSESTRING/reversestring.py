#define class reverse string
class reverse_string:
    #define function within class taking self and reverse argument self is itself and reverse is argument provided by user
    def reverse_words(self, reverse):
        # backwards splits the reverse arg provided by user and then reverses the list 
        backwards = reversed(reverse.split())
        #joins the list into a string rather then a list for easy reading
        end= ' '.join(backwards)
        #return the end variable 
        return end
#request user enter a string to reverse
reverse= input("Enter a string you want to reverse: ")
#print the result call the reverse string class and the reverse words function provideing the reverse variable as an argument
print(reverse_string().reverse_words(reverse))