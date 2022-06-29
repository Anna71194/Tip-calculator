##import sql database ability
import sqlite3

##create a tuple of contacts to pull from

contacts = (31, 'Charles', 'Smith', '555-555-5555', 'CSmith@gmail.com', 99, 'Karen', "Dojo", '555-555-5558', 'KDojo20@yahoo.com', 77, 'Lauren', "Mcormick", '555-555-5522',
'LJMcormick@Outlook.com', 1 , 'Ben', 'Aswald', '555-222-1231', "BAsWal@gmail.com", 8, 'Mart', 'Dijan', '612-243-2341', 'Mhart00@yahoo.com' )
##connect to database
contact = sqlite3.connect('contacts.db')
##create a cursor
cur = contact.cursor()

##create the contact table with different rows and supplied values
cur.execute('''CREATE TABLE contact (ContactID INT PRIMARY KEY, FirstName char(50), LastName char(50), PhoneNumber char(15), EmailAddress char(50))''')

##commit our changes to the database
contact.commit()

##verify that database was created and print confirmation to user
if sqlite3.connect('contacts.db'):
    print('Database Created.')

##create new query to insert values into the contact table 5 ? for values to rows
query= 'INSERT INTO contact VALUES (?,?,?,?,?)'
args= 5
beg= 0
i=0
##create a new list to store only 5 values to pass to execute
vals = []

##5 entries, extend the vals list 5 tuple values to pull to the database
while i < 5:
    vals.extend(contacts[beg:args])
    cur.execute(query,vals)
    ##clear vals
    vals.clear()
    i+=1
    ##to change range of tuple indexes to pull from
    args+=5
    beg+=5
    ##print so user sees successful insert to database
    print('Entered {} rows into table contact' .format(i))

##commit to database to save data
contact.commit()

x = 0
##new query to pull data from contact
query='SELECT * FROM contact'
##print query for user visability
print(query)
cur.execute(query)
##execute query to datavase and then display each row to user 
while x < 5:
    print(cur.fetchone())
    x += 1

##Close the database
contact.close()