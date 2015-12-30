# template for "Stopwatch: The Game"

import simplegui

# define global variables
var = 0
num_of_stops = 0
num_of_successes = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    sec = (t/10) % 60
    mini_sec = t % 10
    min = (t/10) / 60
    min_str = str(min)
    sec_str = str(sec)
    if(min < 10):
        min_str = '0' + str(min)
    if(sec < 10):
        sec_str = '0' + str(sec)
    return min_str + ':' + sec_str + ':' + str(mini_sec)
    

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()

def stop_handler():
    timer.stop()
    global num_of_stops
    global num_of_successes
    global var
    num_of_stops += 1
    if(var % 10 == 0):
        num_of_successes += 1

def reset_handler():
    global var
    var = 0
    timer.stop()
    global num_of_stops
    global num_of_successes
    num_of_stops = 0
    num_of_successes = 0

def increment_count():
    global var
    var += 1

# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, increment_count)


# define draw handler
def draw(canvas):
    global var
    global num_of_stops
    global num_of_successes
    canvas.draw_text(format(var), (70, 120), 30, "White")
    canvas.draw_text(str(num_of_successes)+'\\'+ str(num_of_stops),(250, 60), 20, "White")

    
# create frame
frame = simplegui.create_frame("Stop Watch", 300, 200)
frame.add_button("Start", start_handler ,100)
frame.add_button("Stop",stop_handler ,100)
frame.add_button("Reset", reset_handler ,100)


# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric


