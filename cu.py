from random import randint

def is_valid(st):
    return st.isdigit() and 1 <= int(st) <= second_num

try_count = 0
print("Welcome to the number guessing game!")
print("Type in a second number:")
second_num = int(input())
random_number = randint(1, second_num)
choice = "y"
print(f"Guess a number from 1 to {second_num}")

while True:
    num = input()
    if is_valid(num):
        num = int(num)
    else:
        print(f"Type in a NUMBER from 1 to {second_num}!")
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
        print(f"You guessed the number in {try_count} tries, congratulations!")
        
    print("Want to try again (y/n)?")
    choice = input()
    if choice == "y":
        try_count = 0
        print("Type in a second number:")
        second_num = int(input())
        random_number = randint(1, second_num)
        print(f"Guess a number from 1 to {second_num}")
    else:
        break

print("Thanks for playing, see you next time!")