print('Johnny Moore CTEC 102')
print('Taste Journal Program')
print('')
print(f"This program will ask your input on foods and their tastes',")
print('then deliver the answers to a Taste Journal dictionary.')
print('')
input('Press enter to begin the program: ')

#Create empty dictionary
taste_journal = {}

while True:
    try: 
        #Ask user for choice of action
        answer = int(input('\nEnter 1 to add a new food,\nEnter 2 to look up an entry, Enter 0 to exit: '))
        
        if answer == 1:
            food_entry = input('\nWhich food would you like to add? ')
            taste_entry = input('\nWhat is your opinion on the taste of the food? ')
            taste_journal[food_entry] = taste_entry
        elif answer == 2:
            look_up = input('\nWhich food would you like to look up? ')
            if look_up in taste_journal: 
                print(f'\nYour opinion of {look_up}? "{taste_journal[look_up]}!"')
            else:
                print('\nThat food entry can not be found.')
        elif answer == 0:
            print('\nThank you for playing along!')
            break
        else:
            print('That is not a valid option.')
    except ValueError:
        print('\nSorry, that is not a valid input. Try again.')
input('Press a key to exit the program: ')