#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# joystick_mapping_keyboard.py
# Mapping keyboard Up/Down/Right/Left by joystick 
#
# Author : sosorry
# Date   : 12/10/2015
# Origin : http://python-evdev.readthedocs.org/en/latest/tutorial.html

import time
import spidev
import os
import RPi.GPIO as GPIO
from evdev import UInput, ecodes as e

ui = UInput()
spi = spidev.SpiDev()
spi.open(0,0)

JUMP_PIN = 12
FIRE_PIN = 11
GPIO.setmode(GPIO.BOARD)                
GPIO.setup(JUMP_PIN, GPIO.IN)
GPIO.setup(FIRE_PIN, GPIO.IN)
swt_channel = 0
vrx_channel = 1 
vry_channel = 2 

def ReadChannel(channel):
    adc = spi.xfer2([1, (8+channel)<<4, 0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def ButtonEvent(channel):                                                 
    if GPIO.input(JUMP_PIN) == 1:
        ui.write(e.EV_KEY, e.KEY_LEFTALT, 0)  
        ui.syn()
    if GPIO.input(JUMP_PIN) == 0:
        ui.write(e.EV_KEY, e.KEY_LEFTALT, 1) 
        ui.syn()
    if GPIO.input(FIRE_PIN) == 1:
        ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 0)  
        ui.syn()
    if GPIO.input(FIRE_PIN) == 0:
        ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 1) 
        ui.syn()

try:
    GPIO.add_event_detect(JUMP_PIN, GPIO.BOTH, callback=ButtonEvent)
    GPIO.add_event_detect(FIRE_PIN, GPIO.BOTH, callback=ButtonEvent)

    while True:
        swt_val = ReadChannel(swt_channel)
        vrx_pos = ReadChannel(vrx_channel)
        vry_pos = ReadChannel(vry_channel)

        #print "--------------------------------------------"  
        #print("X : {}  Y : {}  Switch : {}".format(vrx_pos,vry_pos,swt_val))

        # LEFT
        if vry_pos > 700 :
            ui.write(e.EV_KEY, e.KEY_LEFT,  1)  
            ui.write(e.EV_KEY, e.KEY_RIGHT, 0)
            ui.syn()
        # RIGHT
        elif vry_pos < 200 :
            ui.write(e.EV_KEY, e.KEY_RIGHT, 1)
            ui.write(e.EV_KEY, e.KEY_LEFT,  0)
            ui.syn()
        else :
            ui.write(e.EV_KEY, e.KEY_RIGHT, 0)
            ui.write(e.EV_KEY, e.KEY_LEFT,  0)
            ui.syn()

        # DOWN
        if vrx_pos > 700 :
            ui.write(e.EV_KEY, e.KEY_DOWN,  1)  
            ui.write(e.EV_KEY, e.KEY_UP,    0)
            ui.syn()
        # UP
        elif vrx_pos < 200 :
            ui.write(e.EV_KEY, e.KEY_DOWN, 1)
            ui.write(e.EV_KEY, e.KEY_UP,   0)
            ui.syn()
        else :
            ui.write(e.EV_KEY, e.KEY_DOWN, 0)
            ui.write(e.EV_KEY, e.KEY_UP,   0)
            ui.syn()

        time.sleep(0.1)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"


