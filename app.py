
import random
import os

play_again = "Y"
roundsplayed = 0
roundswon = 0
roundslost = 0
roundstied = 0

while play_again.upper() == "Y":

    os.system('clear' if os.name == 'posix' else 'cls')

    print("Hello, world! Time to play some Rochambeau!")
    print("In this game, you will have 3 choices: Rock, Paper or Scissors.")
    print("Rock breaks Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")


    user_choice = "X"
    goodreactions = ["Mad Skills!", "You're Good At This!", "You Chose Wisely!", "Superb!", "Wow!"]
    goodreaction = random.choice(goodreactions)
    badreactions = ["Yikes !", "You were so close!", "You'll Win Next Time!", "Ouch!", "You Chose Poorly!"]
    badreaction = random.choice(badreactions)
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    while user_choice.upper() not in ["ROCK", "PAPER", "SCISSORS"]:
        user_choice = input("Please enter your choice out of these 3 options: Rock, Paper, Scissors, then click Enter : ")
        if user_choice.upper() not in ["ROCK", "PAPER", "SCISSORS"]:
            print("Sorry, Invalid Choice...")

    print(f"Computer chooses: {computer_choice}")

    # Determine the winner
    if user_choice.upper() == computer_choice.upper():
        print(user_choice.upper() + " == " + computer_choice.upper() + " ... It's a tie!")
        roundstied += 1
    elif (user_choice.upper()[0] == "R" and computer_choice == "Scissors"):
        print("Rock breaks Scissors! You win! " + goodreaction)
        roundswon += 1
    elif (user_choice.upper()[0] == "P" and computer_choice == "Rock"):
        print("Paper covers Rock! You win! " + goodreaction)
        roundswon += 1
    elif (user_choice.upper()[0] == "S" and computer_choice == "Paper"):
        print("Scissors cuts Paper! You win! " + goodreaction)
        roundswon += 1
    elif (user_choice.upper()[0] == "S" and computer_choice == "Rock"):
        print("Scissors is broken by Rock! Computer wins! " + badreaction)
        roundslost += 1
    elif (user_choice.upper()[0] == "R" and computer_choice == "Paper"):
        print("Rock is covered by Paper! Computer wins! " + badreaction)
        roundslost += 1
    elif (user_choice.upper()[0] == "P" and computer_choice == "Scissors"):
        print("Paper is cut by Scissors! Computer wins! " + badreaction)
        roundslost += 1

    roundsplayed += 1

    play_again = input("If you want to play this awesome game again, click Y then click Enter...  If you are done, click anything but Y then click Enter: ")
    if play_again.upper() == "Y":
        # Rest of the code to play the game again
        pass
    else:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("NICE JOB!")
        print("You played " + str(roundsplayed) + " round(s).")
        if (roundswon > 0):
            print("You won " + str(roundswon) + " time(s).")
        if (roundslost > 0):
            print("You lost " + str(roundslost) + " time(s).")
        if (roundstied > 0):
            print(str(roundstied) + " round(s) ended in a tie.")        
        print("THANK YOU FOR PLAYING!")