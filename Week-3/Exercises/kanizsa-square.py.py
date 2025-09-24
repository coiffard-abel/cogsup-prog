from expyriment import design, control, stimuli, misc

control.set_develop_mode()

exp = design.Experiment(name = "Square")

control.initialize(exp)

width, height = exp.screen.size
taille = (width//4, width//4)
r = width//10
width, height = exp.screen.size

for x in (-width//4, width//4):
    for y in (-width//4, width//4):
        circles = [stimuli.Circle(radius = r, position = (width//2+x, height//2+y), colour = (0, 0, 0))]


square4 = stimuli.Rectangle(size = (taille, taille), position = (0, 0), colour = (100, 100, 100))


circle4.present(clear=False, update=False)
square4.present(clear=False, update=True)

exp.keyboard.wait()

control.end()