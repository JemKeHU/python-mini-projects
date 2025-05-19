from random import randint

def get_range():
    while True:
        print("Type in a second number:")
        n = input()
        if n.isdigit() and int(n) > 1:
            return int(n)
        else:
            print("Please type in a NUMBER greater than 1!")

def start_game():
    second_num = get_range()
    random_number = randint(1, second_num)
    print(f"Guess a number from 1 to {second_num}")
    return second_num, random_number

def continue_game():
    while True:
        print("Want to try again (y/n)?")
        choice = input()
        return choice.lower() == "y"

def compare(second_num, random_number):
    try_count = 0
    while True:
        num = input()
        if num.isdigit() and 1 <= int(num) <= second_num:
            num = int(num)
        else:
            print(f"Type in a NUMBER from 1 to {second_num}")
            continue
        if num > random_number:
            try_count += 1
            print("Too high, try again")
            continue
        elif num < random_number:
            try_count += 1
            print("Too low, try again")
            continue
        else:
            try_count += 1
            print(f"You guessed the number in {try_count} tries, congratulations!")
            try_count = 0
            break

def game():
    print("Welcome to the number guessing game!")
    while True:
        s_n, r_n = start_game()
        compare(s_n, r_n)
        if not continue_game():
            break
    print("Thanks for playing, see you next time!")

game()