#ch9 Dictionaries

# Make the dictionary
dictionary_name = { 'item_1' : 1, 'item_2' : 2, 'item_3' : 3 }

# Search dictionary for 'item_1' and retrieve its data
print dictionary_name['item_1']

###

# Create programmer dictionary
epic_programmer_dict = {'Tim Berners-Lee' : 'tbl@gmail.com',
                        'Guido van Rossum' : 'gvr@gmail.com',
                        'Linus Torvalds': 'lt@gmail.com' }

# Check dictionary is working
print epic_programmer_dict
print epic_programmer_dict['Tim Berners-Lee']

###


# Changes email address
epic_programmer_dict['Tim Berners-Lee']='tim@gmail.com'

print 'new email for tim: '+epic_programmer_dict['Tim Berners-Lee']


###

# Add Larry Page and his email to the dic
epic_programmer_dict['Larry Page']='lp@gmail.com'
print epic_programmer_dict

###

# Add more programmers to the dictionary
epic_programmer_dict['me']='me@gmail.com'
epic_programmer_dict['sergey brin']='sb@gmail.com'
print epic_programmer_dict

del epic_programmer_dict['sergey brin']
print epic_programmer_dict

