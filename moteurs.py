# a revoir
import time
import RPi.GPIO as GPIO

Motor_A_pin = 4
Motor_B_pin = 17

Motor_A_pin1 = 14
Motor_A_pin2 = 15

Motor_B_pin1 = 27   
Motor_B_pin2 = 18

def motorStop():
    GPIO.output(Motor_A_pin1, GPIO.LOW)
    GPIO.output(Motor_B_pin1, GPIO.LOW)
    
    GPIO.output(Motor_A_pin2, GPIO.LOW)
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
            GPIO.output(Motor_A_pin1, GPIO.LOW)
            GPIO.output(Motor_A_pin2, GPIO.HIGH)
            pwm_A.start(100)
            pwm_A.ChangeDutyCycle(speed)
        elif direction == 'derriere':
            GPIO.output(Motor_A_pin1, GPIO.HIGH)
            GPIO.output(Motor_A_pin2, GPIO.LOW)
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
            motor_A('pause', 'devant', vitesse * 0.88) #Les 0.88 sont là pour équilibrer le fait que l'une des chaines est plus molle donc ralentit le robot
            motor_B('nopause', 'devant',vitesse)
        elif cote == 'gauche':
            motor_A('nopause', 'devant', vitesse * 0.88)
            motor_B('pause', 'devant', vitesse)
        else:
            motor_A('nopause', 'devant', vitesse * 0.88)
            motor_B('nopause', 'devant', vitesse)
    elif direction == 'derriere':
        if cote == 'droit':
            motor_A('pause', 'derriere', vitesse * 0.88)
            motor_B('nopause', 'derriere', vitesse)
        elif cote == 'gauche':
            motor_A('nopause', 'derriere', vitesse * 0.88)
            motor_B('pause', 'derriere', vitesse)
        else:
            motor_A('nopause', 'derriere', vitesse * 0.88)
            motor_B('nopause', 'derriere', vitesse)
    elif direction == 'no':
        if cote == 'gauche':
            motor_A('nopause', 'devant', vitesse * 0.88)
            motor_B('nopause', 'arriere', vitesse)
        elif cote == 'droit':
            motor_A('nopause', 'derriere', vitesse * 0.88)
            motor_B('nopause', 'devant', vitesse)
        else:
            motorStop()
    else:
        pass

def destroy():
    GPIO.cleanup()


class Moteurs:
    def __init__(self):
        setup()


    def avancer(self, vitesse):
        conduite('devant', 'no', vitesse)

        
    def tourner_droite(self, vitesse):
        conduite('no', 'droit', vitesse)


    def tourner_gauche(self, vitesse):
        conduite('no', 'gauche', vitesse)

    
    def reculer_droite(self, vitesse):
        # Je dois identifier le moteur gauche et le moteur droit
        conduite('derriere', 'droit', vitesse)
        
    
    def reculer_gauche(self, vitesse):
        conduite('derriere', 'gauche', vitesse)

    
    def stop(self):
        motorStop()


if __name__ == '__main__':
    try:
        vitesse = 50 
        robot = Moteurs()
        #time.sleep(4) 
        #robot.stop()
        #robot.tourner_droite(vitesse)
        #time.sleep(4)
        #robot.reculer(vitesse)
        #time.sleep(4)
        #robot.stop()
        #time.sleep(4) 
        #robot.tourner_gauche(vitesse)
        while True:
            robot.avancer(vitesse)
    except KeyboardInterrupt:
        destroy()
