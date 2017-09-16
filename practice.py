
# Function
def myFunc(param1, param2)
    return param1+param2

# Class
class Square():
    def __init__(self, a):
        self.a = a
    def Area(self)
        reutn a*a


print("Hello World!!")

# init stuff
x = 2
some_text = "hello world again"

# working with conditions
if x == 1:
    # indented four spaces
    print("x is 1.")
elif x==0:
    print("Who the fuck are you")
else:
    print("you are a nut ball.")
print('\n')

# and if want to work with a SWITCH statement you can use a dictionary (really powerful tool of python)
choices = {'a': 1, 'b': 2 , 'default' : 'deep'}
print ( choices)
#deleting an item from the dictionary
del choices['a']
print(choices)
print("successfully deleted the item 'a'")
print('\n')

# Strings

# splitting a text to a string array by their spaces
splitWords = some_text.split(" ")
print(splitWords[0])
print(splitWords[1])
print(splitWords[2])
print('\n')


#joining words 
words = ["this", "is", 'a', 'list', 'of', 'strings']
print(" ".join(words))


# functions with arrays:
thelist = [5,3,‘p’,9,‘e’]
print("The list length: "+len(thelist) )
print("the sorted list: "+ thelist.sort())
#you can remove with an index using the method pop
#you can remove with the value/key
print('\n')
