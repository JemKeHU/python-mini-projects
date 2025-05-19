from random import choice

def generate_password(length, chars):
    result = ""
    for i in range(length):
        result += choice(chars)
    return result

digits = "23456789"
lowercase_letters = "abcdefghjkmnpqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKMNPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
bad_chars = "il1Lo0O"
chars = ""

password_num = int(input("How many passwords: "))
password_length = int(input("Password length: "))
digits_on = input("Include digits? (y/n) ")
upper_on = input("Include uppercase letters? (y/n) ")
lower_on = input("Include lowercase letters? (y/n) ")
punct_on = input("Include punctiation characters? (y/n) ")
ambig_on = input("Include ambiguous characters? (y/n) ")

if digits_on == "y":
    chars += digits
if upper_on == "y":
    chars += uppercase_letters
if lower_on == "y":
    chars += lowercase_letters
if punct_on == "y":
    chars += punctuation
if ambig_on == "y":
    chars += bad_chars

for i in range(password_num):
    print(generate_password(password_length, chars))