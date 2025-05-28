print('Johnny Moore CTEC 102')
print('Files and Exceptions Program')
print('')
print(f'This program will read a file called "numbers.txt"')
print('and display the sum of every other line.')
print('')
input('Press enter to execute the program: ')
print('')

def main():
    try:
        #Open the text file
        file = open('numbers.txt', 'r')
        #Set number to store the sum of two odd numbers
        sum_of_odd_numbers = 0
        #Set line number variable to keep track of lines as running total
        line_number = 1

        #Read the first line
        line = file.readline()

        #Create loop to go through lines if odd and exists
        while line != '':
            #If there is a remainder when divided by 2, then it is odd
            if line_number % 2 != 0:
                #Create exception for non-valid integers
                try:
                    #Create integer variable from the line
                    number = int(line)
                    #Running total of odd numbers
                    sum_of_odd_numbers += number
                except ValueError:
                    print('This line does not contain a valid integer. ')
            #Read next line for loop
            line = file.readline()
            line_number += 1

        file.close()
        print(f'The sum of all odd numbers in the file is {sum_of_odd_numbers}.')
        print('')

    except IOError:
        print('That file does not exist! ')
        print('')

if __name__ == '__main__':
    main()

input('Press enter to end the program: ')