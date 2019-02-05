#Import modul time
import time
#Import modul RPi.GPIO
import RPi.GPIO as GPIO

enmotor1=21
majumotor1 = 26	# IN1 - Forward Drive
reversemotor1 = 19	# IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
enmotor2=5
majumotor2 = 13	# IN1 - Forward Drive
reversemotor2 = 6	# IN2 - Reverse Drive

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

#Setup Pin PWM
def setup():
    #Set penomeran pin dengan standar Broadcom
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(enmotor1, GPIO.OUT)
    GPIO.setup(enmotor2, GPIO.OUT)

# #Setup Pin kontrol maju mundur
# GPIO.setup(26, GPIO.OUT)
# GPIO.setup(19, GPIO.OUT)

#Maju
def maju():
    GPIO.output(26, GPIO.HIGH)
    GPIO.output(19, GPIO.LOW)

#Mundur
def mundur():
    GPIO.output(26, GPIO.LOW)
    GPIO.output(19, GPIO.HIGH)

def stop():
    GPIO.output(enmotor1, GPIO.LOW)
    GPIO.output(enmotor2, GPIO.LOW)

#Buat instansiasi pin PWM, jika menggunakan dua motor
#namannya bisa diubah menjadi p1 atau p2, bisa juga motor1 dan motor2
p1 = GPIO.PWM(enmotor1, 50)
p2 = GPIO.PWM(enmotor2, 50)

#Lakukan perulangan dengan menaikan dan menurunkan nilai PWM motor
#sehingga motor bergerak bertambah cepat lalu melambat dan seterusnya
def main():
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
        p1.stop()
        p2.stop()
        #Reset gpio dan keluar dari program
        GPIO.cleanup()
if __name__ == "__main__":
    print_message()
    try:
        main()
    except KeyboardInterrupt:
        #Stop penggunaan pwm
        p1.stop()
        p2.stop()
        #Reset gpio dan keluar dari program
        GPIO.cleanup()
