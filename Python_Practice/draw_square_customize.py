import  turtle

def draw_square() :
    window = turtle.Screen()
    window.bgcolor("pink")

    turtle.shape('turtle')
    turtle.color('red')
    turtle.speed(0)
    
    brad = turtle.Turtle()
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)
    
    window.exitonclick()
draw_square()
