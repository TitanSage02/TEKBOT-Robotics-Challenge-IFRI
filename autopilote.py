import threading
from moteurs import Moteurs
from tracking import Tracking
from led import LED

from main import change_main_flag_to
import time

def initialise():
    global moteurs, track, vitesse
    moteurs = Moteurs()
    track = Tracking()
    vitesse = 100

class AutoPilot:
    "Elle gere la direction autonome du robot"
    def __init__(self):
        initialise()
        self._flag = True               # Pour contrôler la fin du thread
        self.avance = True              # Permet de mettre de faire des arrêts sans arrêter le thread
        self.thread = threading.Thread(target=self._thread)
        self.lock = threading.Lock()
    
    @property
    def read_flag(self):
        "Permet à l'autopilote de savoir s'il doit s'arrêter eventuellement"
        with self.lock:
            return self._flag
    
    @property.setter
    def define_flag(self, etat : bool):
        "Prend True si le robot doit avancer et False sinon"
        with self.lock:
            self._flag = etat

    @property
    def read_droit(self):
        "Permet à l'autopilote de savoir s'il doit s'arrêter eventuellement"
        with self.lock:
            return self.avance
    
    @property.setter
    def define_droit(self, etat : bool):
        "Prend True si le robot doit avancer et False sinon"
        with self.lock:
            self.avance = etat

    def demarrer(self):
        self.thread.start()
        print("Autopilot démarré")

    def _thread(self):
        while self.read_flag:
            
            if self.read_droit:
                
                status = track.etat()
                
                if status["milieu"] == 1: 
                    moteurs.avancer(vitesse)
                
                elif status["gauche"] == 1 : 
                    moteurs.tourner_gauche(vitesse)
                    
                elif status["droit"] == 1:
                    moteurs.tourner_droite(vitesse)
                    
                else:
                    change_main_flag_to(False)                  #Arrêt de tous les threads en cours d'éxecution
                    print("Mission terminée !!! ")
                    
                    moteurs.stop() 
                    
                    led = LED()
                    
                    led.color("rouge")
                
                time.sleep(0.1)
            else:
                # Arrêt des moteurs en attendant que le bras robotique fasse sn travail
                moteurs.stop()
        #Fin du parcours
        moteurs.stop()

   
    def pivoter_droite():
        #à revoir peut être
        moteurs.tourner_droite(vitesse)
        time.sleep(0.4)
        moteurs.stop()
    
    
    def pivoter_gauche(self):
        moteurs.tourner_gauche(vitesse)
        time.sleep(0.4)
        moteurs.stop()
    
    
    def reculer_droite():
        "Ramène le robot sur la ligne"
        status = track.etat()
        
        while not 1 in list(status.values()): # S'assure qu'au moins l'un des capteurs du module de tracking détecte la piste
            moteurs.reculer_droite(vitesse)
            status = track.etat()
        
        moteurs.stop() #Le robot est sur la ligne et on coupe les moteurs
    
    def reculer_gauche():
        "Ramène le robot sur la ligne"
        status = track.etat()
        
        while not 1 in list(status.values()): # S'assure qu'au moins l'un des capteurs du module de tracking détecte la piste
            moteurs.reculer_gauche(vitesse)
            status = track.etat()
        
        moteurs.stop() #Le robot est sur la ligne et on coupe les moteurs

        
    
    


if __name__ == "__main__":
    try:
        test_robot = AutoPilot()
        test_robot.demarrer()
        time.sleep(10)
        moteurs.stop()
        test_robot._flag = False
        test_robot.thread.join()
    except:
        pass
        
