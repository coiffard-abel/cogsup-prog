from expyriment import design, control, stimuli

# Init phase

control.set_develop_mode()

exp = design.Experiment(name = "Square")

control.initialize(exp)

squareR = stimuli.Rectangle((50,50), (255, 0, 0), position = (-425,0)) #center of the square is at x=-400

squareG = stimuli.Rectangle((50,50), (0, 255, 0), position = (-25,0)) #center of the square is at x=0

control.start(subject_id=1)

# Displaying init config

squareR.present(clear=True, update=False)

squareG.present(clear=False, update=True)

exp.clock.wait(1000)

# Moving the red square

for i in range(66):
    squareR = stimuli.Rectangle((50,50), (255, 0, 0), position = (-400+i*5,0))
    # -400+(66-1)*5 = -75 position of the red square left side at the end => -75+50 = -25 position of its right side

    squareG = stimuli.Rectangle((50,50), (0, 255, 0), position = (-25,0)) # -25 position of the green square left side

    squareR.present(clear=True, update=False)

    squareG.present(clear=False, update=True)

exp.clock.wait(70) #disrupting time of 70ms which is small enough for the effect to persist

# Moving green square

for i in range(66):
    squareR = stimuli.Rectangle((50,50), (255, 0, 0), position = (-75,0)) # Red square stays at the same position

    squareG = stimuli.Rectangle((50,50), (0, 255, 0), position = (-25+i*5,0))
    # Starting from the center, the green square takes the same number of steps (65) at the same speed (5*i) as red, thus same time

    squareR.present(clear=True, update=False)

    squareG.present(clear=False, update=True)

# Displaying final config

exp.clock.wait(1000)

control.end()