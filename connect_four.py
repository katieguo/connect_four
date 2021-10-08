import turtle

screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor("white")

turtle.speed(0)
turtle.hideturtle()

turtle.penup()
turtle.right(180)

# board
for i in range (9):
  turtle.goto(200,280-50*i)
  turtle.left(90)
  turtle.forward(50)
  turtle.right(90)
  for a in range (7):
    turtle.pendown()
    turtle.circle(20)
    turtle.penup()
    turtle.forward(65)

# num of spots per column full
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0

# player odd or even to det color
player = 0

# draw circle when screen clicked
def Four(x,y):
  global count1
  global count2
  global count3
  global count4
  global count5
  global count6
  global count7
  
  global player
  
  # add starting x values for each column to list
  backcolx = []
  for i in range (7):
    backcolx.append(200-i*65)
  colx = [0]
  for i in range (7):
    colx.append(backcolx[6-i])
  
  # add starting y values for each column to list
  backrowy = []
  for i in range (9):
    backrowy.append(280-((i+1)*50))
  rowy=[0]
  for i in range (9):
    rowy.append(backrowy[8-i])
  
  count=0
  
  # which column in
  if x <= colx[1]+33:
    column = 1
    count1+=1
    count = count1    # count is num row available in column
  elif x <= colx[2]+33:
    column = 2
    count2+=1
    count=count2
  elif x <= colx[3]+33:
    column = 3
    count3+=1
    count=count3
  elif x <= colx[4]+33:
    column = 4
    count4+=1
    count=count4
  elif x <= colx[5]+33:
    column = 5
    count5+=1
    count=count5
  elif x <= colx[6]+33:
    column = 6
    count6+=1
    count=count6
  elif x <= colx[7]+33:
    column = 7
    count7+=1
    count=count7

  # change player so color changes
  if player%2==0:
    color = "red"
    turtle.penup()
    turtle.goto(0,-240)
    turtle.color("white")
    turtle.write('red player\'s turn!', font = ('Times New Roman', 24), align='center')
    turtle.color("black")
    turtle.write('blue player\'s turn!', font = ('Times New Roman', 24), align='center')
  if player%2 == 1:
    color = "blue"
    turtle.penup()
    turtle.goto(0,-240)
    turtle.color("white")
    turtle.write('blue player\'s turn!', font = ('Times New Roman', 24), align='center')
    turtle.color("black")
    turtle.write('red player\'s turn!', font = ('Times New Roman', 24), align='center')
  
  # draw if column isn't full
  if count <=9:
    turtle.penup()
    turtle.goto(colx[column],rowy[count])
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    player+=1   # player color only changes if col not full

screen.onscreenclick(Four)
