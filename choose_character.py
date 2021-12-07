import random
import time
def choose(player):
    """
        Allows the player to choose their character 
    or assign a character to the computer bot.

    Args: 
        time.sleep(.9): paues execution for .9 seconds
        player: user (1 player) or computer bot (2 player)
        x : the int being inputted by the user when picking character
    
    Returns:
            int(x): the selected or randomized name of character
    """
    
    if player != "computer":
        x = input(f"\n{player}, please choose a character:\n(1) Volcamore     (2) Falconstein\n(3) Gasmosphere   (4) Atomic Tic\n----->")
    
    else:
        x = random.randrange(1,5)
    
    x = int(x)
    x = int(x)
    
    if x == 1:
        print(f"{player}, you are Volcamore!")
    
    elif x == 2:
        print(f"{player}, you are Falconstein!")
    
    elif x == 3:
        print(f"{player}, you are Gasmosphere!")
    
    elif x == 4:
        print(f"{player}, you are Atomic Tic!")
    
    time.sleep(.9)
    return int(x)