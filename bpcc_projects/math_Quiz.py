#This program will generate a simple math quiz
#and give the total correct results at the end.

import random

#Constants
ADD = 1         #This creates the coin toss for the operations
SUB = 2 
QUESTIONS = 10  #This sets the number of questions

print('Johnny Moore, CTEC 102: Math Quiz program')
print('')
print('[This program will generate a math quiz of 10 questions.]')
print('')

def main():
    count = 0           #This is for numbering the questions
    correct_count = 0   #This is for totaling the correct answers
    for toss in range(QUESTIONS):
        operation = random.randint(ADD,SUB) #This randomizes the operation
        num1 = random.randint(1,50) #This randomizes the numbers
        num2 = random.randint(1,50) #from 1 to 50
        count += 1 #This adds to the question count each iteration
        if operation == ADD:
            correct_answer = num1 + num2
            correct_count = ask_question(num1, num2, '+', correct_answer, count, correct_count)    
        else:
            correct_answer = num1 - num2
            correct_count = ask_question(num1, num2, '-', correct_answer, count, correct_count)
    print(f'Finished! You got {correct_count} out of 10 answers correct!')

def ask_question(num1, num2, operator, correct_answer, count, correct_count):
    user_answer = int(input(f'{count}.  What is {num1} {operator} {num2}? '))
    if user_answer == correct_answer:
        print('Congratulations, that is the correct answer!')
        print('')
        correct_count += 1
    else:
        print(f'Sorry, the correct answer is {correct_answer}.')
        print('')
    return correct_count

main()
input('Press enter to exit. ')