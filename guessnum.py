import random
secret=random.randint(1,9)

while True:

    times=1
    while True:
        guess=int(input("Enter your guess 1-9"))
        if guess>secret:
            print(" Your guess is higher")
        elif guess<secret:
            print("Your guess is lower")
        else:
            print("Your guess is correct and you guessed it in {} times".format(times))
            break
        times+=1
    quit=input("Type exit if you want to quit")
    if quit=="exit":
        break