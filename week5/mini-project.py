
# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 100
CARD_LIST= range(8)

def new_game():
	global cards, exposed, state, turn
	cards =  CARD_LIST * 2
	random. shuffle(cards)
	exposed = [False] * len(cards)
	state, turn = 0, 0
	label.set_text("Turns = " + str(turn))

# define event handlers
def mouseclick(pos):
	global state, turn, pre_index1, pre_index2
	index = pos[0] // 50
    if not exposed [index]:
    	if state == 0:
    		exposed [index] = True
    		pre_index1 = index
    		state = 1
    	elif state == 1:
    		exposed [index] = True
    		pre_index2 = index
    		state =2
    		turn += 1
    		label.set_text("Turns = " + str(turn))
    	else:
    		if cards[pre_index2] != cards[pre_index1]:
    			exposed[pre_index1], exposed[pre_index2] = False, False
    		exposed[index] = True
    		pre_index1 = index
    		state = 1


# cards are logically 50x100 pixels in size
def draw(canvas):
	for card_index in range(len(cards)):
		card_pos = 50 * card_index
		if not exposed[card_index]:
			canvas.draw_polygon([[card_pos,0],[card_pos, CANVAS_HEIGHT],[card_pos + 50, CANVAS_HEIGHT],[card_pos + 50, 0]], 4, "Black", "Green")
		else:
			canvas.draw_text(str(cards[card_index]), [card_pos, 80], 20, "White")
		

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
