import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT) #234568
GPIO.setup(10, GPIO.OUT)
t = 0.1
pr = GPIO.PWM(10, 400)  # channel=10 frequency=400Hz
pb = GPIO.PWM(27, 400) 
pg = GPIO.PWM(22, 400) 
pr.start(0)
pb.start(0)
pg.start(0)
try:
    while 1:
        for dc in range(1, 101, 5):
            pr.ChangeDutyCycle(dc)
            time.sleep(t)
        for dc in range(1, 101, 5):
            pb.ChangeDutyCycle(dc)
            time.sleep(t)
        for dc in range(1, 101, 5):
            pg.ChangeDutyCycle(dc)
            time.sleep(t)
        for dc in range(100, -1, -5):
            pr.ChangeDutyCycle(dc)
            time.sleep(t)
        for dc in range(100, -1, -5):
            pb.ChangeDutyCycle(dc)
            time.sleep(t)
        for dc in range(100, -1, -5):
            pg.ChangeDutyCycle(dc)
            time.sleep(t)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
