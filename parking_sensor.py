import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

BUZZ_TRIG = 14
HC_TRIG = 23
ECHO = 24

GPIO.setup(BUZZ_TRIG,GPIO.OUT)
GPIO.setup(HC_TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(HC_TRIG, False)
buzzer = GPIO.PWM(BUZZ_TRIG, 200)
buzzer.start(40)
time.sleep(0.5)

while True:
        GPIO.output(HC_TRIG, True)
        time.sleep(0.00001)
        GPIO.output(HC_TRIG, False)

        while GPIO.input(ECHO)==0:
          pulse_start = time.time()

        while GPIO.input(ECHO)==1:
         pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        print("Distance:",distance,"cm")

        if distance <= 8:
                buzzer.ChangeFrequency(1200)
        if distance > 8 and distance <= 15:
                buzzer.ChangeFrequency(700)
        if distance > 15 and distance <= 25:
                buzzer.ChangeFrequency(400)
        if distance > 25:
                buzzer.ChangeFrequency(10)
        time.sleep(0.5)

GPIO.cleanup()
sys.exit()