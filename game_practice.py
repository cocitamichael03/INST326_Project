import random
def choose_character(self):
    numb = random.randrange(1,5)
    if numb == 1:
        character = ""

class PowerUp:
    def __init__(self):
        return self.powerup
    
    def power_up(self):
        self.powerup = 0
        if self.powerup == 0:
            return 2

class Player(PowerUp):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.times_2_attack = 0
        self.attack = 5
        self.blocks = 0
        self.special = 0
        self.power_up_level = 0

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
        ran = random.randrange(0,2)
        
        if ran == 1:
            #print(self.name, "Blocked!")
            self.block()
        else:
            self.change_health(number)
    
    def add_super(self):
        
        if self.attack == 25:
            self.attack = 5
            self.special = 0
        self.special += 5
        
        if self.special == 50:
            self.attack = 25
            self.special = 0

    def attack_opponent(self, powerup = False):
        self.power_up_level += 5
        if self.power_up_level == 50:
            self.power_up()
        self.add_super()
        print(self.attack, self.special)
        return self.attack
    
#Declare winner and loser ---------------------------------------------

    def loss(self):
        return f"{self.name}, you lose."
    
    def winner(self):
        return f"{self.name}, you win!"

def play_game():
    rounds = 0
    players = [Player("Player1"), Player("Player2")]
    
    var = True
    
    while True:
        
        for each in players:
            rounds += 1
            opponent = players[(players.index(each)+1)%2]
            each.on_defense(opponent.attack_opponent())

            if each.get_health() < 1:
                
                for player in players:
                    print(f"Name: {player.get_name()}, Health: {player.get_health()}, Blocks: {player.get_blocks()}")
                print(each.loss())
                print(f"Total rounds: {rounds}")
                var = False
                break
            
        if var == False:
            break
    
if __name__ == "__main__":
    play_game()
