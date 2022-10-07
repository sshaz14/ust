import os
import sys

#key Error: This is raised when key does not exist in dict

try:
    my_dict = {'id':102, 'name':'Suresh', 'city':'Bangalore', 'dept':'IT'}
    print(my_dict['Name'])

except KeyError:
    print('KeyErroe Exception Raised')

#Index Error ...index of a sequence doesn't exist

try:
    mylist = [1,2,3,4,5,6]
    print(mylist[9])

except IndexError:
    print('IndexError Exception Raised')
