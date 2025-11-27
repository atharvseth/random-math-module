import random # importing module
playing = True # initialise
number = str(random.randint(1,15)) #random in-built funtion 

print("i will generate a number from 1 to 14, and you have guess the number one digit at a time !!!!!")
print("the game ends when you get 1 hero!!!!")
while playing:
    guess = input("give me your best guess ! ! ")
    if number == guess:
        print("you win the game!!!!!!!!!")
        print("the number was",number)
        break

    else:
        print("your guess isn't quite write , try again.")
