import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

### Create table named SIMPSON_INFO
##conn.execute("CREATE TABLE SIMPSON_INFO( \
##    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
##    NAME TEXT, \
##    GENDER TEXT, \
##    AGE INT, \
##    OCCUPATION TEXT \
##    );")

### Add Bart Simpson to table
##conn.execute("INSERT INTO SIMPSON_INFO \
##    (NAME, GENDER, AGE, OCCUPATION) VALUES \
##    ('Bart Simpson', 'Male', 10, 'Student' )");

### Add Homer Simpson to table
##conn.execute("INSERT INTO SIMPSON_INFO \
##    (NAME, GENDER, AGE, OCCUPATION) VALUES \
##    ('Homer Simpson', 'Male', 40, 'Nuclear Plant')");
##
### Add Lisa Simpson to table
##conn.execute("INSERT INTO SIMPSON_INFO \
##    (NAME, GENDER, AGE, OCCUPATION) VALUES \
##    ('Lisa Simpson', 'Female', 8, 'Student')");
##
### Save changes
##conn.commit()
##
### Print number of changes to database
##changes = conn.total_changes
##print "Number of changes:", changes

### Get data from database
##cursor = conn.execute("SELECT ID, NAME, GENDER, AGE, OCCUPATION from SIMPSON_INFO")
##print cursor

###same as above
### Get data from database
##cursor = conn.execute("SELECT * from SIMPSON_INFO")
##
### Extract data from cursor
##rows = cursor.fetchall()
##print rows
##
### Searching by character name
### Get data from database
##cursor = conn.execute("SELECT * from SIMPSON_INFO where NAME='Homer Simpson'")
##
### Extract data from cursor
##rows = cursor.fetchall()
##print 'Results for Homer Simpson:'
##print rows
##
### Searching for females
### Get data from database
##cursor = conn.execute("SELECT * from SIMPSON_INFO where GENDER='Female'")
##
### Extract data from cursor
##rows = cursor.fetchall()
##print 'Results for Females:'
##print rows
##
### Searching for students
### Get data from database
##cursor = conn.execute("SELECT * from SIMPSON_INFO where OCCUPATION='Student'")
##
### Extract data from cursor
##rows = cursor.fetchall()
##print 'Results for Students:'
##print rows

### Delete rows with ID=2
##conn.execute("DELETE from SIMPSON_INFO where ID=2")
##
### Save changes
##conn.commit()
##
### Print number of changes
##changes = conn.total_changes
##print "Number of changes: ",changes
##
### Get data from database
##cursor = conn.execute("SELECT * from SIMPSON_INFO")
##
### Extract data from cursor
##rows = cursor.fetchall()
##print rows

### Add Homer Simpson to table
##conn.execute("INSERT INTO SIMPSON_INFO \
##    (NAME, GENDER, AGE, OCCUPATION) VALUES \
##    ('Homer Simpson', 'Male', 40, 'Nuclear Plant')");
##
### Make Homer Simpson's age 41
##conn.execute("UPDATE SIMPSON_INFO set AGE=41 where NAME='Homer Simpson'")
##
### Save changes
##conn.commit()
##
### Print number of changes
##changes = conn.total_changes
##print "Number of changes: ",changes
##
### Get data from database
##cursor = conn.execute("SELECT * from SIMPSON_INFO")
##
### Extract data from cursor
##rows = cursor.fetchall()
##print rows

# Delete the table
conn.execute("DROP TABLE SIMPSON_INFO")

# Save changes
conn.commit()

# Print number of changes
changes = conn.total_changes
print "Number of changes: ",changes

# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO")

# Extract data from cursor
rows = cursor.fetchall()
print rows
#yup table was deleted
