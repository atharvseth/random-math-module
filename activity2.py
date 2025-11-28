import random

while True : 
    user_action = input(" enter a choice ( rock ,paper, scissors):")

    possible_actions  = ["rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\n you chose {user_action}, computer chose {computer_action}\n")

    if user_action == computer_action:
        print(f"both players selected{user_action} its a tie!!!")
    elif user_action == "rock":
        if computer_action =="scissors":
            print("rocks smashes scissors !!! yopu win!!")
        else:
            print("paper cover rock!! , you loose!!")
    elif user_action == "paper":
        if computer_action =="rock":
            print("paper covers rock !!! yopu win!!")
        else:
            print("scissor cut paper!! , you loose!!")
    elif user_action == "scissors":
        if computer_action =="paper":
            print("scissors  cut paper !!! yopu win!!")
        else:
            print("rock smashes scissor !! , you loose!!")
    play_again = input("play again ?(y/n)")
    if play_again != "y":
        break
