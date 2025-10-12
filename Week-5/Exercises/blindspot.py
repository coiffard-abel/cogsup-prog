from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK

data = ('', 0, 0, (0, 0))
full_data = []

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

"""Instructions"""
def display_instr(side):              
    text = stimuli.TextScreen(heading = "Blindspot Finder", text = f"Cover your {side} eye\n\n " \
    "Fix the cross with your other eye\n\n " \
    "Move the circle with your keyboard's arrows until it disappears\n\n " \
    "The circle should disappear when entering your blindspot. If it doesn't, try reducing its size by pressing 2\n\n " \
    "Then try increasing the circle size by pressing 1 and see how big it can be while the effect still working\n\n" \
    "Press SPACE to exit")
    text.present(clear = True, update = True)
    exp.keyboard.wait()

""" Input """
def input_side(prompt):
    """ Asks user for a R or L input."""
    ans = input(prompt) # Ask the user for their guess
    while True: # Repeat until the user inputs a valid letter
        if ans=='R':
            return 1
        if ans=='L':
            return -1
        print('Please, enter "L" or "R"')
        ans = input(prompt)  

""" Experiment """
def run_trial(radius = 75, posCircleX = 0, posCircleY = 0, side = 1, rec_full = False):
    """ Global settings """
    key = 0
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[side*300, 0])
    fixation.preload()
    if side + 1: side='right' 
    else: side='left'
    display_instr(side)
    while(not(key == 32)):
        circle = make_circle(radius, (posCircleX, posCircleY))

        fixation.present(True, False)
        circle.present(False, True)

        key, _ = exp.keyboard.wait()
    
        if(key == 50):
            radius += 5
        elif(key == 49):
            radius -=5
        if(key == 1073741903):
            posCircleX += 5
        elif(key == 1073741904):
            posCircleX -= 5
        if(key == 1073741906):
            posCircleY += 5
        elif(key == 1073741905):
            posCircleY -= 5
        
        if rec_full:
            data = (side, key, radius, (posCircleX, posCircleY))
            full_data.append(data)
            
    data = (side, key, radius, (posCircleX, posCircleY))



side = input_side("Please enter 'R' to test the right eye or 'L' for the left one: ")
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)
control.start(subject_id=1)
run_trial(side=side, rec_full = True)
    
control.end()

if(len(full_data)):
   for side, key, radius, pos in full_data:
    print(f"Trial on {side} eye: key {key} made circle of radius {radius} at pos ({pos[0]}, {pos[1]})")
else:
    print(f"Trial on {data[0]} eye: key {data[1]} made circle of radius {data[2]} at pos ({data[3][0]}, {data[3][1]})")