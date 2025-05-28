print('Johnny Moore CTEC 102')
print('Animal Crossing Program')
print('')
print("In this program, I will ask you for a villager name")
print('and generate a personality and hobby for your villager.')
print('')

import random

#Build lists of personalites and hobbies
personalities = ['Normal', 'Lazy', 'Sisterly', 'Snooty', 
                 'Cranky', 'Jock', 'Peppy', 'Smug']
hobbies = ['Education', 'Fashion', 'Fitness', 
           'Music', 'Nature', 'Playing']

keep_going = 'y'

#Build loop to generate villager characteristics until user wants to exit
while keep_going == 'y':
    #Get villager name from user
    villager_name = input('Please enter a name: ')

    #Randomize personalities and hobbies
    personalities_random = random.randint(0, len(personalities) - 1)
    hobbies_random = random.randint(0, len(hobbies) - 1)

    #Select from random indices
    personalities_result = personalities[personalities_random]
    hobbies_result = hobbies[hobbies_random]

    #Print result
    print(f'Your villager, {villager_name}, is {personalities_result} and loves {hobbies_result}.')
    print('')
    keep_going = input("Would you like to enter another villager name? Enter 'y' or 'n': ")
    print('')

print('Thank you for using my program!')
input('Press enter to exit the program: ')