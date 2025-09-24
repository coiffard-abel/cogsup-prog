from expyriment import design, control, stimuli, misc

control.set_develop_mode()

exp = design.Experiment(name = "Square")

control.initialize(exp)

taille = 50
width, height = exp.screen.size

square1 = stimuli.Rectangle(size = (taille, taille), position = (width//2-taille//2, height//2-taille//2), colour = (0, 255, 0), )
square2 = stimuli.Rectangle(size = (taille, taille), position = (width//2-taille//2, -height//2+taille//2), colour = (255, 255, 0))
square3 = stimuli.Rectangle(size = (taille, taille), position = (-width//2+taille//2, -height//2+taille//2), colour = (255, 255, 0))
square4 = stimuli.Rectangle(size = (taille, taille), position = (-width//2+taille//2, height//2-taille//2), colour = (255, 255, 0))

square1.present(clear=True, update=False)
square2.present(clear=False, update=False)
square3.present(clear=False, update=False)
square4.present(clear=False, update=True)

exp.keyboard.wait()

control.end()