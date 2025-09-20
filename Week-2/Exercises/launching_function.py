from expyriment import design, control, stimuli

# Global init

exp = design.Experiment(name = "Square")

control.initialize(exp)

control.start(subject_id=1)



def launching_function(time_disrupt, space_disrupt, speed_fact):

    # Init phase

    squareR = stimuli.Rectangle((50,50), (255, 0, 0), position = (-425,0)) #center of the square is at x=-400

    squareG = stimuli.Rectangle((50,50), (0, 255, 0), position = (-25,0)) #center of the square is at x=0

    # Displaying init config

    squareR.present(clear=True, update=False)

    squareG.present(clear=False, update=True)

    exp.clock.wait(1000)

    # Moving red square

    for i in range((65-space_disrupt//5)+1):
        squareR = stimuli.Rectangle((50,50), (255, 0, 0), position = (-400+i*5,0)) 

        squareG = stimuli.Rectangle((50,50), (0, 255, 0), position = (-25,0)) # -25 position of the green square left side

        squareR.present(clear=True, update=False)

        squareG.present(clear=False, update=True)

    exp.clock.wait(time_disrupt) #disrupting time
    
    # Moving green square

    for i in range(65//speed_fact+1):
        squareR = stimuli.Rectangle((50,50), (255, 0, 0), position = (-75-space_disrupt,0)) # Red square stays at the same position

        squareG = stimuli.Rectangle((50,50), (0, 255, 0), position = (-25+i*5*speed_fact,0)) 
        # Starting from the center, the green square takes the same number of steps (65) at the same speed (5*i) as red, thus same time

        squareR.present(clear=True, update=False)

        squareG.present(clear=False, update=True)

    # Displaying final config

    exp.clock.wait(1000)


launching_function(0, 0, 1)
launching_function(70, 0, 1)
launching_function(0, 25, 1)
launching_function(0, 0, 3)

control.end()