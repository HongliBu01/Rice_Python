# template for "Stopwatch: The Game"
import simplegui

# define global variables
t = 0
tries = 0
wins = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):    
    A = t // 600
    B = (((t // 10) % 60) // 10)
    C = (((t // 10) % 60) % 10)
    D = t % 10
    return str(A) + ":" + str(B) +str(C) + "." + str(D)
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
	timer.start()

def reset():
    global tries, wins, t
    tries = 0 
    wins = 0
    t = 0
    timer.start()

def stop():
	global tries, wins, t
    tries += 1 
	if (t % 10) == 0:
		wins += 1
	timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
	global t
	t = t + 1

# define draw handler
def draw(canvas):
	canvas.draw_text(format(t), [100,100], 30, "White")
    canvas.draw_text(str(wins) + "/" + str(tries), [150,30], 15, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch",200,200)

# register event handlers
frame.add_button("start", start, 100)
frame.add_button("stop", stop, 100)
frame.add_button("reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
# start frame
frame.start()

# Please remember to review the grading rubric