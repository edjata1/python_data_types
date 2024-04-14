# string 

print("-------- literal assignment ----------")
# literal assignment
first = "Empress"
last = "Djata"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))
print(type(last))
print(type(last) == int)
print(type(last) == float)

print("-------- constructor function ----------")
# constructor function
pizza = str("Extra Cheese")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

print("-------- concatenation ----------")
fullname = first + " " + last
print(fullname)
fullname += "!"
print(fullname)

print("-------- casting number to a string ----------")
decade = str(1990)
print(type(decade))
print(decade)

statement = "I love rap music from the " + decade + "'s."
print(statement)

print("-------- multiple lines ----------")

mulptiline = '''
Hey Buddy, how are you?                                    

I was just checking on you.            
                             All Good??

'''
print(mulptiline)

print("-------- Escaping special characters ----------")
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

print("-------- String Methods ----------")
print(first)
print(first.lower())
print(first.upper())
print(first.title())
print(first)

print(mulptiline.title())
print(mulptiline.replace("Good", "ok"))
print(mulptiline)

print(len(mulptiline))
mulptiline += "                                                                         "
mulptiline = "                            " + mulptiline
print(len(mulptiline))

print(len(mulptiline.strip()))
print(len(mulptiline.lstrip()))
print(len(mulptiline.rstrip()))
print(len(mulptiline))
r_strip = len(mulptiline.rstrip())
print(r_strip)

print("")
print("-------- Build a menu ----------")
title = "mean".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$3.00".rjust(4))
print("Tea".ljust(16, ".") + "$1.00".rjust(4))
print("Muffin".ljust(16, ".") + "$2.25".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4.75".rjust(4))
print("Beer".ljust(16, ".") + "$5.00".rjust(4))

print("")
print("-------- string index value ----------")
print(first[1])
print(first[-1])
print(first[1:-1]) # range from index 1 to end "-1" <-- not part of output
print(first[1:]) # range from index 1 to "end" <-- included

print()
print("-------- Some methods return boolean data ----------")
print(first.startswith("Em"))
print(first.endswith("Z"))

print()
print("-------- boolean data type ----------")
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

print()
print("-------- numeric data type ----------")

# integers type
print("******* integer type *******")
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
print("******* float type *******")
gpa = 3.83
y = float(1.5)
print(type(gpa))
print(isinstance(y, float))

# complex type
print("******* complex type *******")
comp_value = 4 + 7j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built-in functions for numbers
print("******* built-in functions for numbers *******")
print(type(gpa))
print(type(gpa * -2))
print(round(gpa))
print(round(gpa, 2))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to a number 
print("******* casting a string to a number *******")
zipcode = "10475"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attemp to cast incorrect data, example:
# zip_value = int("New York City")



























































































