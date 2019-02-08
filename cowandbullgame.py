import random

def startgame():
    cows=0
    bulls=0
    secret=str(random.randint(1000,9999))
    print(secret)
    guess="0"
    counter=0
    while(not(guess==secret)):
        guess=input("Enter your number:")
        if int(guess)>9999 or int(guess)<1000:
            print("Out of range guess.Enter 4 digit number.Try again")
            continue
        if guess=="quit":
            print("You quited after"+str(counter)+"correct attempt.")
            break
        counter+=1
        cows=0
        bulls=0
        for i in range(0,4):
            if guess[i]==secret[i]:
                cows+=1
            else:
                bulls+=1
        print("Cows:"+ str(cows)+"Bulls:"+str(bulls))
    else:
        print("Your guess is correct. You did it in"+str(counter)+"attempt.")


if __name__=="__main__":
    startgame()