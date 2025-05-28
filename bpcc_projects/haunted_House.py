#This program allows users to explore 
#rooms in a haunted house from a selection of rooms
#Variables to control loop
hours_spent = 0
exploring = True

#Welcome user to the house
print("Welcome to Bly Manor!") 
print("Which would room would you like to explore first?")

#Start loop for room exploring choices
while exploring:
      print('Enter 1 to go to the parlor,') 
      print('Enter 2 to go to the library,')  
      print('Enter 3 to go to the bedroom,')
      room = input('Enter 0 to leave the house! ')
      print('--------------')
      if room == '1':
            print('As soon as you enter the parlor,')
            print('the lights flicker and you see')
            print('a quick flash of a ghost in front of you!!')
            print('Do you need to see more?')
            print('--------------')
            hours_spent += 1
      elif room == '2':
            print('You enter the library, ')
            print('and books fly off the shelves toward you!!!')
            print('Where to now?')
            print('--------------')
            hours_spent += 1
      elif room == '3':
            print('You enter the bedroom, ')
            print('and the bed lifts off the floor!')
            print('Where would you like to go next?')
            print('--------------')
            hours_spent += 1
      elif room == '0':
            exploring = False
      else:
            print('That is not an option. Try again.')
            print('--------------')

print('I guess the manor was too much for you!!!')
print(f'You spent {hours_spent} hour[s] in the manor...')
print('Congratulations on your survival...')
            
          


