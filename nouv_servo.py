from gpiozero import Servo
from time import sleep
# definitions des broches
bras_servo_pin = 13
pince_servo_pin = 15

bras_servo = Servo(bras_servo_pin)
pince_servo = Servo(pince_servo_pin)
def lever_bras():
    print("lever bras")
    bras_servo.value = 0.5
    sleep(1)
    bras_servo.value=0.0
def baisser_bras():
    print('baisser')
    bras_servo.value = - 0.5
    sleep(1)
    bras_servo.value=0.0
def prendre_boite():
    print('prendre')
    pince_servo.value = -1.0
    sleep(1)
    pince_servo.value = 0.0
def deposer_boite():
    print('deposer')
    pince_servo.value=1.0
    sleep(1)
    pince_servo.value = 0.0
try :
    lever_bras()
    sleep(2)
    baisser_bras()
    sleep(2)
    prendre_boite()
    sleep(2)
    deposer_boite()
    sleep(2)
except :
    pass
finally:
    bras_servo.value = 0.0
    pince_servo.value = 0.0



