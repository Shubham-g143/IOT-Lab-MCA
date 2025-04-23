import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

led1 = 15
gpio.setup(led1,gpio.OUT,initial=0)

file1 = open('demo.txt','r')
lines = file1.readline()

on_time = int(lines[0].split("=")[1])
off_time = int(lines[1].split("=")[1])

try :
    gpio.output(led1,True)
    time.sleep(3)
    gpio.output(led1,False)
    time.sleep(4)
except KeyboardInterrupt:
    gpio.cleanup()