import time
import threading
import cv2

class CameraEvent:
    "Un objet de type événement qui signale tous les clients actifs lorsqu'une nouvelle image est disponible."
    def __init__(self):
        self.event = threading.Event()

    def wait(self):
        "Appelé à partir du thread de chaque client pour attendre la prochaine image."
        self.event.wait()

    def set(self):
        "Appelé par le thread de la caméra lorsqu'une nouvelle image est disponible."
        self.event.set()

    def clear(self):
        "Appelé depuis le thread de chaque client après le traitement d'une image."
        self.event.clear()

class PiCamera:
    thread = None
    frame = None
    last_access = 0
    event = CameraEvent()

    @staticmethod
    def _thread():
        "Thread d'arrière-plan de la caméra."
        print('Démarrage du thread de la caméra.')
        camera = cv2.VideoCapture(0)
        while True:
            _, frame = camera.read()
            PiCamera.frame = frame
            PiCamera.event.set()
            time.sleep(5)


    def __init__(self):
        if PiCamera.thread is None:
            PiCamera.thread = threading.Thread(target=self._thread)
            PiCamera.last_access = time.time()
            PiCamera.thread.start()

    def get_frame(self):
        "Retourne l'image actuelle de la caméra."
        PiCamera.last_access = time.time()
        PiCamera.event.wait()
        PiCamera.event.clear()
        return PiCamera.frame

try:
    # Crée une instance de la caméra
    camera = PiCamera()

    time_debut = time.time()
    # Effectue une boucle pour récupérer les images et afficher le résultat du test des servos
    while True:
        frame = camera.get_frame()
        cv2.imshow("Test Camera", frame)

        # Quitte la boucle après 10s
        if time.time() - time_debut > 10:
            cv2.destroyAllWindows()
            break
except Exception as error:
    cv2.destroyAllWindows()
    raise error
