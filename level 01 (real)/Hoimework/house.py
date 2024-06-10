#librarys
from turtle import*

#speed of drawing
speed(10)

#drawing a house
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#moving a arrow
penup()
goto(200, 200)
pendown()

#drawing a roof
color("blue")
begin_fill()
left(120)
forward(200)
right(-120)
forward(200)
end_fill()

#drawing windows
penup()
goto(80,0)
pendown()
left(120)
forward(40)
left(90)
forward(80)
left(90)
forward(40)
left(90)
forward(80)

penup()
goto(10,120)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(140,120)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

#drawing cross lines
penup()
goto(35,120)
pendown()
left(180)
forward(50)

penup()
goto(10,145)
pendown()
right(90)
forward(50)

penup()
goto(140,145)
pendown()

forward(50)

penup()
goto(165,120)
pendown()
right(-90)
forward(50)










exitonclick()