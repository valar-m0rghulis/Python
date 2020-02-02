
# Substrings.

my_string = """Strings are amongst the most popular data types in Python.
We can create the strings by enclosing characters in quotes.
Python treats single quotes the same as double quotes."""

def count_words(string):
    endcount = 0
    incount = 0
    string = string.split()
    for word in string:
        if word[ -1 : ] in ('.', ','):
            word = word[ 0 : -1 ]
        if word[ -2 : ] == 'on':
            endcount += 1
        word = word[ 1 : -1 ]
        if 'on' in word:
            incount += 1
            
    print("Words ending with 'on' : ",endcount)
    print("Words containing 'on' in: ",incount)

print("Count of 'string':",my_string.lower().count("string"))    
count_words(my_string)


'''
OUTPUT :

Count of 'string': 2
Words ending with 'on' :  2
Words containing 'on' in:  1

'''
