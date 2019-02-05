#! /usr/bin/python

from Tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
# GPIO.setup(23, GPIO.OUT)
# GPIO.setup(22,GPIO.OUT)
pwmdc1 = GPIO.PWM(18, 500)
pwmdc1.start(100)
# pwmdc2 = GPIO.PWM(18, 500)
# pwmdc2.start(100)

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=100,
        orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)
    def update(self, duty):
        pwmdc1.ChangeDutyCycle(float(duty))
root = Tk()
root.wm_title('PWM Power Control')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()

# if GPIO.input(22) == 1:
#     GPIO.output(dc1Pin, GPIO.HIGH)
# else :
