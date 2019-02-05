# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18,GPIO.IN)
# #
# prev_input = 1
# # print input
# while True:
#   input = GPIO.input(18)
#   if ((not prev_input) and input):
#     print("Button Pressed")
#   prev_input = input
#   #slight pause to debounce
#   time.sleep(0.05)
# print "ok"
import time
from gpiozero import Button
from signal import pause

#led = LED(17)
prev_input = 1
while 1:
    button = Button(18)
    if ((not prev_input) and button.wait_for_press()):
        print("Button Pressed")
    prev_input = button
    # else:
    #     print("tombol tidak ditekan!")
    time.sleep(0.05)
    # pause()
# GPIO.cleanup()

# from gpiozero import Button
#
# button = Button(18)
# button.wait_for_press()
# print("The button was pressed!")
