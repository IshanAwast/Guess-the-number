import random
import time
import luck_test
import word_event


def reverse():
    try_messages = ["Let's try", "How about", "This one for sure", "This is it", "I am winning this", "This is easy"]
    print('''==========================================================================================================
Pye- Reverse guessing!
You choose the number while I try to guess it!
Very Easy- You can choose a number from 1 to 150 and I have only 10 tries
Easy- You can choose from 1 to 150 and I have 15 tries
Medium- You can choose from 1 to 100 and I have 12 tries
Hard- You can choose from 1 to 50 and I have 16 tries''')
    difc = input(">>>").lower()
    number = int(input("Enter your hidden number >>>"))
    if difc == "easy":
        tries = 15
        limit = 150
        if 0 < number < 151:
            pass
        else:
            print("Pye- Hey! Don't try to fool me!")
            exit()
    elif difc == "medium":
        tries = 12
        limit = 100
        if 0 < number < 100:
            pass
        else:
            print("Pye- Hey! Don't try to fool me!")
            exit()
    elif difc == "very easy":
        tries = 10
        limit = 150
        if 0 < number < 151:
            pass
        else:
            print("Pye- Hey! Don't try to fool me!")
            exit()
    elif difc == "hard":
        tries = 16
        limit = 50
        if 0 < number < 51:
            pass
        else:
            print("Pye- Hey! Don't try to fool me!")
            exit()
    else:
        print("Type correctly will you!!!")
        exit()
    test = luck_test.luck_event("event")
    if test == "pass":
        print("Pye lost 2 tries!")
        tries = tries - 2
    elif test == "fail":
        print("Nothing happened, the match continues...")

    time.sleep(2)
    print(f"Hidden number: {number}")

    while True:
        tm = random.choice(try_messages)
        if tries == 0:
            print("Pye- Ah, I lost, you win...")
            break
        tries = tries - 1
        guess = random.randint(1, limit)
        time.sleep(1)
        print(f"{tm}: {guess}                                      tries left: {tries}")
        print(" ")
        if guess == number:
            print("Pye- Hahaha! I Won!")
            break

    word_event.word_test("event")

    restart = input('Would you like to try again?  Y/N  >>>').lower()
    if restart == "y":
        reverse()
    elif restart == "n":
        print("You left the game...")
        exit()
