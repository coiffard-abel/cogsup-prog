from expyriment import design, control, stimuli

def display_hermann(nrows, ncolumns, sqsize, intersqu, bgcolor = (255, 255, 255), sqcolor = (0, 0, 0)):
    exp = design.Experiment(name = "Hermann", background_colour = bgcolor)

    control.initialize(exp)
    squares = []

    cornerx = -(ncolumns-1)*(sqsize+intersqu)//2
    cornery = -(nrows-1)*(sqsize+intersqu)//2

    for y in range(nrows):
        for x in range(ncolumns):
            squares.append(stimuli.Rectangle(size = (sqsize, sqsize), position = (cornerx+x*(sqsize+intersqu), cornery+y*(sqsize+intersqu)), colour = sqcolor))

    for square in squares:
        square.present(clear=(square==squares[0]), update =(square==squares[len(squares)-1]))

    exp.keyboard.wait()


display_hermann(nrows = 5, ncolumns = 10, sqsize = 50, intersqu = 8)

control.end()