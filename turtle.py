import turtle

jobzz_turtle=turtle.Turtle()

#This is a square
def square():
  jobzz_turtle.forward(100)
  jobzz_turtle.right(90)
  jobzz_turtle.forward(100)
  jobzz_turtle.right(90)
  jobzz_turtle.forward(100)
  jobzz_turtle.right(90)
  jobzz_turtle.forward(100)
  
#This is a star
def star():
  for i in range(5):
    jobzz_turtle.forward(100)
    jobzz_turtle.right(144)
  

square()
jobzz_turtle.forward(100)
square()
jobzz_turtle.forward(100)
star()
