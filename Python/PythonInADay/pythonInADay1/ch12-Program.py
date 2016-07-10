#ch12 Program
'''
# Our epic programmer dict from before
epic_programmer_dict = {
    'Tim Berners-Lee' : 'tbl@gmail.com',
    'Guido van Rossum' : 'gvr@gmail.com',
    'Linus Torvalds': 'lt@gmail.com',
    'Larry Page' : 'lp@gmail.com',
    'Sergey Brin' : 'sb@gmail.com',
    }

print epic_programmer_dict

###2
# Our epic programmer dict from before
epic_programmer_dict = {
    'Tim Berners-Lee' : ['tbl@gmail.com', 111],
    'Guido van Rossum' : ['gvr@gmail.com', 222],
    'Linus Torvalds': ['lt@gmail.com', 333],
    'Larry Page' : ['lp@gmail.com', 444],
    'Sergey Brin' : ['sb@gmail.com', 555]
    }
print epic_programmer_dict

###3

# Search for Tim Berners-Lee
print epic_programmer_dict['Tim Berners-Lee']

# Search for Tim Berners-Lee and get his number
print epic_programmer_dict['Tim Berners-Lee'][0]

#another way
programmer = epic_programmer_dict['Tim Berners-Lee']
print programmer[1]


###4

# Whatever the user types in = personsName
personsName = raw_input('Please enter a name: ')
print personsName

###5

# Asks user to input persons name
personsName = raw_input('Please enter a name: ')

# Looks up the name in the epic dictionary
personsInfo = epic_programmer_dict[personsName]
print personsInfo


###6

# Asks user to input persons name
personsName = raw_input('Please enter a name: ')

# Looks up the name in the epic dictionary
try:
    # Tries the following lines of texts, and if there isn't any errors then it runs
    personsInfo = epic_programmer_dict[personsName]
    print personsInfo
except:
    # If there are errors, then this code gets run.
    print 'No information found for that name'


###7
# Our epic programmer dict with lowercase names
epic_programmer_dict = {
    'tim berners-lee' : ['tbl@gmail.com', 111],
    'guido van rossum' : ['gvr@gmail.com', 222],
    'linus torvalds': ['lt@gmail.com', 333],
    'larry page' : ['lp@gmail.com', 444],
    'sergey brin' : ['sb@gmail.com', 555]
    }

## Asks user to input persons name - converts to lowercase
personsName = raw_input('Please enter a name: ').lower()

# Looks up the name in the epic dictionary
try:
    # Tries the following lines of texts, and if there isn't any errors then it runs
    personsInfo = epic_programmer_dict[personsName]
    print personsInfo
except:
    # If there are errors, then this code gets run.
    print 'No information found for that name'

###8

# Asks user to input persons name - converts to lowercase
personsName = raw_input('Please enter a name: ').lower()

# Looks up the name in the epic dictionary
try:
    # Tries the following lines of texts, and if there aren't any errors then it runs
    personsInfo = epic_programmer_dict[personsName]
    print 'Name: ' + personsName.title() #title makes it uppercase
    print 'Email: ' + personsInfo[0]
    print 'Number: ' + str(personsInfo[1]) #make string to concatenate
except:
    # If there are errors, then this code gets run.
    print 'No information found for that name'

###9 looping
# Our epic programmer dict
epic_programmer_dict = {
    'tim berners-lee' : ['tbl@gmail.com', 111],
    'guido van rossum' : ['gvr@gmail.com', 222],
    'linus torvalds': ['lt@gmail.com', 333],
    'larry page' : ['lp@gmail.com', 444],
    'sergey brin' : ['sb@gmail.com', 555]
    }

# Asks user to input persons name
personsName = raw_input('Please enter a name: ').lower()

# Looks up the name in the epic dictionary
try:
    # Trys the following lines of texts, and if there isn't any errors then it runs
    personsInfo = epic_programmer_dict[personsName]
    print 'Name: ' + personsName.title()
    print 'Email: ' + personsInfo[0]
    print 'Number: ' + str(personsInfo[1])
except:
    # If there are errors, then this code gets run.
    print 'No information found for that name'

# Adding the loop
userWantsMore = True
while userWantsMore == True:
    # Code goes here
    userWantsMore = False

###10
# Our epic programmer dict
epic_programmer_dict = {
    'tim berners-lee' : ['tbl@gmail.com', 111],
    'guido van rossum' : ['gvr@gmail.com', 222],
    'linus torvalds': ['lt@gmail.com', 333],
    'larry page' : ['lp@gmail.com', 444],
    'sergey brin' : ['sb@gmail.com', 555]
    }

def searchPeople(personsName):
    # Looks up the name in the epic dictionary
    try:
        # Trys the following lines of texts, and if there isn't any errors then it runs
        personsInfo = epic_programmer_dict[personsName]
        print 'Name: ' + personsName.title()
        print 'Email: ' + personsInfo[0]
        print 'Number: ' + str(personsInfo[1])
    except:
        print 'No information found for that name' # If there are errors, then this code gets run.

userWantsMore = True
while userWantsMore == True:
    personsName = raw_input('Please enter a name: ').lower() # Asks user to input persons name
    searchPeople(personsName)# Run our new function searchPeople with what was typed in
    userWantsMore = False
    
'''
###11
# Our epic programmer dict from before
epic_programmer_dict = {
    'tim berners-lee' : ['tbl@gmail.com', 111],
    'guido van rossum' : ['gvr@gmail.com', 222],
    'linus torvalds': ['lt@gmail.com', 333],
    'larry page' : ['lp@gmail.com', 444],
    'sergey brin' : ['sb@gmail.com', 555]
    }


def searchPeople(personsName):
    # Looks up the name in the epic dictionary
    try:
        # Trys the following lines of texts, and if there isn't any errors then it runs
        personsInfo = epic_programmer_dict[personsName]
        print 'Name: ' + personsName.title()
        print 'Email: ' + personsInfo[0]
        print 'Number: ' + str(personsInfo[1])
    except:
        # If there are errors, then this code gets run.
        print 'No information found for that name'

userWantsMore = True
while userWantsMore == True:
    # Asks user to input persons name
    personsName = raw_input('Please enter a name: ').lower()

    # Run our new function searchPeople with what was typed in
    searchPeople(personsName)

    # See if user wants to search again
    searchAgain = raw_input('Search again? (y/n)')

    # Look at what they reply and act accordingly
    if searchAgain == 'y':
        # userWantsMore stays as true so loop repeats
        userWantsMore = True
    elif searchAgain == 'n':
        # userWantsMore turns to False to stop loop
        userWantsMore = False
    else:
        # user inputs an invalid response, so we quit anyway
        print "I dont understand what you mean, quitting"
        userWantsMore = False

