# ch10 Functions

#Format
'''
def someFunction(<input variables>):
    <do stuff here with variables>
    return <some value>
'''

# Make function called letsAdd
def letsAdd(x,y):
    addition = x + y # Make addition variable equal to x + y
    return addition # Return addition variable
print letsAdd(3, 5) # Print results to console


###

# Make function called letsAdd
def letsAdd(x,y):
    addition = x + y  # Make addition variable equal to x + y
    someValue = 10 # See how putting this in function does not affect outside of function
    return addition  
print letsAdd(3, 5)
# print someValue get error

###


someValue = 5
# Make function called letsAdd
def letsAdd(x,y):
    # Make addition variable equal to x + y
    addition = x + y
    someValue = 10 # See how putting this in function does not affect outside of function

print someValue

###

# Make function called subtraction
def subtraction(x,y):
    subtract = x-y
    return subtract
print subtraction(10,4)

    
###
def moreSubtraction(x,y,z):
    subtract = x-y-z
    return subtract
print moreSubtraction(40,3,11)

###

def divide(a,b):
    c=float(a)/float(b)
    return c
print divide(100,2)

###

length = len("How epic are built-in functions, huh?")
print length

###

# convert to string
x = 23
print str(x)

# convert to float
y = float(40)/float(7)
print y

yInt = int(y)
print yInt

print round(y)
print int(round(y))




    
