# Program 4: Write a python program in which you ask 4 questions from your classmates.
# Name of this program is: introduce_app.py
# This app will ask classmates their name and a few questions about themselves.
# afterwards, the app will share the answers given by the classmates.


# First greet your classmates
print('Welcome back to school after holidays! Answer these 3 questions to introduce yourself')

# Ask 1st question from your classmates and store the answer in a variable using input().
# QUESTION 1
name = input (' What is your name? ')
print(name)

# Add more questions
# QUESTION 2
color = input (' What is your favorite color? ')
print(color)

# QUESTION 3
food = input (' What is your favorite food? ')
print(food)

# QUESTION 4
tvshow = input (' What is your favorite TV show? ')
print(tvshow)


# Use string formatting: This is a quick way to insert your variable values into a sentence.
# f'This is a sentence {variable}.'
print(f"Everyone, meet {name}'s favorte color is {color}. {name}'s favorite food is {food}. {name}'s favorite TV show is {tvshow}.")
# Program 4: ends here
