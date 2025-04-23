import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
led1 = 15
led2 = 13
sw1 = 37
sw2 = 35

gpio.setup(led1,gpio.OUT,initial=0)
gpio.setup(led2,gpio.OUT,initial=0)
gpio.setup(sw1,gpio.IN)
gpio.setup(sw2,gpio.IN)

def glow(event):
    if event == sw1:
        gpio.output(led1,True)
        time.sleep(3)
        gpio.output(led1,False)
        time.sleep(2)
    
    elif event == sw2:
        gpio.output(led2,True)
        time.sleep(3)
        gpio.output(led2,False)
        time.sleep(2)

gpio.add_event_detect(sw1,gpio.RISING,callback=glow)
gpio.add_event_detect(sw2,gpio.RISING,callback=glow)

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    gpio.cleanup()