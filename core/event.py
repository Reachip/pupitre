import threading

import serial
import RPi.GPIO as GPIO


class Event(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.callbacks = {}
        self.bluetooth_module = serial.Serial(
            port="/dev/ttyAMA0",
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1,
        )

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
                self.callbacks[self.bluetooth_module.readline()]()

            except KeyboardInterrupt:
                GPIO.cleanup()

            except KeyError:
                pass
