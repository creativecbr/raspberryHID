#!/usr/bin/env python3
import time

def write_report(report):
    with open('/dev/hidg0', 'wb+') as fd:
        fd.write(report)
       
def alternate_left_right():
    s1 = b'\x00\x7f\x00'
    s2 = b'\x00\x90\x00'
    for i in range(2):
        write_report(s1)
        time.sleep(0.3)
        write_report(s2)
        time.sleep(0.3)

def click_somewhere():
    s1 = b'\x01\x00\x00'
    s2 = b'\x00\x00\x00'
    for i in range(1):
        write_report(s1)
        time.sleep(0.3)
        write_report(s2)
        time.sleep(0.3)
    write_report(b'\x00\x00\x00')


alternate_left_right()
click_somewhere()
