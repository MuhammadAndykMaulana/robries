#!/usr/bin/python3

from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from gpiozero import Button
from time import sleep

def print_message():
	print ("========================================")
	print ("|              Welcome                 |")
	print ("|      The main program PWM            |")
	print ("|    ------------------------------    |")
	print ("|  Limit switch to control PWM Motor   |")
	print ("|                                      |")
	print ("|                        CV. Robries   |")
	print ("========================================\n")
	print ('Program is running on /etc/rc.local/...')
	print ('Please press Ctrl+C to end the program...')
	input ("Press Enter to begin\n")

#Definisi Driver Motor
# Motor A, Left Side GPIO CONSTANTS
PWM_DRIVE_LEFT = 19		# ENA - H-Bridge enable pin
FORWARD_LEFT_PIN = 26	# IN1 - Forward Drive
REVERSE_LEFT_PIN = 21	# IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_DRIVE_RIGHT = 5		# ENB - H-Bridge enable pin
FORWARD_RIGHT_PIN = 6	# IN1 - Forward Drive
REVERSE_RIGHT_PIN = 13	# IN2 - Reverse Drive

# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)

# Initialise objects for H-Bridge digital GPIO pins
forwardLeft = PWMOutputDevice(FORWARD_LEFT_PIN)
reverseLeft = PWMOutputDevice(REVERSE_LEFT_PIN)
forwardRight = PWMOutputDevice(FORWARD_RIGHT_PIN)
reverseRight = PWMOutputDevice(REVERSE_RIGHT_PIN)

def allStop():
	forwardLeft.value = False
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = False
	driveLeft.value = 0
	driveRight.value = 0

def forwardDrive():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 1.0
	driveRight.value = 1.0

def reverseDrive():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 1.0
	driveRight.value = 1.0

def spinLeft():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 1
	driveLeft.value = 0.2
	driveRight.value = 1
	driveRight.value = 0.01

def SpinRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.1
	driveRight.value = 0.1

def forwardTurnLeft():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.2
	driveRight.value = 0.8

def forwardTurnRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.8
	driveRight.value = 0.2

def reverseTurnLeft():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.2
	driveRight.value = 0.8

def reverseTurnRight():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.8
	driveRight.value = 0.2

def main():
	# button = Button(18)
	# allStop()
	forwardDrive()
	sleep(10)
	reverseDrive()
	sleep(10)
	# spinLeft()
	# sleep(5)
	# while (button.wait_for_press()):
	# 	SpinRight()
	# 	sleep(5)
	# forwardTurnLeft()
	# sleep(10)
	# forwardTurnRight()
	# sleep(5)
	# reverseTurnLeft()
	# sleep(5)
	# reverseTurnRight()
	# sleep(5)


if __name__ == "__main__":
    print_message()
    try:
        main()
    except KeyboardInterrupt:
    	allStop()
