import  turtle

def draw_square(some_turtle) :
    for i in range (1,5) :
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art() :
    window = turtle.Screen()
    window.bgcolor('Pink')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('red')
    brad.speed(3)
    for i in range (1,37) :
        draw_square(brad)
        brad.right(10)
    window.exitonclick()
draw_art()
