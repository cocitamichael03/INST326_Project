import random
import time
"hi "
def choose_character(player):
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

#-----------------------------------------Character function---------------------------------

def character(chr_numb):
    if chr_numb == 1: #Volcamore
        return f"Please choose attack: \n(1) Ash storm      (2) Rock smash\n(3) Volcanic blaze (4) +15 special.\n-----> "
    
    if chr_numb == 2: #Falconstein 
        return f"Please choose attack: \n(1) Birdseye       (2) Big punch \n(3) Volcanic blaze (4) +15 special.\n-----> "
    if chr_numb == 3: #Gasmosphere
        return f"Please choose attack: \n(1) Gas mist       (2) Fiery breeze\n(3) Forest fire  (4) +15 special.    (5) Exit\n-----> "
    if chr_numb == 4: #Atomic Tic
        return f"Please choose attack: \n(1) Explode        (2) Radiactice wave\n(3) Atomic bomb (4) +15 special.\n-----> "


#-----------------------------------------Power Up Class---------------------------------
class PowerUp:
    def __init__(self):
        return self.powerup
    
    def power_up(self):
        self.powerup = 0
        if self.powerup == 0:
            return 2

#-----------------------------------------Player Class------------------------------------
class Player(PowerUp):
    def __init__(self, name, chr_numb):
        self.name = name
        self.health = 100# <-----------------------------health
        self.times_2_attack = 0
        self.attack = 20  # <-----------------------------attack
        self.blocks = 0
        self.special = 0
        self.power_up_level = 0
        self.chr_numb = chr_numb
        self.super_hit = 0

# Player Stats -----------------------------------------------------------
    
    def get_name(self):
        return self.name
    
    def get_health(self):
        return self.health
    
    def get_blocks(self):
        return self.blocks
    
    def block(self):
        self.blocks += 1
    
# Actions ------------------------------------------------------------------
    def change_health(self, number):
        self.health -= number
    
    def change_attack(self):
        self.attack += 1#find a power up
    
    def on_defense(self, number):
        
        """This is the method for the player on defense for the round. It allows
        the playet to potentially block the """
        ran = random.randrange(0,5)
        if number == None:
            print(f"{self.name}, opponent did not strike.")
            time.sleep(1)
        else:
            if ran == 1:
                print(self.name, "blocked your attack!")
                time.sleep(1)
                self.block()
            else:
                print(self.name, f"-{number} health")
                time.sleep(1)
                self.change_health(number)
    
    def add_super2(self, times_2 = False):
        if times_2 == True:
            self.special += 10
        if times_2 == False:
            self.special += 5
            if self.special >= 50:
                self.special = 0
                self.super_hit +=1

    ''' def add_super(self):
        
        if self.attack == 50:
            self.attack = 5
            self.special = 0
        self.special += 5
        
        if self.special == 50:
            self.attack = 50
            self.special = 0'''

    def attack_opponent2(self, number):
        reg_options = [1,2,3,4]
        print(f"{self.name}'s turn.")
        time.sleep(.25)
        
        
        #functions for characters
        a = number
        a = int(a)
        while True:
            if int(a) in reg_options:
                break
            if int(a) == 5:
                if self.super_hit == 0:
                    a = input(f"You do not have any super hits!\n{character(self.chr_numb)}")
                    
                elif self.super_hit > 0:
                    break
            else:
                a = input(f"That input is invalid.\n{character(self.chr_numb)}")
        a = int(a)
        opp_def = random.randrange(1,3)
        self.power_up_level += 5
        self.add_super2()
        if a == 1:
            opp_def = 1
            if a == opp_def:
                print("Computer attacked you!") #############################################
                time.sleep(.5)
                return self.attack
        elif a == 2:
            opp_def = random.randrange(1,3)
            if a == opp_def:
                print("Computer attacked you!") #############################################
                time.sleep(.5)
                return self.attack + 10
            else:
                print(f"{self.name} missed!")
                time.sleep(.5)
                return 0
        elif a == 3:
            opp_def = random.randrange(1,4)
            if a == opp_def:
                print("Computer attacked you!") #############################################
                time.sleep(.5)
                return self.attack + 20
            else:
                print(f"{self.name} missed!")
                time.sleep(.5)
                return 0
        elif a == 5:
            self.super_hit -= 1
            return 60
        else:
            self.add_super2(True)
            return None
                
    def attack_opponent(self):
        reg_options = [1,2,3,4]
        #greet -------------------------------------------
        greeting = random.randrange(1,3)
        if greeting == 1:
            greeting = "you're up!"
        elif greeting == 2:
            greeting = "Let's go!"
        else:
            greeting = "you got this!"
        #greet -------------------------------------------
        #Player's turn
        #1
        #print(f"\n{self.name}, {greeting}\nStats - Attack: {self.attack}, Special: {self.special}, Health: {self.health}, Super hits: {self.super_hit}")
        
        player_ = [f"\n{self.name}, {greeting}\nStats - Attack: {self.attack}, Special: {self.special}, Health: {self.health}, Super hits: {self.super_hit}"]
        for each in player_:
            lines = each.split("\n")
            for each in lines:
                print(each)
                time.sleep(.75)
        
        #functions for characters
        a = input(character(self.chr_numb))
        a = int(a)
        while True:  #-----------------------Pick an attack (6) will be exit
            if int(a) in reg_options:
                break
            if int(a) == 5:
                if self.super_hit == 0:
                    a = input(f"You do not have any super hits!\n{character(self.chr_numb)}")
                    
                elif self.super_hit > 0:
                    break
            else:
                a = input(f"That input is invalid.\n{character(self.chr_numb)}")
        a = int(a)
        opp_def = random.randrange(1,3)
        self.power_up_level += 5
        self.add_super2()
        if a == 1:
            opp_def = 1
            if a == opp_def:
                return self.attack
        elif a == 2:
            opp_def = random.randrange(1,3)
            if a == opp_def:
                return self.attack + 10
            else:
                print(f"{self.name}, you missed!")
                return 0
        elif a == 3:
            opp_def = random.randrange(1,4)
            if a == opp_def:
                return self.attack + 20
            else:
                print(f"{self.name}, you missed!")
                return 0
        elif a == 5:
            self.super_hit -= 1
            return 60
        else:
            self.add_super2(True)
            return None 

