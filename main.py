import random


def guess_the_number(guess):
    number = random.randint(1, 10)
    if guess == number:
        return "You guessed it!"
    else:
        return f"Sorry, the number was {number}"


if __name__ == "__main__":
    user_guess = int(input("Guess a number between 1 and 10: "))
    print(guess_the_number(user_guess))
