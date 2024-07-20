import random
plr1 = random.randrange(3)
plr2 = random.randrange(3)
if plr1 == 0:
    print("Player 1 draws scissors")
elif plr1 == 1:
    print("Player 1 draws paper")
elif plr1 == 2:
    print("Player 1 draws rock")

if plr2 == 0:
    print("Player 2 draws scissors")
elif plr2 == 1:
    print("Player 2 draws paper")
elif plr2 == 2:
    print("Player 2 draws rock")

if plr1 == plr2:
    print("It's a draw")

if plr1 == 0:
    if plr2 == 1:
        print("Player 1 Wins")
    elif plr2 == 2:
        print("Player 2 Wins")

if plr1 == 1:
    if plr2 == 2:
        print("Player 1 Wins")
    elif plr2 == 0:
        print("Player 2 Wins")

if plr1 == 2:
    if plr2 == 0:
        print("Player 1 Wins")
    elif plr2 == 1:
        print("Player 2 Wins")