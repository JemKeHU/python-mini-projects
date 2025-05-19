eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

direction = input("Choose direction (enc/dec): ")
language = input("Language (ru/en): ")
step = int(input("Step size: "))
print("Your text:")
text = input()

result = ""

if direction == "enc":
    for char in text:
        if char.isalpha() and language.strip().lower() == "en":
            if char.islower():
                base = ord("a")
            else:
                base = ord("A")
            new_code = ord(char) + step
            if new_code > base + 25:
                result += chr(new_code - 26)
            elif new_code < base:
                result += chr(new_code + 26)
            else:
                result += chr(new_code)
        elif char.isalpha() and language.strip().lower() == "ru":
            if char.islower():
                base = ord("а")
            else:
                base = ord("А")
            new_code = ord(char) + step
            if new_code > base + 31:
                result += chr(new_code - 32)
            elif new_code < base:
                result += chr(new_code + 32)
            else:
                result += chr(new_code)
        else:
            result += char
elif direction == "dec":
    for char in text:
        if char.isalpha() and language.strip().lower() == "en":
            if char.islower():
                base = ord("a")
            else:
                base = ord("A")
            new_code = ord(char) - step
            if new_code > base + 25:
                result += chr(new_code - 26)
            elif new_code < base:
                result += chr(new_code + 26)
            else:
                result += chr(new_code)
        elif char.isalpha() and language.strip().lower() == "ru":
            if char.islower():
                base = ord("а")
            else:
                base = ord("А")
            new_code = ord(char) - step
            if new_code > base + 31:
                result += chr(new_code - 32)
            elif new_code < base:
                result += chr(new_code + 32)
            else:
                result += chr(new_code)
        else:
            result += char
print(result)