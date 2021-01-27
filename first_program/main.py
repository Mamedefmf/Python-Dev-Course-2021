# ask for the name function
def ask_for_name():
    name_Answer = ""
    while name_Answer == "":
        name_Answer = input("Insert the subject name: ")
    return name_Answer


# ask the age function
def ask_for_age(person_name):
    age_int = 0
    while age_int == 0:
        age_str = input(person_name + " what is his/her age? ")
        try:
            age_int = int(age_str)
        except:
            input_error()
    return age_int


# Input error function (just a test)
def input_error():
    print("Error: Input error. Wrong Format.")


# Display the results
def display_result(person_name, person_age, person_height):
    print("\nThe subject name is " + person_name + " and he/she is " + str(person_age) + " years old")
    print("Soon " + person_name + " will be " + str(person_age + 1) + " years old")

    if person_age <= 13:
        print("The subject is considered a Child")
    elif person_age <= 17:
        print("The subject is considered a Teen")
    elif person_age >= 60:
        print("The subject is considered a Senior")
    else:
        print("The subject is considered an Adult")


# ask the subject 1 and 2 for their names
name = ask_for_name()
name2 = ask_for_name()

# ask the subject 1 and 2 for their ages
age = ask_for_age(name)
age2 = ask_for_age(name2)

# display the results
display_result(name, age, height)
display_result(name2, age2, height2)

# Old Code:
"""

print("The subject name is " + name + " and he/she is " + str(age) + " years old")
print("The subject will be " + str(age + 1) + " years old either this year or the next.")

year = 0

while not year == 2021:
    year = input("What year we are? ")
    try:
        year = int(year)
    except:
        print("Error: Invalid Input")

print("Correct. We are currently in the year " + str(year))
"""
