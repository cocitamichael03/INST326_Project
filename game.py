import random

def choose_character(self):
    numb = random.randrange(1,5)
    if numb == 1:
        character = ""



class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.times_2_attack = 0
        self.attack = 5
        self.blocks = 0
        self.special = 0
    
    def get_name(self):
        return self.name
    
    def get_health(self):
        return self.health
    
    def change_defense(self, number):
        self.health -= number
    
    def add_super(self):
        self.special += 5
        if self.special == 50:
            self.special = 0
            self.attack = 25

    def on_defense(self, number):
        ran = random.randrange(0,2)
        
        if ran == 1:
            #print(self.name, "Blocked!")
            self.block()
        else:
            self.change_defense(number)
        
    def change_attack(self):
        self.attack += 1#find a power up

    def attack_opponent(self):
        self.add_super()
        print(self.attack, self.special)
        self.new_attack = self.attack
        self.attack = 5
        return self.new_attack
    
    def block(self):
        self.blocks += 1
    
    def get_blocks(self):
        return self.blocks
    
    def loss(self):
        return f"{self.name}, you lose."
    
    def winner(self):
        return f"{self.name}, you win!"

class PowerUp(Player):
    #self.heal
    #double damage
    pass

def play_game():
    rounds = 0
    players = [Player("Player1"), Player("Player2")]
    
    var = True
    
    while True:
        
        for each in players:
            rounds += 1
            opponent = players[(players.index(each)+1)%2]
            each.on_defense(opponent.attack_opponent())
            #print(each.get_name(), each.get_health())
            if each.get_health() < 1:
                #print(each.get_name(), each.get_health())
                for player in players:
                    print(f"Name: {player.get_name()}, Health: {player.get_health()}, Blocks: {player.get_blocks()}")
                print(each.loss())
                print(f"Total rounds: {rounds}")
                var = False
                break
            
        #print("\n")
        if var == False:
            break
    
if __name__ == "__main__":
    play_game()

x = input("Please choose an attack: Attack 1 (20 damage) Attack 2 (40 damage):")
print(x)
