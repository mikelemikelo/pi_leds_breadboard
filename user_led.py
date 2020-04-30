import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)

sec = input('Numero de veces de parpadeo:\n')

print('Ok....')
time.sleep(1)

for i in range(int(sec)):
	GPIO.output(21,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(21,GPIO.LOW)
	time.sleep(1)
