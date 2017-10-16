# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math

# initialize global variables used in your code
secret_number = 0
low = 0
high = 0
guess_remaining = 0
# helper function to initial game
def new_game():
	global secret_number, low, high, guess_remaining
	secret_number = random.range(low,high)
	guess_remaining = int(math.ceil(math.log((high-low+1),2)))
	print " "
	print "New game. Range is from ", low + "to ", high
	print " Number of remaining guesses is", guess_remaining 
# define callback functions for control panel

def range100():
    global low, high
    (low,high) = (0,100)
    new_game()

def range1000():
    global low, high
    (low,high) = (0,1000)
    new_game()

def input_guess(guess):
  	global guess_remaining
    print " "
  	print "Guess is", guess
  	guess_remaining = guess_remaining - 1
  	print "Number of remaining guesses is", guess_remaining
  	guess = int(guess)
  	if guess_remaining > 0 :
  		if guess == secret_number :
  			print "Correct!"
  			new_game()
  	    elif guess < secret_number :
  			print "Higher!"
  	    else :
  			print "Lower!"
    else:
    	if guess == secret_number :
    		print "Correct!"
    	else :
  			print "You ran out of guesses. The number was ", secret_number
  	    new_game()
    
# create frame
f = simplegui.create_frame("Guess the number", 100, 200)

# create control elements for window
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

new_game()

