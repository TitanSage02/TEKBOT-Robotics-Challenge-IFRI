import time
from rpi_ws281x import *

LED_COUNT = 12       # Nombre de pixels LED.
LED_PIN = 12         # Broche GPIO connectée aux pixels (18 utilise PWM!).
LED_FREQ_HZ = 800000 # Fréquence du signal LED en hertz (généralement 800khz)
LED_DMA = 10         # Canal DMA à utiliser pour générer le signal (essayez 10)
LED_BRIGHTNESS = 255 # Réglez à 0 pour le plus sombre et à 255 pour le plus lumineux
LED_INVERT = False   # True pour inverser le signal (lors de l'utilisation d'un décalage de niveau transistor NPN)
LED_CHANNEL = 0      # Défini sur '1' pour GPIOs 13, 19, 41, 45 ou 53

class LED:
    def __init__(self):
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip.begin()

    def colorWipe(self, R, G, B):
        color = Color(R, G, B)
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()

led = LED()
try:
    while True:
        led.colorWipe(255, 0, 0)  # Rouge
        time.sleep(0.5)
        led.colorWipe(0, 255, 0)  # Vert
        time.sleep(0.5)
        led.colorWipe(0, 0, 255)  # Bleu
        time.sleep(0.5)
except KeyboardInterrupt:
    led.colorWipe(0, 0, 0)  # Extinction des lumières