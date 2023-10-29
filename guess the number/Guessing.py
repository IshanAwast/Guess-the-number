import randomizers
import messages
import random_event
import luck_test
import word_event


def main_program():
    print('''==================================================================================================================================================================================
Pye-
Guess the number to win!
You will get 5 tries in total, if you can guess the number I chose in these limited tries, you win else you lose.
First of all, please choose the difficulty.
Easy- guess from 1 to 35
Medium- guess from 1 to 70
Hard- guess from 1 to 100''')
    difc = input(">>>")
    tries = 5
    guess = 0
    number = randomizers.ran_number(difc.lower())
    while True:
        try:
            if tries > 0:
                guess = int(input("Guess the number  >>>"))
        except ValueError:
            print("Invalid value type, You have to type a number its common sense! ")
        if guess == number:
            print("You have guessed the number!")
            messages.message(tries)
            break
        if tries == 0:
            test = luck_test.luck_event("event")
            if test == "pass":
                tries = tries + 2
            else:
                print("You failed to guess the number")
                print(f"The number was {number}")
                break

        tries = tries-1
        if tries != 0:
            print(f"You have {tries} tries left")
            if guess > number:
                print("Try going lower")
            else:
                print("Try going higher")

    random_event.random_event()
    word_event.word_test("event")

    restart = input('Would you like to try again?  Y/N >>>').lower()
    if restart == "y":
        main_program()
    elif restart == "n":
        print("You left the game...")
        exit()
