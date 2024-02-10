import turtle as t
import random as r
from time import *


coordinates = {1: [-250, 220], 2: [-50, 220], 3: [160, 220], 4: [-250, 63.34], 5: [-50, 63.34], 6: [160, 63.34],
               7: [-250, -93.34], 8: [-50, -93.34], 9: [160, -93.34]}
done_box = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
finished = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
turn = 0


# for "TIC"
def tic():
    t.pencolor('red')
    t.hideturtle()
    t.speed(100)
    t.pensize(20)
    t.penup()
    t.setpos((-300, 200))
    t.pendown()
    t.speed(0)
    t.forward(76)
    t.setpos((-262, 200))
    t.right(90)
    t.forward(76)
    t.penup()
    t.setpos((-180, 200))
    t.pendown()
    t.forward(76)
    t.penup()
    t.setpos((-90, 200))
    t.pendown()
    t.right(90)
    t.circle(37, 180)


# for "TAC"
def tac():
    t.pencolor('yellow')
    t.penup()
    t.goto(-170, 60)
    t.pendown()
    t.forward(76)
    t.goto(-132, 60)
    t.right(90)
    t.forward(76)
    t.penup()
    t.goto(-70, -16)
    t.pendown()
    t.left(156)
    t.forward(85)
    t.right(132)
    t.forward(85)
    t.back(24)
    t.left(66)
    t.back(40)
    t.penup()
    t.goto(70, 60)
    t.pendown()
    t.right(180)
    t.circle(36, 190)


# for "TOE"
def toe():
    t.pencolor('white')
    t.setheading(0)
    t.penup()
    t.goto(-40, -80)
    t.pendown()
    t.forward(76)
    t.back(38)
    t.right(90)
    t.forward(76)
    t.penup()
    t.goto(70, -120)
    t.pendown()
    t.circle(40)
    t.penup()
    t.right(90)
    t.goto(200, -80)
    t.setheading(90)
    t.pendown()
    t.back(76)
    t.penup()
    t.goto(200, -80)
    t.setheading(0)
    t.pendown()
    t.forward(50)
    t.back(50)
    t.right(90)
    t.forward(38)
    t.left(90)
    t.forward(50)
    t.back(50)
    t.right(90)
    t.forward(38)
    t.left(90)
    t.forward(50)


# TO START TEXT
def start_text():
    t.penup()
    t.pencolor('blue')
    t.goto(-210, -245)
    t.pendown()
    t.write('PRESS SPACE TO START', font=('Verdana', 25, 'normal'))


# TO START GAME
def start_game():
    t.reset()
    t.pencolor('white')
    t.pensize(10)
    p_1 = t.textinput('PLAYER 1 ', 'Name')
    p_2 = t.textinput('PLAYER 2 ', 'Name')
    p_1 = p_1.upper()
    p_2 = p_2.upper()
    choice = r.randint(0, 1)
    t.hideturtle()
    t.penup()
    t.goto(-350, 250)
    t.pendown()
    if choice == 0:
        t.write('{0} USES X'.format(p_1), font=('Verdana', 24, 'normal'))
        t.penup()
        t.goto(-350, 210)
        t.pendown()
        t.write('{0} USES O'.format(p_2), font=('Verdana', 24, 'normal'))
    else:
        t.write('{0} USES X'.format(p_2), font=('Verdana', 24, 'normal'))
        t.penup()
        t.goto(-350, 210)
        t.pendown()
        t.write('{0} USES O'.format(p_1), font=('Verdana', 24, 'normal'))
    sleep(3)
    box()


# FOR THE STRUCTURE OF GAME
def box():
    t.reset()
    t.pencolor('white')
    t.penup()
    t.goto(-300, 250)
    t.pensize(10)
    t.pendown()
    t.speed(10)
    for i in range(4):
        if i % 2 == 0:
            t.forward(600)
        else:
            t.forward(470)
        t.right(90)
    for j in range(2):
        t.right(90)
        t.forward(156.66)
        t.left(90)
        t.forward(600)
        t.back(600)
    t.right(90)
    t.forward(156.66)
    t.left(90)
    for k in range(3):
        t.forward(200)
        t.left(90)
        t.forward(470)
        t.back(470)
        t.right(90)
    t.hideturtle()
    cl.onclick(click, btn=1)


