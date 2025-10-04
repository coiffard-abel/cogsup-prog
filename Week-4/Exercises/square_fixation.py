from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")

control.initialize(exp)

fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5)

control.start(subject_id=1)

exp.screen.clear()
fixation.present(clear=True, update=True)
exp.clock.wait(500)

square.present(clear=False, update=True)
exp.keyboard.wait()

control.end()