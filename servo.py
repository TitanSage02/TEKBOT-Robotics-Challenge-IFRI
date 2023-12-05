import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

def test_servo(channel, pwm_min, pwm_max):
    pwm.set_pwm(channel, 0, pwm_min)
    time.sleep(1)
    pwm.set_pwm(channel, 0, pwm_max)
    time.sleep(1)

if __name__ == '__main__':
    pwm_min = 150
    pwm_max = 450

    # Test pwm0
    test_servo(0, pwm_min, pwm_max)

    # Test pwm1
    test_servo(1, pwm_min, pwm_max)

    # Test pwm2
    test_servo(2, pwm_min, pwm_max)

    # Test pwm3
    test_servo(3, pwm_min, pwm_max)
    
