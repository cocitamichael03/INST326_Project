import random
import time

def choose_character(player):
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

#-----------------------------------------Character function---------------------------------

def character(chr_numb):
    """
        Allows user to choose the kind of
    attack fortheir selected character. 
    
    Args: 
         chr_numb: Accepts int one through six. 

    Returns:
         chr_numb == 1 : The attack options for Volcamore and an exit option.
         chr_numb == 2 : The attack options for Falconstein and an exit option. 
         chr_numb == 3 : The attack options for Gasmosphere and an exit option. 
         chr_numb == 4 : The attack options for Atomic Tin and an exit option. 
    """
    
    if chr_numb == 1: #Volcamore
        return f"Please choose attack: \n(1) Ash storm      (2) Rock smash\n(3) Volcanic blaze (4) +15 special.\nChoose (6) to exit.\n-----> "
    
    if chr_numb == 2: #Falconstein 
        return f"Please choose attack: \n(1) Birdseye       (2) Big punch \n(3) Volcanic blaze (4) +15 special.\nChoose (6) to exit.\n-----> "
    if chr_numb == 3: #Gasmosphere
        return f"Please choose attack: \n(1) Gas mist       (2) Fiery breeze\n(3) Forest fire  (4) +15 special.\nChoose (6) to exit.\n-----> "
    if chr_numb == 4: #Atomic Tic
        return f"Please choose attack: \n(1) Explode        (2) Radiactice wave\n(3) Atomic bomb (4) +15 special.\nChoose (6) to exit.\n-----> "


#-----------------------------------------Power Up Class---------------------------------
class PowerUp:
    """
    
    

    
    """
    def __init__(self):
        """
        
        
        """
        return self.powerup
    
    def power_up(self):
        """
            Sets the initial value of powerup to 0 and
        changes it to 2 if users wants to use powerup
        
        
        Returns:
                
        """
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
        """Returns the name of the player as a string value."""
        return self.name
    
    def get_health(self):
        """Returns the health of the player as a string value."""
        return self.health
    
    def get_blocks(self):
        """Returns the number of blocks as a string value for the player."""
        return self.blocks
    
    def block(self):
        """A counter for the number of blocks for a player."""
        self.blocks += 1
    
# Actions ------------------------------------------------------------------
    def exit_game(self):
        """
            If the player chooses to exit the game, the system will bring
        their points to 0 and tell them they forfeit. 
        
        Args:
             self.health: automatically sets health to 0  when called
             
        Returns:
                (self.name) you forfeit!: Tells the user they forfeit the game
        """
        
        self.health = 0
        print(f"{self.name} you forfeit!")
    
    def change_health(self, number):
        """
        This method subtracts the attack of the other player on offense from the health of the current player on defense.
        It then calls on the get_health method.
        """
        self.health -= number
        self.get_health()

    def change_attack(self):
        self.attack += 1 # <------------------------------------- find a power up
    
    def on_defense(self, number):
        """
            Allows the defensive player to potentially block
        the attack of the offensive player depending on the randomly generated integer.
        If the player does not block, the change_health method is called
        and the current player on defense loses health.
        
        Args:
             number:
             ran: assigns a random number 0-5 to be called
             time.sleep(1): delays execution for 1 second
             
        Returns:
                Whether or not the opponent striked.
        """
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
                if number > 0:
                    print(self.name, f" lost -{number} health")
                    time.sleep(1)
                    self.change_health(number)
                else:
                    print(self.name, f"lost {number} health")
                    time.sleep(1)
                    self.change_health(number)
            return "Opponent Striked"
     
    def add_super(self, times_2 = False):
        """
        This method is called during each round for each player and adds 10 to the total special as well as checking to see if the player
        has reached the threshold to gain a special attack. If the obtained amount of special meets the threshold, a special hit is added
        to the players inventory and can be used. The special is then moved back to 0 to be regenerated in further rounds.
        """
        if times_2 == True:
            self.special += 10
        
        if times_2 == False:
            self.special += 5
            if self.special >= 50:
                self.special = 0
                self.super_hit +=1

    def computer_attack(self, number):
        """
        This method is the attack component only for the computer. 
        It has the same functionality as the attack_opponent designed for players to manually input answers minus the input.
        
        Returns:
            Either none, zero (integer), or an integer that is applied towards the opponent on defense's health.
         """
        reg_options = [1,2,3,4]
        print(f"{self.name}'s turn.")
        time.sleep(.25)
        
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
        self.add_super()
        
        if a == 1:
            opp_def = 1
            
            if a == opp_def:
                print("Computer attacked you!") 
                time.sleep(.5)
                return self.crit_chance()
        
        elif a == 2:
            opp_def = random.randrange(1,3)
            
            if a == opp_def:
                print("Computer attacked you!") 
                time.sleep(.5)
                return self.crit_chance() + 10
           
            else:
                print(f"{self.name} missed!")
                time.sleep(.5)
                return 0
       
        elif a == 3:
            opp_def = random.randrange(1,4)
            
            if a == opp_def:
                print("Computer attacked you!") 
                time.sleep(.5)
                return self.crit_chance() + 20
            
            else:
                print(f"{self.name} missed!")
                time.sleep(.5)
                return 0
        
        elif a == 5:
            self.super_hit -= 1
            return 60
        
        else:
            self.add_super(True)
            return None

    def crit_chance(self):
        """This method gives the player on offense a random change of getting a critical hit which is dependent upon
        a randomly generated number. This method is called for both the computer_attack() and player_attack() methods when returning the attack.
        
        Returns:
            self.attack + 50 or self.attack which is an integer value.
        """
        crit_set = random.randrange(0,11)
        if crit_set <= 3:
            print("Critical Hit!")
            return self.attack + 50
        else:
            return self.attack
                
    # Critical hit ------------------------------------------------------------------      
    def attack_opponent(self):
        """
        This method is the attack component for players. It first greets the player on offense, then shows the players stats, 
        and then calls on the corresponding character through the character() function for a list of moves to choose from.
        It then takes the players input for a move and runs it through the corresponding if statement to see whether the hit lands or misses
        depending on the randomly generated number.
        
        Returns:
            Either none, zero (integer), or an integer that is applied towards the opponent on defense's health.
         """
        reg_options = [1,2,3,4,6]
        greeting = random.randrange(1,3)
        
        if greeting == 1:
            greeting = "you're up!"
        
        elif greeting == 2:
            greeting = "Let's go!"
        
        else:
            greeting = "you got this!"
        
        #greet -------------------------------------------

        player_ = [f"\n{self.name}, {greeting}\nStats - Attack: {self.attack}, Special: {self.special}, Health: {self.health}, Super hits: {self.super_hit}"]
        
        for each in player_:
            lines = each.split("\n")
            
            for each in lines:
                print(each)
                time.sleep(.75)
        
        #functions for characters----------------------------------------------- 
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
        self.add_super()
        
        if a == 1:
            opp_def = 1
            if a == opp_def:
                return self.crit_chance()
        
        elif a == 2:
            opp_def = random.randrange(1,3)
            
            if a == opp_def:
                return self.crit_chance() + 10
            
            else:
                print(f"{self.name}, you missed!")
                return 0
        
        elif a == 3:
            opp_def = random.randrange(1,4)
            
            if a == opp_def:
                return self.crit_chance() + 20
            
            else:
                print(f"{self.name}, you missed!")
                return 0
        
        elif a == 5:
            self.super_hit -= 1
            return 60
        
        elif a == 6:
            self.exit_game()
        
        else:
            self.add_super(True)
            return None 

