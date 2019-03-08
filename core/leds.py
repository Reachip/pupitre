import time
import RPi.GPIO as GPIO


def animation(period, handlers):
    for loop in range(period):
        for handler in handlers:
            GPIO.output(handler, GPIO.LOW)
            time.sleep(0.1)

        for handler in reversed(handlers):
            GPIO.output(handler, GPIO.HIGH)
            time.sleep(0.1)
