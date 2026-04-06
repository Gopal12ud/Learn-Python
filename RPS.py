import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']

    while True:
        user = input("\nChoose rock, paper or scissors (or 'quit'): ").lower()
        if user == 'quit':
            break


        computer = random.choice(choices)
        print(f"computer chose: {computer}")

        if user == computer:
            print("It's a tie!")
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'paper' and computer == 'rock') or \
             (user == 'scissors' and computer == 'paper'):
            print("You win!")
        else:
           print("computer wins!")

rock_paper_scissors()        