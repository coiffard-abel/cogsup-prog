from expyriment import design, control, stimuli, io
import math

exp = design.Experiment(name = "Kanizsa", background_colour = (100, 100, 100))

control.initialize(exp)
width, height = exp.screen.size

def display_kanizsa(factor, ratio = 1, cfactor = 1):
    circles = []
    w = math.sqrt(factor*factor/(ratio*ratio+1))
    l = math.sqrt(factor*factor-w*w)
    taille = (w, l)
    r = factor//(6*cfactor)

    for x, c in [(-w//2, 255), (w//2, 0)]:
        for y in [-l//2, l//2]:
            circles.append(stimuli.Circle(radius = r, position = (y, x), colour = (c, c, c)))

    square4 = stimuli.Rectangle(size = taille, colour = (100, 100, 100), position = (0, 0))

    circles[0].present(clear=True, update =False)
    circles[1].present(clear=False, update =False)
    circles[2].present(clear=False, update =False)
    circles[3].present(clear=False, update =False)
    square4.present(clear=False, update=True)

display_kanizsa(factor = math.sqrt(width*width+height*height)//5)

exp.keyboard.wait()

control.end()