import time
import RPi.GPIO as GPIO

line_pin_right = 19
line_pin_middle = 16
line_pin_left = 20

motor_pin_left = 21
motor_pin_right = 26


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(line_pin_right, GPIO.IN)
    GPIO.setup(line_pin_middle, GPIO.IN)
    GPIO.setup(line_pin_left, GPIO.IN)
    GPIO.setup(motor_pin_left, GPIO.OUT)
    GPIO.setup(motor_pin_right, GPIO.OUT)

def run():
    status_right = GPIO.input(line_pin_right)
    status_middle = GPIO.input(line_pin_middle)
    status_left = GPIO.input(line_pin_left)

    print('LF3: %d   LF2: %d   LF1: %d\n' % (status_right, status_middle, status_left))

    # Logique de contrôle des moteurs en fonction des états des capteurs de ligne
    if status_right == 1 and status_middle == 0 and status_left == 1:
        # Avancer
        GPIO.output(motor_pin_left, GPIO.HIGH)
        GPIO.output(motor_pin_right, GPIO.HIGH)
    elif status_right == 0 and status_middle == 1 and status_left == 0:
        # Tourner à gauche
        GPIO.output(motor_pin_left, GPIO.LOW)
        GPIO.output(motor_pin_right, GPIO.HIGH)
    elif status_right == 1 and status_middle == 1 and status_left == 0:
        # Tourner à droite
        GPIO.output(motor_pin_left, GPIO.HIGH)
        GPIO.output(motor_pin_right, GPIO.LOW)
    else:
        # Arrêt
        GPIO.output(motor_pin_left, GPIO.LOW)
        GPIO.output(motor_pin_right, GPIO.LOW)

    time.sleep(0.2)

try:
    setup()
    while True:
            run()
except KeyboardInterrupt:
    GPIO.cleanup()
