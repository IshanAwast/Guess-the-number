import random


def ran_number(difc):

    if difc == "easy":
        print("You have to guess the number from 1 to 35")
        number = random.randint(1, 35)
        return number
    elif difc == "medium":
        print("You have to guess the number from 1 to 70")
        number = random.randint(1, 70)
        return number
    elif difc == "hard":
        print("You have to guess the number from 1 to 100")
        number = random.randint(1, 100)
        return number
    else:
        print("Invalid input ")
        print("Please restart")
        exit()
