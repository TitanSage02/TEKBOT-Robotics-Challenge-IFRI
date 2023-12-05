import time
import picamera

# Initialisation de la caméra
camera = picamera.PiCamera()

try:
    while True:
        # Nom du fichier avec timestamp
        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = f"photo_{timestamp}.jpg"

        # Capture et enregistrement de la photo
        camera.capture(filename)

        # Attente de 5 secondes
        time.sleep(5)

except KeyboardInterrupt:
    # Arrêt du programme en cas d'interruption (Ctrl+C)
    pass

finally:
    # Fermeture de la caméra
    camera.close()
    
