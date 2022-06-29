import sqlite3

contact = sqlite3.connect('contacts.db')
cur = contact.cursor()

cur.execute('''CREATE TABLE contact (ContactID INT PRIMARY KEY, FirstName char(50), LastName char(50), PhoneNumber char(15), EmailAddress char(50))''')


contact.commit()
contact.close()

if sqlite3.connect('contacts.db'):
    print('Database Created.')
    contact.close()




