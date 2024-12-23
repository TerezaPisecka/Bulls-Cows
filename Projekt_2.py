"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Tereza Písecká
email: pisecka.tereza@seznam.cz
discord: TerkaP terka_41921
"""

import random
import time

def generate_secret_number():
    while True:
        number = random.randint(1000, 9999)
        if len(set(str(number))) == 4:
            return str(number)

def validate_and_get_input():
    while True:
        guess = input("Enter a 4-digit number: ")
        if len(guess) != 4:
            print("Please enter exactly 4 digits.")
        elif not guess.isdigit():
            print("Only numbers are allowed. Please try again.")
        elif guess[0] == '0':
            print("The number cannot start with 0. Please try again.")
        elif len(set(guess)) != 4:
            print("Digits must not repeat. Please try again.")
        else:
            return guess

def evaluate_guess(secret, guess):
    bulls = 0
    cows = 0
    for s, g in zip(secret, guess):
        if s == g:
            bulls += 1
    for g in guess:
        if g in secret and g not in [secret[i] for i in range(len(secret)) if secret[i] == guess[i]]:
            cows += 1
    return bulls, cows

def bulls_and_cows():
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4-digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)

    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()

    while True:
        guess = validate_and_get_input()
        attempts += 1

        bulls, cows = evaluate_guess(secret_number, guess)
        
        if bulls == 4:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Correct! You guessed the right number in {attempts} attempts.")
            print(f"It took you {elapsed_time:.2f} seconds to win.")
            break
        else:
            bull_word = "bull" if bulls == 1 else "bulls"
            cow_word = "cow" if cows == 1 else "cows"
            print(f"{bulls} {bull_word}, {cows} {cow_word}")
            print("-" * 47)

if __name__ == "__main__":
    bulls_and_cows()
