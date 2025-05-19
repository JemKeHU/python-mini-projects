from random import choice

digits = "23456789"
lowercase_letters = "abcdefghjkmnpqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKMNPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
bad_chars = "il1Lo0O"
chars = ""

def generate_password(length, chars):
    result = ""
    for i in range(length):
        result += choice(chars)
    return result

def yes_or_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ["y", "n"]:
            return answer == "y"
        print("Please enter 'y' or 'n'")

def get_pref():
    count = int(input("How many passwords to generate? "))
    length = int(input("Length of each password? "))
    digits_on = yes_or_no("Include digits")
    upper_on = yes_or_no("Include uppercase letters")
    lower_on = yes_or_no("Include lowercase letters")
    punct_on = yes_or_no("Include punctuation letters")
    ambig_on = yes_or_no("Include ambiguous letters")
    return count, length, digits_on, upper_on, lower_on, punct_on, ambig_on

def chars_set(dig, up, low, punc, amb):
    chars = ""
    if dig:
        chars += digits
    if up:
        chars += uppercase_letters
    if low:
        chars += lowercase_letters
    if punc:
        chars += punctuation
    if amb:
        chars += bad_chars
    return chars

def main():
    count, length, use_digits, use_upper, use_lower, use_punct, use_ambiguous = get_pref()
    chars = chars_set(use_digits, use_upper, use_lower, use_punct, use_ambiguous)

    if not chars:
        print("No character types selected. Cannot generate password.")
        return 

    for i in range(count):
        print(generate_password(length, chars))

main()