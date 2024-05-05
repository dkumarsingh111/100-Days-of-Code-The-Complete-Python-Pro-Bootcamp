#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
noOfLaps = 1000
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for lap in range(0, noOfLaps):
    if(at_goal()):
        done()
    elif(wall_in_front()):
       jump()
    else:    
        move()
        


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
