# import the random module
import random

# constant variables
"""
minimum_number = minimum number that the random.randint can use
maximum_number = maximum number that the random.randint can use
number_questions = number of questions of the test
"""
# setting the difficulty
difficulty = 0
MIN_NUMBER = 0
MAX_NUMBER = 0
NB_QUESTIONS = 0

while difficulty == 0:
    difficulty = input("""Welcome to Math Challenge Python Game
    1. Casual | Numbers between 1 and 10 | 5 Questions
    2. Regular | Numbers between 1 and 100 | 10 Questions
    3. Hard - | Numbers between 1 and 1000 | 15 Questions
    4. Insane - | Numbers between 1 and 10000 | 20 Questions
    Please choose a difficulty: """)
    try:
        difficulty == int(difficulty)
    except:
        print("ERROR: You must insert a number")

if difficulty == 1:
    MIN_NUMBER = 1
    MAX_NUMBER = 10
    NB_QUESTIONS = 5
elif difficulty == 2:
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    NB_QUESTIONS = 10
elif difficulty == 3:
    MIN_NUMBER = 1
    MAX_NUMBER = 1000
    NB_QUESTIONS = 15
elif difficulty == 4:
    MIN_NUMBER = 1
    MAX_NUMBER = 10000
    NB_QUESTIONS = 20

""" this function generates tree random numbers
a and b are numbers between MIN_NUMBER and MAX_NUMBER
o(operator) is to randomly choose a math operator (+ - * or /)
after that it will return True or False
"""

def ask_question():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    o = random.randint(0, 4)
    default_o = "+"
    compute = a + b
    if o == 1:
        default_o = "-"
        compute = a - b
    elif o == 2:
        default_o = "*"
        compute = a * b
    elif o == 3:
        default_o = "/"
        compute = a / b
    user_answer = input(f"{a} {default_o} {b} = ")
    int_answer = int(user_answer)
    if int_answer == compute:
        return True

    return False

nb_points = 0
for i in range(1, NB_QUESTIONS + 1):
    print(f"Question {i} out of {NB_QUESTIONS}:")
    if ask_question():  # if ask_question is True do this
        print("Right answer")
        nb_points += 1
    else:  # if ask_question is False do this
        print("Wrong answer")

print(f"\nPoints: {nb_points}/{NB_QUESTIONS}")

average = int(NB_QUESTIONS / 2)
if nb_points == NB_QUESTIONS:
    print("Excellent")
elif nb_points == 0:
    print("You need to study math")
elif nb_points == average:
    print("Average Score")
elif nb_points < average:
    print("You can do better")
elif nb_points > average:
    print("Good Score")
