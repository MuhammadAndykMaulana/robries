import time
#Import modul RPi.GPIO
import RPi.GPIO as GPIO

#Set penomeran pin dengan standar Broadcom
GPIO.setmode(GPIO.BCM)
#Setup Pin PWM
GPIO.setup(18, GPIO.OUT)
#Setup Pin kontrol maju mundur
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
#
# #Maju
# GPIO.output(23, GPIO.HIGH)
# GPIO.output(24, GPIO.LOW)
#
# #Mundur
# GPIO.output(23, GPIO.LOW)
# GPIO.output(24, GPIO.HIGH)
#
# #Buat instansiasi pin PWM, jika menggunakan dua motor
# #namannya bisa diubah menjadi p1 atau p2, bisa juga motor1 dan motor2
# p = GPIO.PWM(18, 50)
#
# #Lakukan perulangan dengan menaikan dan menurunkan nilai PWM motor
# #sehingga motor bergerak bertambah cepat lalu melambat dan seterusnya
# try:
#     p.start(50)
#     while 1:
#         for dc in range(0, 101, 5):
#             #Perintah untuk mengubah kecepatan motor, dc bisa bernilai 0 - 100
#             p.ChangeDutyCycle(dc)
#             time.sleep(0.1)
#         for dc in range(100, -1, -5):
#             p.ChangeDutyCycle(dc)
#             time.sleep(0.1)
#
# except KeyboardInterrupt:
#     #Stop penggunaan pwm
#     p.stop()
#     #Reset gpio dan keluar dari program
#     GPIO.cleanup()
#! /usr/bin/python3

import RPi.GPIO as GPIO
import time

enable_pin = 18
in1_pin = 23
in2_pin =24
GPIO.setmode(GPIO.BCM)
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)
pwm = GPIO.PWM(enable_pin, 500)
pwm.start(0)

def cw():
    GPIO.output(in1_pin, True)
    GPIO.output(in2_pin, False)

def ccw():
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin, True)

while True:
    try:
        cmd = input("Command, f/r 0..9, E.g. f5 :")
        print (cmd)
        direction = cmd[0]
        if direction == "f":
            cw()
        else:
            ccw()
        speed = int(cmd[1]) * 10
        pwm.ChangeDutyCycle(speed)
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        print("Keyboard interrupt")
    finally:
        GPIO.cleanup()
        pwm.stop()

"""
#Import modul time
import time
#Import modul RPi.GPIO
import RPi.GPIO as GPIO

#Set penomeran pin dengan standar Broadcom
GPIO.setmode(GPIO.BCM)
#Setup Pin PWM
GPIO.setup(25, GPIO.OUT)
#Setup Pin kontrol maju mundur
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

#Maju
GPIO.output(22, GPIO.HIGH)
GPIO.output(27, GPIO.LOW)

#Mundur
#GPIO.output(22, GPIO.LOW)
#GPIO.output(27, GPIO.HIGH)

#Buat instansiasi pin PWM, jika menggunakan dua motor
#namannya bisa diubah menjadi p1 atau p2, bisa juga motor1 dan motor2
p = GPIO.PWM(25, 50)

#Lakukan perulangan dengan menaikan dan menurunkan nilai PWM motor
#sehingga motor bergerak bertambah cepat lalu melambat dan seterusnya
try:
    p.start(50)
    while 1:
        for dc in range(0, 101, 5):
            #Perintah untuk mengubah kecepatan motor, dc bisa bernilai 0 - 100
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)

except KeyboardInterrupt:
    #Stop penggunaan pwm
    p.stop()
    #Reset gpio dan keluar dari program
    GPIO.cleanup()
"""