# for clicks on box
def click(x1, y1):
    global x, y, k, turn
    if -300 <= x1 <= -100 and 93.34 <= y1 <= 250:
        x, y = coordinates[1][0], coordinates[1][1]
        done_box[1] += 1
        k = 1

    elif -100 <= x1 <= 100 and 93.34 <= y1 <= 250:
        x, y = coordinates[2][0], coordinates[2][1]
        k = 2
        done_box[2] += 1

    elif 100 <= x1 <= 300 and 93.34 <= y1 <= 250:
        x, y = coordinates[3][0], coordinates[3][1]
        done_box[3] += 1
        k = 3

    elif -300 <= x1 <= -100 and -63.32 <= y1 <= 93.34:
        x, y = coordinates[4][0], coordinates[4][1]
        done_box[4] += 1
        k = 4

    elif -100 <= x1 <= 100 and -63.32 <= y1 <= 93.34:
        x, y = coordinates[5][0], coordinates[5][1]
        done_box[5] += 1
        k = 5

    elif 100 <= x1 <= 300 and -63.32 <= y1 <= 93.34:
        x, y = coordinates[6][0], coordinates[6][1]
        done_box[6] += 1
        k = 6

    elif -300 <= x1 <= -100 and -220 <= y1 <= -63.32:
        x, y = coordinates[7][0], coordinates[7][1]
        done_box[7] += 1
        k = 7

    elif -100 <= x1 <= 100 and -220 <= y1 <= -63.32:
        x, y = coordinates[8][0], coordinates[8][1]
        done_box[8] += 1
        k = 8

    elif 100 <= x1 <= 300 and -220 <= y1 <= -63.32:
        x, y = coordinates[9][0], coordinates[9][1]
        done_box[9] += 1
        k = 9
    else:
        pass
    turn += 1
    draw(x, y)


# for drawing on box
def draw(x2, y2):
    t.penup()
    t.speed(0)
    t.pencolor('white')
    t.goto(x2, y2)
    if turn % 2 == 0:
        o_point(x2, y2)
    else:
        x_point()


# draw X
def x_point():
    if done_box[k] != 1 or finished[k] == 1 or finished[k] == 2:
        return
    t.color('red')
    t.setheading(0)
    t.pendown()
    t.right(40)
    t.forward(120)
    t.back(60)
    t.left(80)
    t.forward(60)
    t.back(120)
    finished[k] = 1
    end()


# draw O
def o_point(x1, y1):
    if done_box[k] != 1 or finished[k] == 1 or finished[k] == 2:
        return
    t.pencolor('yellow')
    t.speed(10)
    t.setheading(0)
    t.goto(x1 + 45, y1 - 98.33)
    t.pendown()
    sleep(0.5)
    t.circle(50, 360)
    sleep(0.5)
    finished[k] = 2
    end()


# ending game
def end():
    for i in range(1, 10, 3):
        check_rows_x = finished[i] == 1 and finished[i + 1] == 1 and finished[i + 2] == 1
        check2_rows_o = finished[i] == 2 and finished[i + 1] == 2 and finished[i + 2] == 2
        if check_rows_x:
            finish('x')
        elif check2_rows_o:
            finish('o')
    for i in range(1, 4):
        check2_cols_x = finished[i] == 1 and finished[i + 3] == 1 and finished[i + 6] == 1
        check2_cols_o = finished[i] == 2 and finished[i + 3] == 2 and finished[i + 6] == 2
        if check2_cols_x:
            finish('x')
        elif check2_cols_o:
            finish('o')
    for i in range(1, 4, 2):
        if i == 1:
            check_diag_x = finished[i] == 1 and finished[i + 4] == 1 and finished[i + 8] == 1
            check_diag_o = finished[i] == 2 and finished[i + 4] == 2 and finished[i + 8] == 2
            if check_diag_x:
                finish('x')
            elif check_diag_o:
                finish('o')
        else:
            check_diag_x1 = finished[i] == 1 and finished[i + 2] == 1 and finished[i + 4] == 1
            check_diag_o1 = finished[i] == 2 and finished[i + 2] == 2 and finished[i + 4] == 2
            if check_diag_x1:
                finish('x')
            elif check_diag_o1:
                finish('o')


# finisher
def finish(winner):
    sleep(0.5)
    t.reset()
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    t.pencolor('white')
    t.hideturtle()
    if winner == 'x':
        t.write('X WON !', font=('Verdana', 60, 'normal'))
    else:
        t.write('O WON !', font=('Verdana', 60, 'normal'))
    sleep(1)


# MAIN
t.bgcolor('black')
tic()
tac()
toe()
start_text()
t.onkey(start_game, "space")
t.listen()
cl = t.Screen()
t.mainloop()
