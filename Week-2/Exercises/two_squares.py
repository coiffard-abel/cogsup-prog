from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name = "Square")

control.initialize(exp)

fixation = stimuli.FixCross()

squareR = stimuli.Rectangle((50,50), (255, 0, 0), position = (-125,0)) #200px is edge-to-edge

squareB = stimuli.Rectangle((50,50), (0, 0, 255), position = (125,0))

control.start(subject_id=1)

squareR.present(clear=True, update=False)

squareB.present(clear=False, update=True)

exp.clock.wait(500)

exp.keyboard.wait()

control.end()