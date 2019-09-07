import random
number=random.randint(1,99)
guesses=0
while(guesses<5):
    guess=int(input("enter a number between 1 to 99 "))
    guesses=guesses+1
    print("This is your %d guess "%guesses)
    if(guess<number):
        print("guess is low")
    elif(guess>number):
        print("guess is high")
    elif(guess==number):
        break
if (guess==number):
    guesses=str(guesses)
    print("your guess it in:",guesses+"guesses")
if(guess!=number):
    guesses=str(guesses)
    print("the secret number is",number)
        
