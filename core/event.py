import logging
import threading
from logging.handlers import RotatingFileHandler

import serial
import RPi.GPIO as GPIO


class Event(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.callbacks = {}
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(message)s")
        file_handler = RotatingFileHandler("/home/pi/pupitre.log", "a", 1000000, 1)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(stream_handler)

        try:
            self.bluetooth_module = serial.Serial(
                port="/dev/ttyAMA0",
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1,
            )

        except Exception as error:
            self.logger.warning("Erreur concernant le serial du Raspberry : " + error)

    def on_with_sound_and_leds(self, callback):
        self.callbacks[b"2"] = callback
        return callback

    def on_with_just_sound(self, callback):
        self.callbacks[b"1"] = callback
        return callback

    def on_with_leds(self, callback):
        self.callbacks[b"3"] = callback
        return callback

    def run(self):
        while True:
            try:
                req = self.bluetooth_module.readline()
                self.callbacks[req]()

            except KeyboardInterrupt:
                GPIO.cleanup()

            except KeyError:
                pass
