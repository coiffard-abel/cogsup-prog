from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name = "Square")

control.initialize(exp)

fixation = stimuli.FixCross()

squareR = stimuli.Rectangle((50,50), (255, 0, 0), position = (-400,0)) #200px is edge-to-edge

squareG = stimuli.Rectangle((50,50), (0, 255, 0), position = (0,0))

control.start(subject_id=1)


for i in range(117):
    squareR = stimuli.Rectangle((50,50), (255, 0, 0), position = (-400+3*i,0)) #200px is edge-to-edge

    squareG = stimuli.Rectangle((50,50), (0, 255, 0), position = (0,0))

    squareR.present(clear=True, update=False)

    squareG.present(clear=False, update=True)


exp.keyboard.wait()

control.end()