import os
import json
import time
import random
from pathlib import Path

from omxplayer.player import OMXPlayer
import RPi.GPIO as GPIO

from core import event
from core import leds

event = event.Event()
event.start()

with open(os.getcwd() + "/pypitre/config.json") as json_file: 
    global json_datas
    json_datas = json.load(json_file)

GPIO.setmode(GPIO.BCM)
[GPIO.setup(handler, GPIO.OUT, initial=GPIO.HIGH) for handler in json_datas["leds_handlers"]]


@event.on_with_just_sound
def with_just_sound():
    path = Path(json_datas["music_path"])
    OMXPlayer(path)

@event.on_with_sound_and_leds
def with_sound_and_led():
    path = Path(json_datas["music_path"])
    OMXPlayer(path)

    for loop in range(5):
        for handler in json_datas["leds_handlers"]:
            GPIO.output(handler, GPIO.LOW)
            time.sleep(0.1)

        for handler in reversed(json_datas["leds_handlers"]):
            GPIO.output(handler, GPIO.HIGH)
            time.sleep(0.1)

@event.on_with_leds
def with_leds():
    for loop in range(5):
        for handler in json_datas["leds_handlers"]:
            GPIO.output(handler, GPIO.LOW)
            time.sleep(0.1)

        for handler in reversed(json_datas["leds_handlers"]):
            GPIO.output(handler, GPIO.HIGH)
            time.sleep(0.1)

event.join()


