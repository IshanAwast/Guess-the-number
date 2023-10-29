import random
import messages


def random_event():
    chance = random.randint(1, 6)
    if chance == random.randint(1, 6):
        print("You have encountered an event!")
        choice = input("Would you like to join? Y/N  >>>").lower()
        if choice == "y":
            print("Insane difficulty guess the number!")
            print("You have to guess the number from 1 to 250")
            tries = 5
            guess = 0
            number = random.randint(1, 250)
            while tries != 0:
                try:
                    guess = int(input("Guess the number  >>>"))
                except ValueError:
                    print("Invalid value type, You have to type a number its common sense! ")

                if guess == number:
                    print("You have guessed the number!")
                    messages.message(tries)
                    break

                tries = tries - 1
                if tries != 0:
                    print(f"You have {tries} tries left")
                    if guess > number:
                        print("Try going lower")
                    else:
                        print("Try going higher")

            if tries == 0:
                print("You failed to guess the number")
                print(f"The number was {number}")
                pass
        elif choice == "n":
            print("You chose not to enter the event...")
            pass
        else:
            print("You couldn't type a single letter properly, you were disqualified... ")
            pass

