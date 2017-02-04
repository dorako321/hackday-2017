#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO

def GPIOstart(number):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(number, GPIO.OUT)
    GPIO.output(number, 1)
    return

def GPIOcleanup():
    GPIO.cleanup()
    return
