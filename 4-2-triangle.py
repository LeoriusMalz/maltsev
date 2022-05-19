import RPi.GPIO as GPIO
import time

def dec2bin(x):
    return [int(i)for i in bin(x)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

T = 50

try:
    while True:
        for i in range(255):
            time.sleep(1/T)
            number = dec2bin(i)
            GPIO.output(dac, number)
        
        for i in range(255, 0, -1):
            time.sleep(1/T)
            number = dec2bin(i)
            GPIO.output(dac, number)
        
        break

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
