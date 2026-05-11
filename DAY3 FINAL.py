direction=input("enter your direction 'Right' or 'Left':")
if direction=="right":
    action=input("swim or wait:")
    if action=="wait":
        door=input("which door would u select red blue or green:")
        if door=="blue":
            print("Congratulation You won the game")
        else:
            print("GAME OVER")
    else:
        print("GAME OVER")
else:
    print("Game Over")
