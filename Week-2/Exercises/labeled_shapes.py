from expyriment import design, control, stimuli, misc
import math

# Init phase

exp = design.Experiment(name = "Square")

control.initialize(exp)

fixation = stimuli.FixCross()

hexagon = stimuli.Shape(position = (125,0), colour = (255, 255, 0), vertex_list = misc.geometry.vertices_regular_polygon(6, 24.94))

#hexagon height = triangle height = 21.65px => hexagon side = 24.94px with online hexagon converter from inner circle to side

hline = stimuli.Line((125, 21),(125, 71), 3, (255, 255, 255))

htext = stimuli.TextLine("hexagon", (125, 82), text_colour = (255, 255, 255))

triangle = stimuli.Shape(position = (-125,0), colour = (125, 0, 125), vertex_list = misc.geometry.vertices_regular_polygon(3, 50))

#triangle height (from center) = sqrt(50^2-25^2)/2 = 21.65px

tline = stimuli.Line((-125, 21),(-125, 71), 3, (255, 255, 255))

ttext = stimuli.TextLine("triangle", (-125, 82), text_colour = (255, 255, 255))

control.start(subject_id=1)


# Display

hexagon.present(clear=True, update=False)

hline.present(clear=False, update=False)

htext.present(clear=False, update=False)

ttext.present(clear=False, update=False)

triangle.present(clear=False, update=False)

tline.present(clear=False, update=True)

exp.keyboard.wait()

control.end()