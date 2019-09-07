import time
name=input("Hey What is your name?")
print("My name is "+name)
time.sleep(1)
print("start guessing")
time.sleep(0.5)
word="kanak"
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

    guess=input("guess a charectar?")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("wrong")
        print("you have",+turns,"more turns avaialable")
    if turns==0:
        print("you are a looser")
        
