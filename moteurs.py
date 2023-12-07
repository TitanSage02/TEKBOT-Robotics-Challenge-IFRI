# a revoir

        
        
        
import time
import RPi.GPIO as GPIO

Motor_A_pin = 4
Motor_B_pin = 17

Motor_A_pin1 = 14
Motor_A_pin2 = 15
Motor_B_pin1 = 27
Motor_B_pin2 = 18

Dir_forward = 0
Dir_backward = 1


def motorStop():
    GPIO.output(Motor_A_pin1, GPIO.LOW)
    GPIO.output(Motor_A_pin2, GPIO.LOW)
    GPIO.output(Motor_B_pin1, GPIO.LOW)
    GPIO.output(Motor_B_pin2, GPIO.LOW)
    GPIO.output(Motor_A_pin, GPIO.LOW)
    GPIO.output(Motor_B_pin, GPIO.LOW)

def setup():
    global pwm_A, pwm_B
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor_A_pin, GPIO.OUT)
    GPIO.setup(Motor_B_pin, GPIO.OUT)
    GPIO.setup(Motor_A_pin1, GPIO.OUT)
    GPIO.setup(Motor_A_pin2, GPIO.OUT)
    GPIO.setup(Motor_B_pin1, GPIO.OUT)
    GPIO.setup(Motor_B_pin2, GPIO.OUT)

    motorStop()
    try:
        pwm_A = GPIO.PWM(Motor_A_pin, 1000)
        pwm_B = GPIO.PWM(Motor_B_pin, 1000)
    except:
        pass

def motor_A(status, direction, speed):
    global pwm_A
    if status == 'pause':
        GPIO.output(Motor_A_pin, GPIO.LOW)
        GPIO.output(Motor_A_pin1, GPIO.LOW)
        GPIO.output(Motor_A_pin2, GPIO.LOW)
    else:
        if direction == 'devant':
            GPIO.output(Motor_A_pin1, GPIO.HIGH)
            GPIO.output(Motor_A_pin2, GPIO.LOW)
            pwm_A.start(100)
            pwm_A.ChangeDutyCycle(speed)
        elif direction == 'derriere':
            GPIO.output(Motor_A_pin1, GPIO.LOW)
            GPIO.output(Motor_A_pin2, GPIO.HIGH)
            pwm_A.start(0)
            pwm_A.ChangeDutyCycle(speed)

def motor_B(status, direction, speed):
    global pwm_B
    if status == 'pause':
        GPIO.output(Motor_B_pin, GPIO.LOW)
        GPIO.output(Motor_B_pin1, GPIO.LOW)
        GPIO.output(Motor_B_pin2, GPIO.LOW)
    else:
        if direction == 'devant':
            GPIO.output(Motor_B_pin1, GPIO.HIGH)
            GPIO.output(Motor_B_pin2, GPIO.LOW)
            pwm_B.start(100)
            pwm_B.ChangeDutyCycle(speed)
        elif direction == 'derriere':
            GPIO.output(Motor_B_pin1, GPIO.LOW)
            GPIO.output(Motor_B_pin2, GPIO.HIGH)
            pwm_B.start(0)
            pwm_B.ChangeDutyCycle(speed)

def conduite(direction, cote, vitesse):
    if direction == 'devant':
        if cote == 'droit':
            motor_A('pause', 'devant', vitesse)
            motor_B('nopause', 'devant', int(vitesse * 0.9))
        elif cote == 'gauche':
            motor_A('nopause', 'devant', int(vitesse * 0.9))
            motor_B('pause', 'devant', vitesse)
        else:
            motor_A('nopause', 'devant', vitesse)
            motor_B('nopause', 'devant', vitesse)
    elif direction == 'derriere':
        if cote == 'droit':
            motor_A('pause', 'derriere', int(vitesse * 0.9))
            motor_B('nopause', 'derriere', vitesse)
        elif cote == 'gauche':
            motor_A('nopause', 'derriere', vitesse)
            motor_B('pause', 'derriere', int(vitesse * 0.9))
        else:
            motor_A('nopause', 'derriere', vitesse)
            motor_B('nopause', 'derriere', vitesse)
    elif direction == 'no':
        if cote == 'droit':
            motor_A('nopause', 'devant', vitesse)
            motor_B('nopause', 'arriere', vitesse)
        elif cote == 'gauche':
            motor_A('nopause', 'derriere', vitesse)
            motor_B('nopause', 'devant', vitesse)
        else:
            motorStop()
    else:
        pass

def destroy():
    motorStop()
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        vitesse = 60.0
        setup()
        conduite('devant', 'no', vitesse) # avance uniquement devant
        time.sleep(5)
        conduite('devant', 'droit', vitesse) # avance et tourne
        time.sleep(5)
        conduite('no', 'gauche', vitesse) # fais un toure sur lui meme du coté gauche
        time.sleep(5)
        motorStop()
        destroy()
    except KeyboardInterrupt:
        destroy()
