#!/usr/bin/env python
# coding=utf-8
import RPi.GPIO as GPIO
import time
#import picamera
import datetime  # new
sensor = 22
vibration = 20
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(vibration, GPIO.OUT)
GPIO.output(vibration,1)
def get_file_name():  # new
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")
def vib():
        p = GPIO.PWM(20,50)
        p.start(100)
        for i in range (100,1,-1):
                p.ChangeDutyCycle(i)
#               time.sleep(0.02)
        for i in range (1,100,1):
                p.ChangeDutyCycle(i)
#               time.sleep(0.01)
previous_state = False
current_state = False
#cam = picamera.PiCamera()
try:
 while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        print("GPIO pin %s is %s" % (sensor, new_state))
        if current_state:
#          fileName = get_file_name()
#          cam.capture(fileName)
           GPIO.output(20,0)
           time.sleep(1)
    else:
        GPIO.output(20,1)
except KeyboardInterrupt:
        GPIO.output(20,1)
        GPIO.cleanup()
