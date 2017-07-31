import turtle

triangle=turtle.clone()
triangle.shape("triangle")

#this works, but theres more options
#triangle.goto(50, 50)
#triangle.goto(50, -50)
#triangle.goto(0, 0)

triangle.forward(50)
triangle.left(120)
triangle.forward(100)
triangle.left(120)
triangle.forward(100)
triangle.left(120)
triangle.forward(50)

triangle.left(90)
