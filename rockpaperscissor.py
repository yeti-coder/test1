__author__="sam"
#rock paper scissor game
# player1=""
# player2=""
# player1_input=""
# player2_input=""

rps=["rock","scissor","paper"]

player1=input("Enter player1 name")
player2=input("Enter player2 name")

while True:
    while True:
        player1_input=(input(player1+"! Rock, Paper or Scissor?"))
        player1_input=player1_input.lower()
        if player1_input in ["rock","scissor","paper"]:
            break
        else:
            print("Invalid entry")

    while True:
        player2_input=(input(player2+"! Rock, Paper or Scissor?"))
        player2_input=player2_input.lower()
        if player2_input in ["rock","scissor","paper"]:
            break
        else:
            print("Invalid entry")

    if player1_input==player2_input:
        print("game draw")
    elif (player1_input=="rock" and player2_input=="scissor") or (player1_input=="scissor" and player2_input=="paper") or (player1_input=="paper" and player2_input=="rock"):
        print(player1+"is winner")
    else:
        print(player2+"is winner")
    play_again=input("Do you want to play again? [yes/no]")
    if play_again=="no":
        break




