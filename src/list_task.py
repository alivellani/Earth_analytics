### Write an immutable function that merges the following inputs into a single list. (Feel free to use the space below or submit a link to your work.)

# Inputs
# - Original list of strings
# - List of strings to be added
# - List of strings to be removed

# Return
# - List shall only contain unique values
# - List shall be ordered as follows
# --- Most character count to least character count
# --- In the event of a tie, reverse alphabetical

# Other Notes
# - You can use any programming language you like
# - The function you submit shall be runnable

# For example:

# Original List = ['one', 'two', 'three',]
# Add List = ['one', 'two', 'five', 'six]
# Delete List = ['two', 'five']
# Result List = ['three', 'six', 'one']*

from collections import OrderedDict

def func(org,add,rem):
    
    # test if the all lists have all strings
    
    # add add to org
    org.extend(add)

    # remove duplicates
    res = list(OrderedDict.fromkeys(org))
    
    # remove del from added list
    res = [x for x in res if x not in rem]
    
    # sort the list size of elements and incase of tie, by reverse alphabetical order
    return sorted(res, key=lambda ele: (len(ele), ele), reverse=True)

