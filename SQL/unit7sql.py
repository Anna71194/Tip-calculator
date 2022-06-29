##import sql database ability
import sqlite3

##connect to database
contact = sqlite3.connect('contacts.db')
##create a cursor
cur = contact.cursor()

##select three columns from the contact database function
def select_three_columns():
    ##craft query to hold passed syntax to system
    query = 'SELECT FirstName, LastName, EmailAddress FROM contact '
    ##call print function to display results
    print_results(query)

##update function to update row in contact database
def update_statement():
    ##use global curson
    global cur
    ##craft query to change information for contactid 31
    query = "UPDATE contact SET EmailAddress = 'Csmith20@yahoo.com', PhoneNumber = '320-239-1212' WHERE ContactID = 31"
    ##run query
    cur.execute(query)
    ##recraft query to display all rows of contact to reflect change
    query = 'SELECT * FROM contact'
    ##call print results function
    print_results(query)

##delete statment function to delete last row
def delete_statement():
    ##use global cursor
    global cur
    ##craft delete syntax to remove row where primary key is 8
    query = "DELETE FROM contact WHERE ContactID = 8"
    ##execute the function
    cur.execute(query)
    ##recraft query to display all contact database data to reflect change
    query = 'SELECT * FROM contact'
    ##print results function
    print_results(query)

##orint results function passing query
def print_results(query):
    ##global cursor import
    global cur
    global contact
    x = 0
    ##print query for user visability
    print(query)
    cur.execute(query)
    ##execute query to database and then display each row to user 
    while x < 5:
        print(cur.fetchone())
        x += 1
    ##enter new line
    print('\n')
    ##commit changes to database
    contact.commit()

##call functions
select_three_columns()
update_statement()
delete_statement()
##Close the database
contact.close()