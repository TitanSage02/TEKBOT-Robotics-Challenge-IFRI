import time
import threading
import RPi.GPIO as GPIO
import sys
import Adafruit_PCA9685

# Initialisation du module PCA9685 pour le contrôle des servos
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

# Paramètres initiaux des servos

#0 : gauche
#1 : droit 

servo_params = {
    0: {"init": 300, "max": 450, "min": 150, "pos": 300, "direction": 1},
    1: {"init": 300, "max": 480, "min": 160, "pos": 300, "direction": 1},
    2: {"init": 300, "max": 500, "min": 100, "pos": 300, "direction": 1},
    3: {"init": 300, "max": 500, "min": 300, "pos": 300, "direction": 1}
}

def ctrl_range(raw, max_genout, min_genout):
    """Contrôle la plage des valeurs pour éviter les dépassements."""
    if raw > max_genout:
        return max_genout
    elif raw < min_genout:
        return min_genout
    else:
        return raw

def move_servo(channel, speed, direction):
    """Fait bouger un servo dans une direction avec une vitesse donnée."""
    global pwm, servo_params

    if direction:
        #Inversion de la direction si nécessaire
        speed = -speed

    # Modification de la position du servo
    servo_params[channel]["pos"] = ctrl_range(speed, servo_params[channel]["max"], servo_params[channel]["min"])
    pwm.set_pwm(channel, 0, servo_params[channel]["pos"])

def servo_init():
    """Initialise les servos à leurs positions initiales."""
    global pwm, servo_params

    for channel, params in servo_params.items():
        pwm.set_pwm(channel, 0, params["pos"])

def clean_all():
    """Arrête proprement tous les servos."""
    global pwm
    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(50)
    pwm.set_all_pwm(0, 0)


try:
    # Initialise les servos
    servo_init()

    # Teste les servos en les déplaçant à différentes positions
    for i in range(5):
        move_servo(0, 400, 1)
        print("Déplace le servo 0 vers la position 400 avec une vitesse de 1")
        time.sleep(10)

        move_servo(1, 200, 1)
        print("Déplace le servo 1 vers la position 200 avec une vitesse de 1")
        time.sleep(10)

        move_servo(2, 300, 1) 
        print("Déplace le servo 2 vers la position 300 avec une vitesse de 1")
        time.sleep(10)

        move_servo(3, 250, 1) 
        print("Déplace le servo 3 vers la position 250 avec une vitesse de 1")
        time.sleep(10)

except KeyboardInterrupt:
    # Arrête proprement les servos en cas d'interruption par l'utilisateur
    clean_all()
