import turtle
import time
import datetime as dt

def draw_dot(t:turtle.Turtle,x:int,y:int):
    tp(t,x,y+15)
    t.goto(x-5,y+10)
    t.goto(x,y+5)
    t.goto(x+5, y+10)
    t.goto(x,y+15)
    
    tp(t,x,y-15)
    t.goto(x-5,y-10)
    t.goto(x,y-5)
    t.goto(x+5, y-10)
    t.goto(x,y-15)
    
def draw_vsegment(t:turtle.Turtle,x:int,y:int):
    tp(t,x,y+23)
    t.goto(x+3,y+20)
    t.goto(x+3,y-20)
    t.goto(x,y-23)
    t.goto(x-3,y-20)
    t.goto(x-3,y+20)
    t.goto(x,y+23)

def draw_hsegment(t:turtle.Turtle, x:int, y:int):
    tp(t,x+23,y)
    t.goto(x+20,y+3)
    t.goto(x-20,y+3)
    t.goto(x-23,y)
    t.goto(x-20,y-3)
    t.goto(x+20,y-3)
    t.goto(x+23,y)
        
def draw_num(t,x,y,num):
    if num == "1":
        draw_vsegment(t,x+25,25)
        draw_vsegment(t,x+25,-25)
    elif num == "2":
        draw_vsegment(t,x+25,25)
        draw_vsegment(t,x-25,-25)
        draw_hsegment(t,x,50)
        draw_hsegment(t,x,0)
        draw_hsegment(t,x,-50)
    elif num == "3":
        draw_vsegment(t,x+25,25)
        draw_vsegment(t,x+25,-25)
        draw_hsegment(t,x,50)
        draw_hsegment(t,x,0)
        draw_hsegment(t,x,-50)
    elif num == "4":
        draw_vsegment(t,x-25,25)
        draw_vsegment(t,x+25,25)
        draw_vsegment(t,x+25,-25)
        draw_hsegment(t,x,0)
    elif num == "5":
        draw_vsegment(t,x-25,25)
        draw_vsegment(t,x+25,-25)
        draw_hsegment(t,x,50)
        draw_hsegment(t,x,0)
        draw_hsegment(t,x,-50)
    elif num == "6":
        draw_vsegment(t,x-25,25)
        draw_vsegment(t,x+25,-25)
        draw_vsegment(t,x-25,-25)
        draw_hsegment(t,x,50)
        draw_hsegment(t,x,0)
        draw_hsegment(t,x,-50)
    elif num == "7":
        draw_vsegment(t,x+25,25)
        draw_vsegment(t,x+25,-25)
        draw_hsegment(t,x,50)
    elif num == "8":
        draw_vsegment(t,x+25,25)
        draw_vsegment(t,x+25,-25)
        draw_vsegment(t,x-25,25)
        draw_vsegment(t,x-25,-25)
        draw_hsegment(t,x,50)
        draw_hsegment(t,x,0)
        draw_hsegment(t,x,-50)
    elif num == "9":
        draw_vsegment(t,x+25,25)
        draw_vsegment(t,x+25,-25)
        draw_vsegment(t,x-25,25)
        draw_hsegment(t,x,50)
        draw_hsegment(t,x,0)
        draw_hsegment(t,x,-50)
    elif num == "0":
        draw_vsegment(t,x+25,25)
        draw_vsegment(t,x+25,-25)
        draw_vsegment(t,x-25,25)
        draw_vsegment(t,x-25,-25)
        draw_hsegment(t,x,50)
        draw_hsegment(t,x,-50)
        

def draw_time(t,time, x):
    t.clear()
    if time < 10:
        time = "0"+str(time)
    else:
        time = str(time)
    draw_num(t,x-35,0,time[0])
    draw_num(t,x+35,0,time[1])
    
def tp(t:turtle.Turtle,x:int,y:int):
    t.up()
    t.goto(x,y)
    t.down()

t = turtle.Turtle()
t.pensize(2)
t.hideturtle()
t.color("red")
t.fillcolor("black")
t.speed(0)

s = turtle.Screen()
s.bgcolor("lightgreen")
s.setup(600, 600) 

t_sec = t.clone()
t_min = t.clone()
t_hr = t.clone()
p_sec, p_min, p_hr = [0,0,0]
draw_dot(t,-80,0)
draw_dot(t,80,0)
while True:
    sec = dt.datetime.now().second
    if sec != p_sec:
        p_sec = sec
        draw_time(t_sec, sec, 160)
    
    mn = dt.datetime.now().minute
    if mn != p_min:
        p_min = mn
        draw_time(t_min, mn, 0)
    
    hr = dt.datetime.now().hour
    if hr != p_hr:
        p_hr = hr
        draw_time(t_hr, hr, -160)
    time.sleep(0.5)
    