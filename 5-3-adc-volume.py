import RPi.GPIO as GPIO
import time
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc1():
    for value in range(256):
        sig = decimal2binary(value)
        GPIO.output(dac, sig)
        time.sleep(0.001)
        compval = GPIO.input(comp)
        if compval == 0:
            return value
    return value

def adc2():
    val = 0
    bin = 128
    for i in range(8):
        buf = val + bin
        sig = decimal2binary(int(buf))
        GPIO.output(dac, sig)
        time.sleep(0.001)
        compval = GPIO.input(comp)
        if compval == 1:
            val += bin
            bin /= 2
    return val

try:
    while True:
        DecimallValue = adc1()
        val = 1
        i = 1
        ch = DecimallValue
        ch -= 32
        while ch > 0:
            ch -= 32
            i = i*2
            val += i
        loud = decimal2binary(int(val))
        print("voltage is ")
        print(DecimallValue*3.3/255)
        GPIO.output(leds, loud)
        time.sleep(0.1)

finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()
