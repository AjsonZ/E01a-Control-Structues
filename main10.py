#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')                 # print out 'Greeting!'
colors = ['red','orange','yellow','green','blue','violet','purple']         # make a list of color
play_again = ''                     # make "play again" empty
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'):                           #start a while loop with two conditions
    match_color = random.choice(colors)                                     # using random method to select a color randomly
    count = 0                       # count strat with 0
    color = ''                      # make color empty
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()                   # It turns all letters on 'color' into the lower case and delete all the spaces.
        count += 1                                      # the 'count' will plus one after finishing a loop 
        if (color == match_color):                      # if color equals to match_color, it will execute the following codes
            print('Correct!')                           # when condition is true, it will print out 'Correct！'
        else:                                           # if false
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))  # if false, it will print out this line.
    print('\nYou guessed it in {0} tries!'.format(count))  # print out this line in the next line with the number of user's tries
    if (count < best_count):                            # if user's tries are less than best_count which is the biggest number
        print('This was your best guess so far!')       # it will print out this line
        best_count = count                              # let best_count = count
    play_again = input("\nWould you like to play again? ").lower().strip()      # print this out on the next line and delete all spaces and turn it into lower case.
print('Thanks for playing!')                            # print out 'Thanks for playing.'