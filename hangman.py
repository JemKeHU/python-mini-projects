import random

def get_word(lst):
    return random.choice(lst).upper()

word_list = [
    "apple", "bridge", "cloud", "desert", "eagle", "forest", "garden", "honey",
    "island", "jungle", "kitchen", "lantern", "mountain", "notebook", "ocean",
    "pencil", "quartz", "rocket", "sandwich", "tunnel", "umbrella", "valley",
    "window", "xylophone", "yogurt", "zebra", "anchor", "balloon", "candle",
    "drum", "engine", "feather", "glove", "hammer", "igloo", "jacket", "kite",
    "ladder", "mirror", "needle", "orange", "pirate", "queen", "rainbow",
    "snowman", "train", "violin", "whistle", "yarn", "zipper"
]

def break_string(string):
    res = []
    for char in string:
        res.append(char)
    return res

def display_hangman(tries):
    stages = [  
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   |
                   | SALADYN, TY
                   | KURWO JEBANA
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def handle_input():
    while True:
        word_or_char = input("Type in a letter: ")
        if word_or_char.isalpha():
           return word_or_char.strip().upper()
        else:
            print("Please type in a letter or an entire word!") 

def play(word):
    word_completion = "_" * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play a word guessing game!")
    while True:
        user_input = handle_input()

        if user_input in word and len(user_input) == 1 and not user_input in guessed_letters:
            word_completion = break_string(word_completion)
            for i in range(len(word)):
                if word[i] == user_input:
                    word_completion[i] = word[i]
            word_completion = "".join(word_completion)
        elif len(user_input) == len(word):
            if user_input == word:
                print(f"You win in {tries} tries!")
                break
            else:
                print("Incorrect answer!")
                tries -= 1
        else:
            print("Incorrect answer!")
            tries -= 1

        if tries == 0:
            print("You lost!")
            print(f"The word is {word}")
            break

        if word_completion == word:
            print(f"You win in {tries} tries!")
            break

        if len(user_input) == 1:
            guessed_letters.append(user_input)
        else:
            guessed_words.append(user_input)
    
        print(display_hangman(tries))
        print(word_completion)
        print(f"Guessed letters: {", ".join(guessed_letters)}")
        print(f"Guessed words: {", ".join(guessed_words)}") 
play(get_word(word_list))