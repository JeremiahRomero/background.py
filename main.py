import turtle as trtl

trtl.speed(10)

#wall

def draw_wall():
  trtl.penup()
  trtl.setposition(-320,-170)
  trtl.pendown()
  trtl.begin_fill()
  trtl.color("tan")
  trtl.left(20)
  trtl.forward(300)
  trtl.left(70)
  trtl.forward(250)
  trtl.backward(250)
  trtl.right(100)
  trtl.forward(365)
  trtl.left(100)
  trtl.forward(300)
  trtl.left(88)
  trtl.forward(360)
  trtl.left(5)
  trtl.forward(290)
  trtl.left(88)
  trtl.forward(340)
  trtl.end_fill()
draw_wall()

#floor

trtl.begin_fill()
trtl.color("grey")
trtl.left(89)
trtl.forward(643)
trtl.left(90)
trtl.forward(45)
trtl.left(80)
trtl.forward(365)
trtl.left(30)
trtl.forward(310)
trtl.left(160)
trtl.forward(650)
trtl.end_fill()

#fireplace

trtl.penup()
trtl.setposition(25,50)
trtl.pendown()
trtl.color("brown")

def draw_fireplace():
  trtl.begin_fill()
  trtl.right(5)
  trtl.forward(250)
  trtl.right(90)
  trtl.forward(150)
  trtl.right(95)
  trtl.forward(50)
  trtl.right(85)
  trtl.forward(105)
  trtl.left(88)
  trtl.forward(152)
  trtl.left(90)
  trtl.forward(95)
  trtl.right(95)
  trtl.forward(45)
  trtl.right(85)
  trtl.forward(130)
  trtl.end_fill()
draw_fireplace()

#carpet rug

trtl.penup()
trtl.setposition(-25,-100)
trtl.pendown()
trtl.color("red")

def draw_carpet():
  trtl.begin_fill()
  trtl.left(120)
  trtl.forward(190)
  trtl.backward(190)
  trtl.left(145)
  trtl.forward(240)
  trtl.right(140)
  trtl.forward(60)
  trtl.right(28)
  trtl.forward(368)
  trtl.end_fill()
draw_carpet()

