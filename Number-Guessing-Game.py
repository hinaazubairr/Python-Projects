# Program: Number Guessing Game
# 1. Program generates a random number.
    # To generate a random number, import the random module.
    # generates a random number between 1 and 100.
    # store this random number in a variable.
    # we do not include this random import line in loop as we want to generate a random number only once.
# 8. we use loop for repetition, so that user can make multiple guesses.
    # we use the while loop here. for infinitive loop

# 2. Ask the user for an input to make a guess: 'Guess the number between 1 and 100'
    # store this number in a variable.
    # also convert it into int.
    # print this number on screen.
    # 3. when we run this program till here, and enter an invalid input like 'a' then the program crashed, because an exception is thrown on this line.
    # and the type of exception is: Value Error. So to handle this situation & prevent our program from crashing, we have to add this line is try block.
    #except followed by the type of error we want to handle. In this situation, valueerror and says 'Please enter a valid number'

    # 4. if user enters a number between 1 and 100, then check if that number is higher to num1 which is guess number.
        # print too high 
    # 5. if user number entered is less than the number to guess then print 'too low' 
        # we have to add this line of code in the try block, otherwise we get an error of variable scope.
    
    # 6. if user enters an invalid character, 
    #   then the program prints an error: ' Please enter a valid number'
    # 7. else , number equal guess and print 'well done'

# 1.
import random

num_to_guess= random.randint(1,100) #8

# 8.
while True:
    # 3.
    try:
        # 2.
        user_input= int(input('Guess the number between 1 and 100: ')) 
        # 5.
        if (user_input<num_to_guess): 
            print("Too low")
        # 4.
        elif (user_input>num_to_guess): 
            print("Too high")
        # 7.
        else:
            print("Congratulations! You guessed the number!")
            break
     #6.       
    except ValueError:
        print('Please enter a valid number')

    
    
    