#Declare winner and loser ---------------------------------------------
    def get_winner(self):
        """
            Tells the player that they won the game.
            
        Attribute:
                  name: players name

        Return:
                name, you win!: the players name and that they won. 
        """
        return f"------{self.name}, you win!------"
    
    #Play Game Again------------------------------------------------------
    def play_again(self):
        """
        This method gives the player the option to play again and is called in the play_game() function after a player reaches 0 health.
        If the player chooses to play again, the play_game() function is called and if the player does not want to play again,
        the dont_play() method is called. 
        """
        option = input(" Would you like to play again?").lower()
        while True:
            if option == "yes":
                play_game()
            elif option == "no":
                self.dont_play()
            else:
                option = input(" That is not a valid answer. Try again.").lower()
    
    #Exits the game-----------------            
    def dont_play(self):
        """
           Thanks the user for playing the game and allows them to see the leaderboard if they desire.
        
        Attribute: 
                   check_leaderboard(): calls the function
                   exit(): calls the exit function
        
        Return: 
                string: "Thanks for playing" if chosen to exit game. 
        """

        print("Thanks for playing")
        lb_check = input("Would you like to check the leaderboard? (yes or no) ")
        
        if lb_check == "yes":
            check_leaderboard
        
        exit()

# check leaderboard function ------------------------------------------------------------------
def check_leaderboard():
    """This function opens up the leaderboard."""
    print("Leaderboard: \n")
    with open('leaderboard.txt') as f:
        contents = f.read()
        print(contents)

def play_game():
    """
    This method initiates the game by asking the player if it will be single player or multiplayer. From there it creates instances of the Player class
    according to the input of the amount of players. The appropriate while loop is then executed for game play.
    The health of each player is examined each round to determine if the zero health limit is reached, ending the game if so.
    The game stats are displayed at the end of the game as well as the players stats being added to the leaderboard.
    The play_again method from the Player class is then called to give the player(s) the option to play again.
    """
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
            for each in players:
                if int(player.get_health()) > 0:
                    result = "win"
                else:
                    result = "lose"
            leaderboard.write(f"{player1},{result}\n")
            leaderboard.close()
            break
        
        if number_of_players == 1:
            rounds += 1
            opponent = players[1]

            if count == 0:
                players[0].on_defense(players[1].computer_attack(random.randrange(1,5)))
                count += 1
            
            for each in players:
                if each.get_health() < 1:
                    print("\n------------STATS------------")
                    for player in players:
                        print(f"{player.get_name()} - Health: {player.get_health()}, Blocks: {player.get_blocks()}")
                    print(players[(players.index(each)+1)%2].get_winner())
                    print(f"      Total rounds: {rounds}")
                    var = False
                    break
                    
            
            if count == 1:
                if var == False:
                    break
                else:
                    count = 0
                    players[1].on_defense(players[0].attack_opponent())
        
        
            for each in players:
                if each.get_health() < 1:
                    print("\n------------STATS------------")
                    for player in players:
                        print(f"{player.get_name()} - Health: {player.get_health()}, Blocks: {player.get_blocks()}")
                    print(players[(players.index(each)+1)%2].get_winner())
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
                    print(players[(players.index(each)+1)%2].get_winner())
                    print(f"      Total rounds: {rounds}")
                    var = False
                    break

    players[0].play_again()
                
            
if __name__ == "__main__":
    play_game()