#Ce code a été testé sur le robot et validé 

import RPi.GPIO as GPIO
import time

Tr = 11 
Ec = 8

def setup_ultrasonic():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Tr, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Ec, GPIO.IN)

def checkdist():
    GPIO.output(Tr, GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(Tr, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Tr, GPIO.LOW)

    while not GPIO.input(Ec):
        pass
    t1 = time.time()

    while GPIO.input(Ec):
        pass
    t2 = time.time()

    dist = (t2 - t1) * 340 / 2

    return dist

    


try:
    setup_ultrasonic()
    while True:
        distance = checkdist()
        print(f"{distance:.2f} cm")
        time.sleep(1)
finally:
        GPIO.cleanup()
