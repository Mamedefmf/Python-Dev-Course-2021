#SLICES

persons=("John", "Mamede", "Bruna", "Rogéria", "Almeida")
    # [start_range:end_range:step]
#for i in persons [::0]:
#    print (i)

name = "Bruna"
print(name[0:2])



""" ---------------- Functions and Tuples
def get_informations():
    return "Bruna", 27, 1.70  # Python automatically generates a Tuple


def display_information(name, age, height):
    print(f"{name}, {age} years old, {height}m of height")


# Display Option 3

info = get_informations()
# display_information(info) >>> this won't work because display_information needs 3 arguments. This will put the
#                           tuple (container), not the separate arguments

display_information(*info) # the    *    before a tuple will unpack it
"""


# Display Option 1
"""
info = get_informations()
print(info) # complete tuple
print("Name: " + (info[0]))
print("Age: " + str(info[1]))
print("Height: " + str(info[2])) """

# Display Option 2
"""
name, age, height = get_informations()   # This will work too
print(name)
print(age)
print(height)
"""

""" ---------- LIST ----------
persons = ["Almeida", "Bruna", "Suria", "Mamede"]
new_persons = "Fabio"
persons.append(new_persons)
print(persons)



def change_value(a):
    a[0] = 10

test = [1, 2, 3, 4]
change_value(test)
print(test)
"""

""" ---------- TUPPLES  -----------
a = "Mamede" # Theoretically the String "John" is a collection of Letters
print(a[0]) # The positive Index will aways start at 0
print(a[-1]) # If you use a negative Index like -1 it will select the last item of the collection and count backwards
print()

values = range(0, 9) # = tupple (0,1,2,3,4,5,6,7,8)
print(values[-1])


# index:       0         1        2        3
persons = ("Almeida", "Bruna", "Suria", "Mamede")
# neg. index  -4        -3       -2       -1
print(len(persons)) # the len function will count the collection items = 4
print(len(a)) # Counting Mamede = 6 letters
print()


persons = ("Almeida", "Bruna", "Suria", "Mamede")
for i in range(0, len(persons)):
    print(i)

for i in persons:
    print(i)

print()

values = range(0, 9) # = tupple (0,1,2,3,4,5,6,7,8)
print(values[-1])
print(len(values))

"""
