
import random

def computer():
    x = ["r", "p", "s"]
    return random.choice(x)

def rule(player, computer):
    if player == computer:
        return [0,0]
    elif (player == "r") and (computer == "s"):
        return [1,0]
    elif (player == "r") and (computer == "p"):
        return [0,1]
    elif (player == "p") and (computer == "r"):
        return [1,0]
    elif (player == "p") and (computer == "s"):
        return [0,1]
    elif (player == "s") and (computer == "r"):
        return [0,1]
    elif (player == "s") and (computer == "p"):
        return [1,0]
def scoreCard(pScore, cScore):
    if pScore == cScore:
        print("It's a Tie !")
    elif pScore > cScore:
        print("Congrats, You won !")
    elif pScore < cScore:
        print("Better luck next time !")

while True :
    print('\n'*2)
    player_score, computer_score = 0, 0
    num_of_rounds = input("Number of rounds ('q' to quit): ")
    print("-"*35+"|")
    if num_of_rounds == "q":
        break
    for i in range(int(num_of_rounds)):
        player = input("\nYour Turn : \nRock[r]\nPaper[p]\nScissor[s]\nYOU => ").casefold()
        com = computer()
        print("COM => ", com)
        print()
        print("-"*35+"|")
        score = rule(player.strip()[0], com)
        player_score += score[0]
        computer_score += score[1]
    print("-"*35+"|")
    print(f"Your score : {player_score}\nComputer score : {computer_score}")
    scoreCard(player_score, computer_score)
    print("-"*35+"+")
    

    
