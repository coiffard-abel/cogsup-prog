from expyriment import design, control, stimuli

def preloading(stimuli):
    for stimulus in stimuli:
        stimulus.preload()

def draw(stimuli):
    t0 = exp.clock.time
    for stimulus in stimuli:
        stimulus.present(clear=(stimulus==stimuli[0]), update=(stimulus==stimuli[len(stimuli)-1]))
    return exp.clock.time - t0

def present_for(stimuli, time):
    exp.clock.wait(time-draw(stimuli))



exp = design.Experiment(name="timing puzzle")

#control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")

preloading([fixation, text])
t0 = exp.clock.time
present_for([fixation], 1000)
t1 = exp.clock.time
text.present(clear = True, update = True)

fix_duration = (t1 - t0)/1000

exp.clock.wait(1000)

units = "second" if fix_duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.clock.wait(2000)

control.end()