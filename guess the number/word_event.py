import time
import random
import threading
timer = 0
timer2 = 0


def countdown():
    global timer
    global timer2
    timer2 = timer
    for x in range(timer2):
        timer = timer - 1
        time.sleep(1)

    print('''
Time up!''')


countdown_thread = threading.Thread(target=countdown)


def word_test(occur):
    words = ["pye", "lose", "win", "event", "...hi...", "difficult", "guess", "try", "nerd", "amazing", "project",
             "insane", "ah...", "unwanted", "stone", "nose", "rock", "computer", "unexpected", "python", "scarf"]
    chance = random.randint(1, 8)
    chance2 = random.randint(1, 8)
    choice = "none"
    word = "none"
    entry = "none"
    score = 0
    if occur == "game" or "custom":
        chance = chance2
    if chance == chance2:
        if occur == "event":
            print("You have encountered an event!")
            choice = input("Would you like to join? Y/N  >>>").lower()
        elif occur == "game" or "custom":
            choice = input("Do you want to start the word test? Y/N >>>").lower()
        if choice == "y":
            print('''Word test!
You have to type the given words to gain 10 (by default) score points 
under 30 seconds (by default) to win, else you lose.
Word test will start in-''')
            limit = 0
            if occur == "custom":
                global timer
            timer = 0
            if occur == "game" or "event":
                timer = 30
                limit = 10
            if occur == "custom":
                timer = int(input("Enter your time in seconds: "))
                limit = int(input("Enter score required to win: "))

            time.sleep(2)
            for i in range(3):
                time.sleep(1)
                print(i)
            countdown_thread.start()
            while True:
                print(f"score: {score}")
                if word != entry:
                    print("You entered incorrect word, you lost...")
                    break

                if score == limit:
                    print("You won! Amazing speed!")
                    exit()

                word = random.choice(words)
                print(f"Word- {word}")
                entry = input(">>>")
                if word == entry:
                    score = score + 1

                if timer == 0:
                    if score != 10:
                        print("You are out of time, you lost...")
                    break

        elif choice == "n":
            print("You chose not to join...")
        else:
            print("You couldn't type a single letter correctly, you were disqualified...")
