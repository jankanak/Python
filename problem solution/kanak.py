import time
global apples
global gold
apples=0
gold=0
def start():
    print("hello and welcome!")
    name=input("what is your name :")
    print("welcome ,"+name+" !")
    print("the object of this game  is to collect apple")
    print("after collecting the apple sell them")
    choice=input("do you want to play Y/N?")
    if choice=="Y":
        begin()
    if choice=="N":
        print("just go to hell")
def begin():
    global apples
    global gold
    if gold>30:
        print("you won the game")
        play=input("do you want to play again Y /N !")
        if play=="Y":
            print("again start the game")
        if play=="N":
            print ("happy ending")
        
    print ("let us started the game")
    pick=input("do you want to pick  an apple?Y/N!")
    if pick=="Y":
        time.sleep(1)
        print("you pick an apple")
        apples=apples+1
        print("you currently have: ",apples,"apples")
        begin()
    if pick=="N":
        sell=input("Do you want to  sell apples?Y/N")
        if sell=="Y":
                   print("you currently have: ",apples,"apples")
                   print("you have sold your apples")
                   gold=apples*10
                   apples=0
                   print("your gold is now",gold)
                   begin()
                   
        
     
start()

