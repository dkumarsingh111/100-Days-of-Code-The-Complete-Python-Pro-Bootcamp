#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
      
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
### Solution-1
while at_goal() != True:
    jump()

### Solution-2
# noOfLaps = 6
# for lap in range(0, noOfLaps):
#     jump()   
        
        


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
