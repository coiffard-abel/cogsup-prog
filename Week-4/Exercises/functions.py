from expyriment import design, control, stimuli
import random

def load(stims):
    for stimulus in stims:
        stimulus.preload()

def timed_draw(exp, stims):
    t0 = exp.clock.time
    for stimulus in stims:
        stimulus.present(clear=(stimulus==stims[0]), update=(stimulus==stims[len(stims)-1]))
    return exp.clock.time - t0

def present_for(exp, stims, t=1000):
    exp.clock.wait(t-timed_draw(exp, stims))
