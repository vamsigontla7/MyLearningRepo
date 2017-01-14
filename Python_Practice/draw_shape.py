import  turtle

def draw_shape() :
    window = turtle.Screen()
    window.bgcolor("pink")

    turtle.shape('turtle')
    turtle.color('yellow')
    turtle.speed(0)
    
    brad = turtle.Turtle()
    brad.color('red')

    i=0
    while i<4 :
        brad.forward(100)
        brad.right(90)
        i = i+1
    
    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)

    steve = turtle.Turtle()
    steve.shape('circle')
    steve.color('yellow')
    j=0
    while j<3 :
        steve.forward(100)
        steve.left(120)
        j = j+1    
    window.exitonclick()
draw_shape()
