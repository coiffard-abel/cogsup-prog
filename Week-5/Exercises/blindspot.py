from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

"""Instructions"""
def display_instr():
    text = stimuli.TextScreen(heading = "Blindspot Finder", text = "Cover your right eye\n\n " \
    "Fix the cross with your left eye\n\n " \
    "Move the circle with your keyboard's arrows until it disappears\n\n " \
    "The circle should disappear when entering your blindspot. If it doesn't, try reducing its size by pressing 2\n\n " \
    "Then try increasing the circle size by pressing 1 and see how big it can be while the effect still working\n\n" \
    "Press SPACE to exit")
    text.present(clear = True, update = True)
    exp.keyboard.wait()

""" Experiment """
def run_trial(radius = 75, posCircleX = 0, posCircleY = 0):
    key = 0
    display_instr()
    while(not(key == 32)):
        fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0])
        fixation.preload()

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


control.start(subject_id=1)

run_trial()
    
control.end()