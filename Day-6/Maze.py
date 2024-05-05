#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_right()
    move()


### Solution-1
while at_goal() != True:
    if(wall_in_front() and wall_on_right()):
       turn_left()
    elif(wall_on_right()):
       move()
    elif(right_is_clear()):
       jump()
    elif(front_is_clear()):
       move()
    else:    
        move()




### Solution-2
# noOfLaps = 1000    
# for lap in range(0, noOfLaps):
#     if(at_goal()):
#         done()
#     elif(wall_in_front() and wall_on_right()):
#        turn_left()
#     elif(wall_on_right()):
#        move()
#     elif(right_is_clear()):
#        jump()
#     elif(front_is_clear()):
#        move()
#     else:    
#         move()
        


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
