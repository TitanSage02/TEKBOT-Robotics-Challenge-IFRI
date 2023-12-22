from autopilote import AutoPilot
from ultrason import Ultrason
from picamera import PiCamera
from modele import Model
from servo import Servo
from led import LED
import threading
import time


led = LED()
ia = Model()
ultra = Ultrason()
camera = PiCamera()
robot = AutoPilot()
bras_robotique = Servo()


def change_main_flag_to(value: bool):
    "Arrête le robot et arrête tous les flux"
    
    global main_flag, robot, led
    main_flag = value
    
    if not main_flag:
        "Arrêt de tous les threads"
        led.define_flag = False
        robot.define_flag = False
        bras_robotique.define_flag = False
        robot.thread.join()
        bras_robotique.join()

    
def main():
    
    robot.demarrer()

    while main_flag: 
        #print(ultra.checkdist())
        
        if ultra.checkdist() <= 50 :
            #C'est ici on va gérer le thread de la caméra
            capture = camera.capture("photo.jpg")
            position_poubelle, couleur_poubelle = ia.predict(capture)
            
            if  ultra.checkdist() <= 10:                                    # On arrête le robot à 10cm du déchet
                
                robot.define_droit = False                                  # On arrête l'autopilote
                print("====================================INFOS====================================")
                print("Arrêt des moteurs")
                print("Déchet détecté")
                
                print("Démarrage du processus")
                
                t1 = time.time()

                print("Le bras_robotique capture le déchet")
                bras_robotique.capturer_dechet()
                
                bras_robotique.soulever_dechet()

                
                if position_poubelle == "droite":
                    print("Pivot à droite")

                    robot.pivoter_droite()                  #   Il fait un pivot à droite en fait
                    
                    print("Le bras_robotique lâche le déchet à droite")
                    
                    bras_robotique.relacher_dechet()          #   ouverture des pinces
    
                    print("Retour sur la ligne", end="")
                    
                    robot.reculer_gauche()                  #   pour se remettre sur la ligne, ici on va tester un reculement et s'arrêter quand le robot revient sur la ligne
                    
                    print("...")

                elif position_poubelle == "gauche":
                    
                    print("Pivot à gauche")

                    robot.pivoter_gauche()                  #   Il fait un pivot à droite en fait
                    
                    print("Le bras_robotique lâche le déchet à gauche")
                    
                    bras_robotique.relacher_dechet()          #   ouverture des pinces
    
                    print("Retour sur la ligne", end="")
                    
                    robot.reculer_droite()                  #   pour se remettre sur la ligne, ici on va tester un reculement et s'arrêter quand le robot revient sur la ligne
                    
                    print("...")
                
                t2 = time.time()

                print(f"Le processus a duré {t2-t1} secondes.")
                
                while not ultra.checkdist() <= 15: # S'assurer que le robot ne continue pas tant qu'un obstacle est toujours devant lui
                    robot.define_droit = True
                            

main_flag = True
thread_principal = threading.Thread(target=main)