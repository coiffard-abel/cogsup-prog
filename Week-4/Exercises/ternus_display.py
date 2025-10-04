from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE

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

def make_circles(r, tags, gap):
    circles = []
    for i in range(3):
        circles.append(stimuli.Circle(radius=r, position = ((2*r+gap)*i-(r+gap//2)*3, 0), colour = (225, 225, 225)))
    
    if tags:
        for i in range(3):
            circles.append(stimuli.Circle(radius=r/10, position = ((2*r+gap)*i-(r+gap//2)*3, 0), colour=[(225, 0, 0), (0, 225, 0), (0, 0, 225)][i]))
    
    return circles

def ternus(r, isi, tags):
    circleDuration = 200
    maxIterations = 100
    gap = r//3
    isi *= 1000//60

    circles = make_circles(r, tags, gap)
    
    for i in range(maxIterations):
        present_for(circles, circleDuration)

        if exp.keyboard.check(K_SPACE):
            break

        if isi>0:
            t0 = exp.clock.time
            exp.screen.clear()
            exp.screen.update()
            
        circles[0].position = ((2*((i+1)%2)-1)*(r+gap//2)*3, 0)
        if tags:
            circles[3].position = ((2*((i+1)%2)-1)*(r+gap//2)*3, 0)

        if isi>0:
            dt = exp.clock.time-t0
            exp.clock.wait(isi-dt)

exp = design.Experiment(name="ternus display")

#control.set_develop_mode()
control.initialize(exp)

ternus(70, 0, False)
exp.screen.clear()
exp.screen.update()
exp.clock.wait(1000)

ternus(70, 3, False)
exp.screen.clear()
exp.screen.update()
exp.clock.wait(1000)

ternus(70, 1, True)


control.end()