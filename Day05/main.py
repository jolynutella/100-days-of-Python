# This program generates a password with desired parameters

import random

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password = ""
randomized_password = ""

for _ in range(1, num_letters + 1):
    password += random.choice(letters)

for _ in range(1, num_symbols + 1):
    password += random.choice(symbols)

for _ in range(1, num_numbers + 1):
    password += random.choice(numbers)

for _ in range(1, len(password) + 1):
    randomized_password += random.choice(password)

print(f"Here is your password: {str(randomized_password)}")