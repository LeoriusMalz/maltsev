import RPi.GPIO as GPIO

#def dec2bin(x):
#    return [int(i)for i in bin(x)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)
p.start(0)

try:
    while True:
        k = int(input())
        p.stop()
        p.start(k)
        print(k*3.3/100)
        
finally:
    GPIO.cleanup()
