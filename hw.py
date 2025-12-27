import turtle

raphael = turtle.Turtle()
wn = turtle.Screen()

wn.title("Raphael")
wn.bgcolor("red")


raphael.forward(150)


raphael.penup()
raphael.backward(150)
raphael.right(90)
raphael.forward(40)
raphael.left(90)
raphael.pendown()


raphael.forward(150)

wn.mainloop()
turtle.exitonclick()
