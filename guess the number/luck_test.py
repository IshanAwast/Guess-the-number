import random
import time


def luck_event(occur):
    chance = random.randint(1, 4)
    choice = "none"
    chance2 = random.randint(1, 4)
    if occur == "game":
        chance = chance2
    if chance == chance2:
        if occur == "event":
            print("You have been granted a chance to receive an extra try or cut off 2 tries of pye!")
            choice = input("Would you like to try? Y/N >>>").lower()
        elif occur == "game":
            choice = input("Do you want to start the luck test? Y/N >>>").lower()
        if choice == "y":
            if occur == "event":
                print("You will spin a wheel, if you hit the jackpot, you will be granted your wish!")
            elif occur == "game":
                print("You will spin a wheel, if you hit the jackpot, you win!")
            command = input("Enter spin to start >>>").lower()
            if command == "spin":
                number = random.randint(1, 20)
                times = 5
                print(f"JACKPOT: {number}")
                while True:
                    if times == 0:
                        print("You are not very lucky, you lost...")
                        test = "fail"
                        if occur == "event":
                            return test
                        break
                    times = times - 1
                    spin = random.randint(1, 20)
                    time.sleep(1)
                    print(spin)
                    if spin == number:
                        print("How lucky! You Won!")
                        test = "pass"
                        if occur == "event":
                            return test
                        break

            else:
                print("What a shame... , You couldn't even type a word correctly")
                test = "fail"
                if occur == "event":
                    return test
                exit()
        elif choice == "n":
            print("You didn't want to give it a try...")
            test = "fail"
            if occur == "event":
                return test
            exit()
        else:
            print("What a shame... , You couldn't even type a single letter correctly")
            test = "fail"
            if occur == "event":
                return test
            exit()

    if occur == "game":
        restart = input('Would you like to try again?  Y/N  >>>').lower()
        if restart == "y":
            luck_event("game")
        elif restart == "n":
            print("You left the game...")
            exit()
