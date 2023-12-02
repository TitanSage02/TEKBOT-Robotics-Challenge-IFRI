import time
import threading
import cv2

class CameraEvent:
    def __init__(self):
        self.event = threading.Event()

    def wait(self):
        self.event.wait()

    def set(self):
        self.event.set()

    def clear(self):
        self.event.clear()

class PiCamera:
    thread = None
    frame = None
    event = CameraEvent()

    @staticmethod
    def _thread():
        print('Démarrage du thread de la caméra.')
        camera = cv2.VideoCapture(0)
        while True:
            _, frame = camera.read()
            PiCamera.frame = frame
            PiCamera.event.set()
            time.sleep(1)  # capture une image toutes les une seconde

    def __init__(self):
        if PiCamera.thread is None:
            PiCamera.thread = threading.Thread(target=self._thread, daemon=True)
            PiCamera.thread.start()

    def get_frame(self):
        "retrourne une frame à une taille fixe (224x224)"
        PiCamera.event.wait()
        PiCamera.event.clear()

        resized_frame = cv2.resize(PiCamera.frame, (224, 224))

        return resized_frame

try:
    # Crée une instance de la caméra
    camera = PiCamera()

    time_debut = time.time()
    # Effectue une boucle pour récupérer les images et afficher le résultat du test des servos
    while True:
        frame = camera.get_frame()
        cv2.imshow("Test Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # Quitte la boucle si la touche 'q' est pressée

        # Quitte la boucle après 60 secondes
        t = time.time() - time_debut
        if t > 60:
            break

except Exception as error:
    cv2.destroyAllWindows()
    raise error
finally:
    cv2.destroyAllWindows()
