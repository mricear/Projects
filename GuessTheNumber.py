
import random
import simplegui

number_of_guesses = 0
max_number = 100


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    frame = simplegui.create_frame("guess_number", 200, 200)
    frame.add_button("Range is [0,100)", range100, 200)
    frame.add_button("Range is [0,1000)", range1000, 200)
    frame.add_input("Enter a guess", input_guess, 100)
    
    global secret_number
    global max_number
    
    secret_number = random.randrange(0,max_number)
   
    global number_of_guesses 
    print "Number of remaining guesses is", number_of_guesses
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    print "New game. Range is from 0 to 100"
    global max_number 
    max_number = 100
    global number_of_guesses 
    number_of_guesses = 7

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print "New game. Range is from 0 to 1000"
    global max_number 
    max_number = 1000
    global number_of_guesses 
    number_of_guesses = 10
    
    
def input_guess(guess):
    global secret_number
    global number_of_guesses
    
    
    # main game logic goes here	
    guess_number = int(guess)
    print "Guess was", guess_number 
    
    number_of_guesses -= 1
    print "Number of remaining guesses is", number_of_guesses
    
    if(guess_number > secret_number):
        print "Lower!"
    
    elif(guess_number < secret_number):
        print "Higher!"
    
    else:
        print "Correct!"
        new_game()
        return
    
    if(number_of_guesses <= 0):
        print "You ran out of guesses. The number was", secret_number
        new_game()
        return
        
    

    
# create frame


# register event handlers for control elements and start frame


# call new_game 
#new_game()


# always remember to check your completed program against the grading rubric

#input_guess(5)

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console



secret_number = 74	
range100()
new_game()
input_guess("50")
input_guess("75")
input_guess("62")
input_guess("68")
input_guess("71")
input_guess("73")
input_guess("74")


