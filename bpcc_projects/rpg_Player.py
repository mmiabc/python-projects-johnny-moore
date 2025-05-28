import random

class Player:

    def __init__(self, name, health, defense, attack_power):
        self.HP = health
        self.Defense = defense
        self.Attack_power = attack_power
        self.KO = False
        self.Name = name

    def level_up(self):
        if not self.KO:
            self.Attack_power += 5
            self.Defense += 3

    def attack(self):
        if not self.KO:
            return self.Attack_power * random.choice([1,2])
        
    def take_hit(self, damage):
        if not self.KO:
            actual_damage = max(0, damage - self.Defense)
            self.HP -= actual_damage
            if self.HP <= 0:
                self.KO = True
    
    def __str__(self):
        if self.KO == False:
            return f'Your player is at {self.HP} health with {self.Attack_power} attack and {self.Defense} defense.'
        else:
            return f'Your player is knocked out!'
        
print('**Johnny Moore - RPG Player Program**')
print('**CTEC 102-902**')
print('')
print('This program will ask for a name to create a RPG player.')
print('Afterwards, the program will demonstrate a few actions of the player.')
print('')
    
#Establish a player for user and display the current status
player1 = Player(input("What is your player's name?: "), 50, random.randint(1,10), random.randint(1,10))
print(player1)
print('')

#Demo attacking
input("Press enter to attack an enemy: ")
player_attack = player1.attack
print('You have destroyed an enemy!')
input('Press enter to continue: ')
print('')

#Demo leveling up
player1.level_up()
print(f"Your player has leveled up to {player1.Attack_power} attack and {player1.Defense} defense!")
input('Press enter to continue: ')
print('')

#Demo taking a hit
print('An enemy approaches and attacks you!')
enemy_attack = 20
player1.take_hit(enemy_attack)
print(f"Your player now has {player1.HP} health points!")
input('Press enter to continue: ')
print('')

#KO player1
print('The enemy attacks again!')
enemy_attack = 50 #High attack
player1.take_hit(enemy_attack)
KO_health = max(0, player1.HP)
print(f"Your player now has {KO_health} health points!")

#Demo not being able to attack while KO
input('Press enter to attack the enemy: ')
player_attack = player1.attack
print(player1)
print("You can't attack!")
print('')

print('Thank you for trying my program.')
input('Press any key to exit: ')





