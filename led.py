import time
import threading
from rpi_ws281x import *

LED_COUNT = 12       # Nombre de pixels LED.
LED_PIN = 12         # Broche GPIO connectée aux pixels (18 utilise PWM!).
LED_FREQ_HZ = 800000 # Fréquence du signal LED en hertz (généralement 800khz)
LED_DMA = 10         # Canal DMA à utiliser pour générer le signal (essayez 10)
LED_BRIGHTNESS = 255 # Réglez à 0 pour le plus sombre et à 255 pour le plus lumineux
LED_INVERT = False   # True pour inverser le signal (lors de l'utilisation d'un décalage de niveau transistor NPN)
LED_CHANNEL = 0      # Défini sur '1' pour GPIOs 13, 19, 41, 45 ou 53

led_color = [0, 0, 0]

class LED:
    def __init__(self):
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip.begin()
        
        self.thread = threading.Thread(target=self._colorWipe)
        self.thread.start()
        self.lock  = threading.Lock()
        self._flag = True
    
    @property
    def read_flag(self):
        with self.lock:
            return self._flag

    @property.setter
    def define_flag(self, value: bool):
        with self.lock:
            self._flag = value
    
    
    def _colorWipe(self):
        global led_color
        while self.read_flag:        
            R = led_color[0]
            G = led_color[1]
            B = led_color[2]
            self.colorWipe(R, G, B)
            for i in range(1, 20):
                self.colorWipe(R(1-i), G(1-i), B(1-i))
            for i in range(20, 1. -1):
                self.colorWipe(R(1+i), G(1+i), B(1-i))

    def colorWipe(self, R, G, B):
        color = Color(R, G, B)
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()

    def color(self, couleur):
        global led_color               
        if couleur == "vert":
            led_color = [0, 255, 0]
            
        elif couleur == "rouge":
            led_color = [255, 0, 0]
            
        elif couleur == "bleu":
            led_color = [0, 0, 255]
            
        elif couleur == "marron":
            led_color = [139, 69, 19]
            

if __name__ == '__main__':
    led = LED()
    try:
        while True:
            led.colorWipe(255, 0, 0)  # Rouge
            time.sleep(0.5)
            led.colorWipe(150, 24, 50)
            time.sleep(0.5)
            led.colorWipe(0, 255, 0)  # Vert
            time.sleep(0.4)
            led.colorWipe(123, 40, 92) 
            led.colorWipe(24, 79, 152)  
            time.sleep(0.4)
            led.colorWipe(0, 0, 255)  # Bleu
            time.sleep(0.5)
    except:
        led.define_flag = False
        led.thread.join()
        led.colorWipe(0, 0, 0)
        exit(0)



