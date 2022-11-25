from tkinter import *
import time


window= Tk()
window.title('Alien')

c = Canvas(window, height =300, width = 400)
c.pack()

#create_oval(top left x-r, top left y-r,bottom right x+r, bottom right y+r, fill= 'color')
body = c.create_oval(100, 150, 300, 250, fill = 'green')
eye = c.create_oval(170, 70, 230, 130, outline = 'red', fill = 'white')
eyeball = c.create_oval(190, 90, 210, 110, fill = 'black')
mouth = c.create_oval(150, 220, 250, 240, fill = 'red')
neck = c.create_line(200, 150, 200, 130)
hat = c.create_polygon(180, 75, 220, 75, 200, 20, fill = 'blue')


def eye_control(event):
    key=event.keysym
    if key == 'Left':
        c.move(eyeball, -1, 0)
    elif key == 'Right':
        c.move(eyeball, 1, 0)
    elif key == 'Up':
        c.move(eyeball, 0, -1)
    elif key == 'Down':
        c.move(eyeball, 0, 1)
c.bind_all('<Key>',eye_control)




#itemconfig lets you change properties of shapes
def mouth_open(event):
    c.itemconfig(mouth, fill = 'black')
c.bind_all('<KeyPress-o>',mouth_open)


def mouth_burp():
    c.itemconfig(mouth, fill = 'black')
    c.itemconfig(words, text='Burpppp!')
    window.update()
    
    c.itemconfig(mouth, fill = 'red')
    
def mouth_burp_c():
    c.itemconfig(mouth, fill = 'red')


def mouth_close(event):
    c.itemconfig(mouth, fill = 'red')
c.bind_all('<KeyPress-c>',mouth_close)

words = c.create_text(200, 280, text='')
#window.attributes('-topmost',1)
def burp(event):
    mouth_burp()
    time.sleep(.5)
    c.itemconfig(words, text='')
c.bind_all('<Button-1>',burp)


def close_eye():
    c.itemconfig(eye, fill='green')
    c.itemconfig(eyeball, state=HIDDEN)
    window.update()
    
def open_eye():
    c.itemconfig(eye, fill='white')
    c.itemconfig(eyeball, state=NORMAL)


def blink(event):
    close_eye()
    time.sleep(.5)
    open_eye()
c.bind_all('<KeyPress-a>',blink)
    




window.mainloop()
