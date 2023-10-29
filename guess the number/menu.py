import Guessing
import luck_test
import word_event
import reverse

print('''===========================================================================================================================================================================
Welcome!
I am pye, and I will respond to your commands.
Use the "help" command for more information.''')
command = " "
while True:
    command = input(">>>").lower()
    if command == "help":
        print('''===================================================================================================
Play- To start the number guessing game
Play reverse- To start reverse number guessing game
Play luck- To start luck test
Play word- To start word test
Word custom- To start customized word test
Game info- To get more details on the number guessing game and the reverse as well as luck test.
Quit- To leave the game
Interact info- To get details on the questions that Pye will respond to.
====================================================================================================================''')

    elif command == "game info":
        print('''Number guessing game-
You will get 5 tries to score victory!
You can choose the difficulty as you wish but do not give incorrect inputs.
You may also encounter events, and get chance to get more tries in a game!

Reverse number guessing game-
You set a number and the pye tries to gues the number you set!
You can choose the difficulty as you wish but do not give incorrect inputs.
You may also encounter events, and get chance to get cut off tries in a game!

Luck test-
You spin a wheel to test your luck!

Word test-
Test your typing speed!
You need to get 10 score points under 25 seconds to win else you lose!

Word test customized- You can set your own win score and time limit
====================================================================================================================''')

    elif command == "interact info":
        print('''These are the questions you can ask pye-
Hello
How are you
Who are you
I am fine too
I am not fine
Tell me some tricks
What events can occur
How do you get more tries
How do you pronounce your name
What does your name mean
What are the chances of events
...''')
    elif command == "hello":
        print("Hello there!")
    elif command == "how are you":
        print("I am fine, what about you?")
    elif command == "who are you":
        print("I am pye ofcourse, I already introduced at the beginning!")
    elif command == "i am fine too":
        print("Good to hear!")
    elif command == "i am not fine":
        print("ah... I hope you have a happy day")
    elif command == "tell me some tricks":
        print("Keep taking halves, in this way you narrow your options quickly!")
    elif command == "what events can occur":
        print("For now you can encounter insane difficulty guess the number and word test")
    elif command == "how do you get more tries":
        print("With a chance of 1 out of 4, you may encounter a test of luck, if you win you get one more try!")
    elif command == "how do you pronounce your name":
        print("It is pronounced 'pie'")
    elif command == "what does your name mean":
        print("It is simply extension of a python file 'py' with 'e'")
    elif command == "what are the chances of events":
        print('''Luck test- 1/4
Insane difficulty guess the number- 1/6
Word test- 1/8''')

    elif command == "play" or "quit" or "play reverse" or "play luck" or "play word" or "word custom":
        break

if command == "play":
    Guessing.main_program()
elif command == "play reverse":
    reverse.reverse()
elif command == "play luck":
    luck_test.luck_event("game")
elif command == "play word":
    word_event.word_test("game")
elif command == "word custom":
    word_event.word_test("custom")
elif command == "quit":
    print("You left the game...")
    exit()
else:
    print("Invalid command, please check the command list")
