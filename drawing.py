from turtle import *


def draw_smile():
    """Draw a simple emoji-style smiley face using turtle graphics"""
    clear()
    reset()
    setup(600, 600, 0, 0)
    speed(6)
    bgcolor('lightblue')

    # face
    penup(); goto(0, -150); pendown()
    pensize(3); pencolor('black'); fillcolor('yellow')
    begin_fill(); circle(150); end_fill()

    # eyes (use dot for brevity)
    penup(); goto(-50, -30); pendown(); dot(30, 'black')
    penup(); goto(50, -30); pendown(); dot(30, 'black')

    # simple smile arc
    penup(); goto(-60, -80); pendown()
    pensize(6); pencolor('black')
    setheading(-60)
    circle(80, 120)

    hideturtle()
    exitonclick()


def draw_tree():
    """Draw a simple tree using turtle graphics"""
    clear()
    reset()
    setup(600, 600, 0, 0)
    speed(6)
    bgcolor('lightblue')
    
    penup()
    goto(-25, -250)
    pendown()
    pensize(2)
    pencolor('brown')
    fillcolor('saddlebrown')
    begin_fill()
    setheading(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(100)
    right(90)
    forward(50)
    end_fill()
    
    penup()
    goto(-40, -100)
    pendown()
    fillcolor('green')
    begin_fill()
    circle(50)
    end_fill()
    
    penup()
    goto(40, -100)
    pendown()
    begin_fill()
    circle(50)
    end_fill()

    penup()
    goto(0, -60)
    pendown()
    fillcolor('limegreen')
    begin_fill()
    circle(45)
    end_fill()
    
    hideturtle()
    exitonclick()


print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for smile, 2 for tree)\n"
              "Your selection is: ")
    try:
        a = int(a)
        if a == 1:
            draw_smile()
        elif a == 2:
            draw_tree()
        else:
            print("Please input the value in [1,2]")
    except ValueError:
        print("Please input the value in [1,2]")


