#Ce code a été testé sur le robot et validé 
import RPi.GPIO as GPIO
import time

class Ultrason:
    global Tr, Ec 
    Tr = 11 
    Ec = 8

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Tr, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(Ec, GPIO.IN)
    
    @staticmethod
    def checkdist():
        "Retourne en cm la distance qui sépare le robot de l'obstacle le plus proche"
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(Ec, GPIO.IN)
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
            
        return ( (t2-t1) * 340/2 ) * 100

    
if __name__ == '__main__':   
    try:
        ultrasons  = Ultrason()
        while True:
            distance = ultrasons.checkdist()
            print(f"{distance:.2f} cm")
            time.sleep(0.1)
    finally:
        GPIO.cleanup()
        