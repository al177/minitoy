import machine
import os
import time


def boot(binfile):
    creset=machine.Pin(5,machine.Pin.OUT, machine.Pin.PULL_UP)
    cdone=machine.Pin(4,machine.Pin.IN, machine.Pin.PULL_UP)
    ss=machine.Pin(15,machine.Pin.OUT, machine.Pin.PULL_UP)
    s=machine.SPI(1,polarity=1,phase=1,baudrate=10000000)

    creset.off()
    ss.off()
    time.sleep(1)
    creset.on()
    print(cdone.value())
    time.sleep(1)
    with open(binfile,'rb') as f:
        b=f.read(32)
        while b:
            b=f.read(32)
            s.write(b)
    print(cdone.value())
    bytecnt=0
    while bytecnt < 20:
        bytecnt+=1
        s.write(b'X')
    print(bytecnt)
    ss.on()
    print(cdone.value())

