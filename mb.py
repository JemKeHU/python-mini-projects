from random import choice
from time import sleep

answers = ["Certainly", "It's a foregone conclusion", "No doubt about it", "Definitely yes", "You can be sure of it", "I think so", "Most likely", "Good prospects", "Signs say yes", "Yes", "It's not clear yet, try again", "Ask later", "Better not to tell", "It's impossible to predict now", "Concentrate and ask again", "Don't even think about it", "My answer is no", "According to my data - no", "The prospects are not very good", "Very doubtful"]

def continue_game():
    while True:
        print("Wanna continue? (y/n)")
        choice = input()
        if choice.lower() == "y":
            return True
        elif choice.lower() == "n":
            return False
        else:
            print("Unknown answer, type in 'y' or 'n'")

def is_not_legal(st):
    return st.strip() == ""

def answer_logic():
    print("Enter your question:")
    question = input()
    if is_not_legal(question):
        print("You need to ask something!")
    else:
        sleep(1)
        print(choice(answers))

        
def game():
    print("Hello World, I am a magic ball and I know the answer to any question you have.")
    print("What is your name?")
    name = input()
    print(f"Hello {name}")
    while True:
        answer_logic()
        if continue_game():
            continue
        else:
            break
    print("Come back if you have some questions!")
game()