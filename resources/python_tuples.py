'''
The difference between a list and a tuple is that a tuple is immutable, meaning it cannot be changed.
A list is mutable, meaning it can be changed.
A tuple is a sequence of values separated by commas and enclosed in parentheses.
A list is a sequence of values separated by commas and enclosed in square brackets.'''

#Example List:
my_list = ['a', 'b', 'c', 'd', 'e']
my_list.append('f') # <--add an item to the end of the list
my_list[1] = 'z' # <--change the value of an item in the list
my_list.remove('c') # <--remove an item from the list

#Example Tuple:
my_tuple = ('a', 'b', 'c', 'd', 'e')
#my_tuple.append('f') # <--this will throw an error because tuples are immutable
#my_tuple[1] = 'z' # <--this will throw an error because tuples are immutable
#my_tuple.remove('c') # <--this will throw an error because tuples are immutable


'''
Use Cases:
Use a tuple when you want to store a sequence of values that will not change.
Use a list when you want to store a sequence of values that may change.
'''