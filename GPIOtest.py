#!/usr/bin/python
# coding: utf-8

# モジュール使用宣言
# GPIOモジュールとtimeモジュールをimport
import RPi.GPIO as GPIO
import time

number=21

# GPIO指定をGPIO番号で行う
GPIO.setmode(GPIO.BCM)

# GPIO21ピンを出力モードに設定
GPIO.setup(number, GPIO.OUT)

# GPIO21番ピンを3.3Vに設定
GPIO.output(number, 1)

# 1秒待つ
time.sleep(1)

# GPIO設定をリセット
GPIO.cleanup()
