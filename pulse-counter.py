import RPi.GPIO as GPIO
import time, sys

FLOW_SENSOR = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel):
    global count
    count = count + 1

GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)

while True:
    try:
        time.sleep(0.5)

        if count > 0:
            print count
            count = 0
            sys.stdout.flush()

    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()

