import random
secretNumber = 52

print('Johnny Moore - CTEC 102 Midterm Program\n')
print("This program will ask for a number, \n"
      "and the user will be given options to transform the number\n"
      "until a secret number is found.\n")

def main():
    number = (int(input('Please enter a number: ')))
    exit_program = False
    while exit_program == False:
        print("\n" "Enter 1 to multiply the number by 3.\n"
            "Enter 2 to integer divide the number by 2.\n"
            "Enter 3 to add a random number to the number (from 1 to 5).\n"
            "Enter 4 to subtract 1 from the number.\n"
            "Enter 5 to check if the number is the secret number.")
        options = (int(input('Enter 0 to exit: ')))
        if options == 1:
            number = number * 3
            print(f'The number is now {number}.')
        elif options == 2:
            number = int(number // 2)
            print(f'The number is now {number}.')
        elif options == 3:
            number = number + random.randint(1,5)
            print(f'The number is now {number}.')
        elif options == 4:
            number = number - 1
            print(f'The number is now {number}.')
        elif options == 5:
            if number == secretNumber:
                print("Congratulations! That's the secret number!")
            elif number > secretNumber:
                print('Sorry, that number is too high to be the secret number.')
            else: 
                print('Sorry, that number is too low to be the secret number.')
        elif options == 0:
            exit_program = True
        else:
            print('That is not a valid option.')
    print(f'\nYour final number is {number}. Thank you for your time.')
    input('Press any key to exit:')
            
if __name__ == '__main__':
    main()