#Declare winner and loser ---------------------------------------------

    def loss(self):
        return f"{self.name}, you lose."
    
    def winner(self):
        return f"------{self.name}, you win!------"

def play_game():
    number_of_players = input("Choose (1) 1 player or (2) 2 players: ")
    number_of_players = int(number_of_players)
    rounds = 0
    var = True

    if number_of_players == 1:
        player1 = input("Player 1, enter your screen name: ")
        player2 = "computer"
        player1_chr = choose_character(player1)
        players = [Player(player1, player1_chr), Player(player2, choose_character("computer"))]

    if number_of_players == 2:
        player1 = input("Player 1, enter your screen name: ")
        player2 = input("Player 2, enter your screen name: ")
        player1_chr = choose_character(player1)
        player2_chr = choose_character(player2)
        players = [Player(player1, player1_chr), Player(player2, player2_chr)]

    count = 0
    while True:
        if var == False:
            leaderboard = open("leaderboard.txt", "a")
            leaderboard.write(f"{player1}\n")
            leaderboard.close()
            break
        
        if number_of_players == 1:
            rounds += 1
            opponent = players[1]
            if count == 0:
                players[0].on_defense(players[1].attack_opponent2(random.randrange(1,5)))
                count += 1
                print(count, "Player 1")
            if count == 1:
                count = 0
                players[1].on_defense(players[0].attack_opponent())
                print(count, "Player 2")
        
        
            for each in players:
                if each.get_health() < 1:
                        print("\n------------STATS------------")
                        for player in players:
                            print(f"{player.get_name()} - Health: {player.get_health()}, Blocks: {player.get_blocks()}")
                        print(players[(players.index(each)+1)%2].winner())
                        print(f"      Total rounds: {rounds}")
                        var = False
                        break
        if number_of_players == 2:
            for each in players:
                rounds += 1
                opponent = players[(players.index(each)+1)%2]
                each.on_defense(opponent.attack_opponent())

                if each.get_health() < 1:
                    print("\n------------STATS------------")
                    for player in players:
                        print(f"{player.get_name()} - Health: {player.get_health()}, Blocks: {player.get_blocks()}")
                    print(players[(players.index(each)+1)%2].winner())
                    print(f"      Total rounds: {rounds}")
                    var = False
                    break
                
            
if __name__ == "__main__":
    play_game()