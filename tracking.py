import RPi.GPIO as GPIO

class Tracking:
    global line_pin_right, line_pin_middle, line_pin_left
    
    line_pin_right = 19
    line_pin_middle = 16
    line_pin_left = 20

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(line_pin_right, GPIO.IN)
        GPIO.setup(line_pin_middle, GPIO.IN)
        GPIO.setup(line_pin_left, GPIO.IN)
    
    def etat(self):
        "Retourne un dictionnaire renseignant l'état des capteurs"
        status_right = GPIO.input(line_pin_right)
        status_middle = GPIO.input(line_pin_middle)
        status_left = GPIO.input(line_pin_left)
        status = {"droit": status_right, "milieu" : status_middle, "gauche" : status_left}
        return status

if __name__== '__main__':
    try : 
        track = Tracking()
        while True:
            status = track.etat()
            print(status)
    except:
        GPIO.cleanup()