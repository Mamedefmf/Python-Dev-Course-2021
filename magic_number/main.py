import random

def ask_number (min, max):
    number_int = 0
    while number_int == 0:
        number_str = input(f"What is the magic number ?\nType a number between {min} and {max} : ")
        try:
            number_int = int(number_str)
        except:
            print("INPUT ERROR: You need to type a valid number")
        else:
            if number_int < min or number_int > max:
                print(f"INPUT ERROR: You must give a number between {min} and {max}")
                number_int = 0
    return number_int


MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)
NB_LIVES = 4

number = 0
lives = NB_LIVES

while not number == MAGIC_NUMBER and lives > 0:
    print(f"You have {lives} attempts left")
    number = ask_number(MIN_NUMBER, MAX_NUMBER)
    if number > MAGIC_NUMBER:
        print(f"{number} is greater than the Magic Number")
        lives -= 1 # subtract 1 live
    elif number < MAGIC_NUMBER:
        print(f"{number} is lower than the Magic Number")
        lives = lives - 1 # subtract 1 live
    else:
        print(f"You Won! the Magic Number is {MAGIC_NUMBER}\n Congratulations !!!")

if lives == 0:
    print(f"You Lost!\nThe magic number was: {MAGIC_NUMBER}")