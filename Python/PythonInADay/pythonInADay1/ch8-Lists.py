#ch8 Lists

# Create the list of epic programmers
epic_programmer_list = ["Tim Berners-Lee",
                        "Guido van Rossum",
                        "Linus Torvalds",
                        "Larry Page",
                        "Sergey Brin",]

#print "epic programmers:" + epic_programmer_list
#get error

print "an epic programmer:" + epic_programmer_list[0]
print "an epic programmer:" + epic_programmer_list[1]
print "an epic programmer:" + epic_programmer_list[2]
print "an epic programmer:" + epic_programmer_list[3]
print "an epic programmer:" + epic_programmer_list[4]

epic_programmer_list.append("Me")
print epic_programmer_list

#looping through programmer list, print programmer name to console
for programmer in epic_programmer_list:
    print programmer

#looping through programmer list, print intro and name to console
for programmer in epic_programmer_list:
    print "an epic programmer: " + programmer

#create list of numbers
number_list=[0,1,2,3,4,5]

#print each to the power of 2
for x in number_list:
    print x**2


#append power of 2 to empty number list
empty_number_list=[]

for x in number_list:
    empty_number_list.append(x**2)
print empty_number_list

