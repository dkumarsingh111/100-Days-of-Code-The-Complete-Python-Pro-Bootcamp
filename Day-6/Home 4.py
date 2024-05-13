#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%204&url=worlds%2Ftutorial_en%2Fhome4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
    
while at_goal() != True:
    if(wall_in_front() and wall_on_right()):
       turn_left()
    elif(right_is_clear()):
        turn_right()
        move()
    else:
        move()
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
