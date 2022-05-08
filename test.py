#VBUS - relay comm
#VSYS - relay 3v pin
#GND - relay gnd pin
#3V3_EN - none
#3V3_OUT - Moisture Power
#ADC_VREF - none
#GP28 - none
#AGND - pump gnd
#GP27 - moisture scl
#GP26 - moisture sda
#run - none
#GP22 - relay control
#GND - moisture ground

import time, board, busio
dir(board)
i2c = busio.I2C(board.GP27, board.GP26)
from adafruit_seesaw.seesaw import Seesaw
ss = Seesaw(i2c, addr=0x36)

from machine import Pin
pump = Pin(22, Pin.OUT)
level = 990

def status():
    print(ss.moisture_read())
    print(ss.get_temp())

def pump_water():
    while True:
        if ss.moisture_read() < level:
            print(ss.moisture_read())
            pump.on()
            time.sleep(2.5)
            pump.off()
        time.sleep(100.0)
