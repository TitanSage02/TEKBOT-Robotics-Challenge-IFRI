
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685
#import RPIservo


servo1_direction = 1
servo2_direction = 1
servo3_direction = 1
servo4_direction = 1

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#(duty ratio -100)/2.55
#Using the ebove formula, we have 
# 100 for 0°
# 560 for 180°


pwm0_init = 500
pwm0_max  = 450
pwm0_min  = 150
pwm0_pos  = pwm0_init

pwm1_init = 300
pwm1_max  = 480
pwm1_min  = 160
pwm1_pos  = pwm1_init

pwm2_init = 300
pwm2_max  = 500
pwm2_min  = 100
pwm2_pos  = pwm2_init

pwm3_init = 300
pwm3_max  = 500
pwm3_min  = 300
pwm3_pos  = pwm3_init

origin_pos = 300 #300

def duty_ratio(angle): # calcul les angles en degre
    degre = (angle - 100)/2.55
    return int(degre)

def initialization():
    
    try:    
        pwm.set_all_pwm(0, 100) # all servomotor are initialize to 300 degree
        time.sleep(1)
    except:
        pass
    

# min and max degree interval
def interval (angle,min_angle,max_angle):
    if angle < min_angle:
        angle = min_angle
        
    elif angle > max_angle:
        angle = max_angle
        
    else:
        pass
    
    return int(angle)

# second servomotor

"""
def ahead():
	global pwm0_pos, pwm1_pos
	pwm.set_pwm(0, 0, pwm0_init)
	pwm.set_pwm(1", 0, (pwm1_ma"x-20))
	pwm0"_pos = pwm0_"init
	pwm1_"pos = pwm1_"max-20
   " 
"""


        
def servo_camera(angle_camera): # servo numero 11
# initialisation
    angle = interval(angle_camera, 150, 500)
    pwm.set_pwm(11, 0, angle)

def servo_post_cam(n): 
    #angle = interval(post_angle, 150, 500)   
    pwm.set_pwm(12, 0,n)
    
    
def servo_arm_1(angle_arm1):
    angle = interval(angle_arm1, 150, 500)
    pwm.set_pwm(13, 0,angle)
    
def servo_180(angle_180):
    angle = interval(angle_180, 150, 500)
    pwm.set_pwm(14, 0,angle)
    
def hand_servo(hand_angle):
    angle = interval(hand_angle, 150, 500)
    pwm.set_pwm(15, 0,angle)
    
def clean_all():
	global pwm
	pwm = Adafruit_PCA9685.PCA9685()
	pwm.set_pwm_freq(50)
	pwm.set_all_pwm(0, 0)
    
    
if  __name__ == '__main__':

    try:
        angle_camera = 200
        post_angle = 150
        angle_arm1 = 250
        angle_180 = 100
        hand_angle = 150
        
        pwm.set_pwm_freq(50)
        #initialization()
        #print("initialisation terminer")
        #time.sleep(1)
        #servo_camera(angle_camera) #   * caméra
        
        #time.sleep(1)
        #pwm.set_pwm(12, 0, 300)
        #time.sleep(4)
        #pwm.set_pwm(12, 0, 185)    #servo_post_cam(post_angle) #   *4
        
        #time.sleep(1)
        
        #pwm.set_pwm(13, 0, 100) #   *3 
        #time.sleep(2)
        #pwm.set_pwm(13, 0, 255) #   *3 

        #time.sleep(1)
        
        pwm.set_pwm(12, 0, 300) # servo 4 init
        pwm.set_pwm(12, 0, 185) # servo 4 position de capture
        time.sleep(4)
        pwm.set_pwm(13, 0, 255) # abaisser bon angle  servo 3 
        pwm.set_pwm(13, 0, 100) # soulève servo 3
        
        #time.sleep(1)
        
        #hand_servo(hand_angle) #    *1
        
        #time.sleep(1)
        
        clean_all()
        #print(f"post_cam {post_angle}")
        
        
    except:
        pass


"""
def initialise():
    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(50)
    
    pwm.set_pwm(12, 0, 300) # servo 4 init
    pwm.set_pwm(12, 0, 185) # servo 4 position de capture

    pwm.set_pwm(13, 0, 255) # abaisser bon angle  servo 3 
    pwm.set_pwm(13, 0, 100) # soulève servo 3




"""