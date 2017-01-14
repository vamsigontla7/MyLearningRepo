import turtle

def draw_outer_triangle(some_turtle) :
    for i in range (1,4) :
        some_turtle.forward(250)
        some_turtle.left(120)

def draw_inner_triangle() :
    brad = turtle.Turtle()
    brad.color('yellow')
    for i in range (1,6) :
        brad.forward(50)
        brad.left(120)
        for i in range(1,6) :
            brad.begin_fill()
            for i in range (1,4) :
                brad.forward(25)
                brad.left(120)
            brad.end_fill()
    
def draw_shape() :
    window = turtle.Screen()
    window.bgcolor('white')

    steve = turtle.Turtle()
    steve.shape('turtle')
    steve.color('black')
    steve.speed(0)
    for i in range (1, 2) :
        draw_outer_triangle(steve)
        steve.right(10)
        draw_inner_triangle()
    window.exitonclick()
draw_shape()
