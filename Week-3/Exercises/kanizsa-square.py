from expyriment import design, control, stimuli, io

exp = design.Experiment(name = "Square", background_colour = (100, 100, 100))

control.initialize(exp)

circles = []

width, height = exp.screen.size
taille = (width//4, width//4)
r = width//20

for x, c in [(-width//8, 255), (width//8, 0)]:
    for y in [-width//8, width//8]:
        circles.append(stimuli.Circle(radius = r, position = (y, x), colour = (c, c, c)))

square4 = stimuli.Rectangle(size = taille, colour = (100, 100, 100), position = (0, 0))

circles[0].present(clear=True, update =False)
circles[1].present(clear=False, update =False)
circles[2].present(clear=False, update =False)
circles[3].present(clear=False, update =False)
square4.present(clear=False, update=True)

exp.keyboard.wait()

control.end()