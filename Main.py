#Turtle Project 
by Rashiem Kalif Bell

import turtle
turtle.color("blue")

def back (len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def move(len):
  back(-1 * len)
  
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360/ num)
    
def sprial(len, angle):
    for i in range(len, 5, -5):
      turtle.forward(i)
      turtle.right(angle)
    
sprial(75, 45)
move(150)
turtle.color("red")
sprial(150, 116)

# for n in range(3,10):
#   move(50) #forward
#   polygon(n, 100 / n)
#   back(50)
#   turtle.right(360/7)
