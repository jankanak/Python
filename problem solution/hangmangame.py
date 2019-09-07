import time
name=input("What is your name?")
print("hello"+name,"Time to play hangman")
time.sleep(1)
print("Start guessing")
time.sleep(0.5)
word="secret"
guesses=""
turns=10
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed+=1
    if failed==0:
        print("you win")
        break
    
    guess=input("guess  a charectar?")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("wrong")
        print("you have",+turns,"more guesses")
        if turns==0:
            print("you loose")
    
