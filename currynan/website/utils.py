#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
import time
import datetime

def GPIOstart(number):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(number, GPIO.OUT)
    GPIO.output(number, 1)
    return

def GPIOcleanup():
    GPIO.cleanup()
    return

def executer(hour,minute,little=0,date=datetime.datetime.now()):
    #電圧をかけるGPIO番号。固定
    number=21

    #何秒間電圧をかけるべきなのか計算
    do_time=int(little) / 1

    #予約された時間になるまで待つ
    #time.sleep(予約された時間 - 現在の時間)
#    reservedTime=date.replace(hour=int(hour)).replace(minute=int(minute)).replace(second=0)
#    delta=(reservedTime - date).seconds
#    if delta > 60:
#        return
#    time.sleep(delta)
    time.sleep(3)

#    f=open("test.tmp","w")
#    f.write(str(date))
#    f.write("\n")
#    f.write(str(reservedTime))
#    f.write("\n")
#    f.write(str(delta))
#    f.write("\n")

    GPIOstart(number)
    time.sleep(do_time)
#    time.sleep(5)
    GPIOcleanup()

#    f.write("finish")
#    f.close()

