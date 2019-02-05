#! /usr/bin/python3

import RPi.GPIO as GPIO
import os,time

# Set #17 as limit switch pin, #18 as dc1 pin, #27 as dc2 pin
lim11Pin = 17
lim12Pin = 17
lim21Pin =
lim22Pin =
dc1Pin = 12
dc2Pin = 27

# Define a function to print message at the beginning
def print_message():
	print ("========================================")
	print ("|              Limit Switch            |")
	print ("|      Middle pin of limit switch      |")
	print ("|         connect to gpio0;            |")
    print ("|    ------------------------------    |")
	print ("|                                      |")
	print ("|Limit switch to control PWM which DC  |")
	print ("|                                      |")
	print ("|                        CV. Robries   |")
	print ("========================================\n")
	print 'Program is running on /etc/rc.local/...'
	print 'Please press Ctrl+C to end the program...'
	input ("Press Enter to begin\n")

# Define a setup function for some setup
def setup():
	# Set the GPIO modes to BCM Numbering
	GPIO.setmode(GPIO.BCM)
	# Set limitPin input
	# Set dcPin output,
	# and initial level to High(3.3v)
	GPIO.setup(lim11Pin, GPIO.IN)
    GPIO.setup(lim12Pin, GPIO.IN)
    GPIO.setup(lim21Pin, GPIO.IN)
    GPIO.setup(lim22Pin, GPIO.IN)
	GPIO.setup(dc1Pin, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(dc2Pin, GPIO.OUT, initial=GPIO.HIGH)

# Define a main function for main process
def main():
	# Print messages
	print_message()
	while True:
		# limit switch high (logic high), dc1 on and fast pwm
		if GPIO.input(lim11Pin) == 1:
			print 'DC1 ON (High Value)'
			GPIO.output(dc1Pin, GPIO.HIGH)
			#GPIO.output(dc2Pin, GPIO.HIGH)
            #print pwm fast
        # limit switch low (logic low), dc1 on and low pwm
        elif GPIO.input(lim12Pin) == 1:
            print 'DC1 ON (Low Value)'
			#GPIO.output(dc1Pin, GPIO.HIGH)
			GPIO.output(dc2Pin, GPIO.HIGH)
            #print pwm low
        time.sleep(0.5)
		# limit switch low, dc2 on
		if GPIO.input(lim21Pin) == 1:
			print '    DC2 ON (High Value)'
			GPIO.output(dc2Pin, GPIO.LOW)
			GPIO.output(dc1Pin, GPIO.HIGH)
            #print pwm fast
            # limit switch low (logic low), dc1 on and low pwm
        elif GPIO.input(lim12Pin) == 1:
            print 'DC1 ON (Low Value)'
    		#GPIO.output(dc1Pin, GPIO.HIGH)
    		GPIO.output(dc2Pin, GPIO.HIGH)
            #print pwm low


# Define a destroy function for clean up everything after
# the script finished
def destroy():
	# Turn off motor DC
	GPIO.output(dc1Pin, GPIO.HIGH)
	GPIO.output(dc2Pin, GPIO.HIGH)
	# Release resource
	GPIO.cleanup()
# If run this script directly, do:
if __name__ == '__main__':
	setup()
	try:
		main()
	# When 'Ctrl+C' is pressed, the child program
	# destroy() will be  executed.
	except KeyboardInterrupt:
		destroy()
