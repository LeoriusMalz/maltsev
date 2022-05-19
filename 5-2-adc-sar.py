import RPi.GPIO as GPIO
import time
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc():
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
        time.sleep(0.1)
        DecimallValue = adc()
        print("voltage is ")
        print(DecimallValue*3.3/255)
        print("DecimallValue is ")
        print(DecimallValue)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
