
# Project : Problem : Dice Rolling game
    # when we execute this program, first we get this question: Roll the dice ? (Y/N):
    # Here we have only 2 options: Yes or No, if you type anything else, we get an error message saying "Invalid choice!"
    # If we type 'y' either in uppercase or lower case, it doesn't matter and every time we get 2 new random numbers.
    # and if we type 'n', our program terminates and displays a message saying 'Thanks for playing!"

# Steps:
# 1. use comments to map out how this program should behave.
# 15. Import random
# 14. loop: While loop is True
    # Declare a variable like 'playing' and initialize it to true, then add it as the loop condition.
    # while playing is true then we're going to repeat this instructions and when user types 'n' then we can use the break statement
    # to jumpout of this loop but better way to do this is to not add another variable and only use 'true'
    # 2. Ask the user a question like: roll the dice?
        # as variable 'value' is a string variable and we have diff string functions available in python.
        # therefore, we use lower() function, to tell python that whatever the user enters : convert that to lower case.
    # 3. Then we should check the user input: 
    # 4. If user enters y
    # 5.    generate 2 random numbers, for this we need to import the random
            # in this module, we have a method, we cann random. randint: that generate a random integer or a random number between two numbers A & B.
            # in this case, between 1 & 6
    # 6.    print them
        # for simplicity, we can use a formatted or an F string 
        # so we type 'f' before our quotes, and inside parentheses we want to print our random numbers
    # 7. If user enters n
    # 8.    print 'thank you message'
    # 9.    Terminate the program.
    # To terminate the program we want to break out of our loop

    # 10. else
    # 11.   print 'invalid choice'
    # 12. You want to make sure that the user can keep playing until they decide to terminate the game.
# 13. so we should put these instructions inside a loop for repetition.



# Program Implementation:

import random

while True:
    Value = input ("Roll the dice: (Y/N) : ").lower()
    if (Value == 'y'):
        num1=random.randint(1,6)
        num2=random.randint(1,6)
        print(f'({num1},{num2})')
    elif (Value == 'n'):
        print("Thanks for playing!")
        break
    else:
        print ("Invalid choice:")
 
