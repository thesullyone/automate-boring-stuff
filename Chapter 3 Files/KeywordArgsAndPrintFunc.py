'''
Most arguments are identified by their position in the function call.
For example, random.randint(1, 10) is different from random.randint(10, 1). 
The function call random.randint(1, 10) will return a random integer 
between 1 and 10 because the first argument is the low end of the range 
and the second argument is the high end (while random.randint(10, 1) 
causes an error).

However, rather than through their position, keyword arguments are 
identified by the keyword put before them in the function call. Keyword 
arguments are often used for optional parameters. For example, the print()
function has the optional parameters end and sep to specify what should 
be printed at the end of its arguments and between its arguments (separating 
them), respectively.
'''

print('Hello')
print('World')

'''
The two outputted strings appear on separate lines because the print() 
function automatically adds a newline character to the end of the string 
it is passed. However, you can set the end keyword argument to change the 
newline character to a different string. For example, if the code were this:
'''

print('Hello', end='')
print('World')

'''
The output is printed on a single line because there is no longer a newline 
printed after 'Hello'. Instead, the blank string is printed. This is useful if 
you need to disable the newline that gets added to the end of every print() 
function call.

Similarly, when you pass multiple string values to print(), the function will 
automatically separate them with a single space.
'''
print('cats', 'dogs', 'mice')
# resolves to "cats dogs mice"
# but

print('cats', 'dogs', 'mice', sep=',')

# resolves to "cats,dogs,mice"


