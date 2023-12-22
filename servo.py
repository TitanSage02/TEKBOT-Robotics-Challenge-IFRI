import threading



def initialise():
    pass


def servo_libre():
    pass


class Servo():
    def __init__(self):
        # En fait, chaque servo sera mis dasn un bras
        self._flag = True              
        self.lock = threading.Lock()
    
    @property
    def read_flag(self):
        with self.lock:
            return self._flag
    
    @property.setter
    def define_flag(self, etat : bool):
        with self.lock:
            self._flag = etat
    

    @staticmethod
    def capturer_dechet():
        pass

    @staticmethod
    def soulever_dechet():
        pass

    @staticmethod
    def relacher_dechet():
        pass
    
    @staticmethod
    def join():
        initialise()                # Remet les servos dans l'état qu'il faut
        servo_libre()               # libère les servos 
        ######## fin du thread de chaque servo_moteur
        pass