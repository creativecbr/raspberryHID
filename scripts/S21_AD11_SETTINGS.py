#!/usr/bin/env python3
import time

NULL_CHAR = chr(0)

DELAY=0.5
SHORT_DELAY=0.1

TAB = chr(43)
PAGE_UP = chr(75)
UP_ARROW = chr(82)
LEFT_ARROW = chr(80)
RIGHT_ARROW = chr(79)
DOWN_ARROW = chr(81)
ENTER = chr(40)
ESCAPE = chr(41)
ZERO = chr(39)

N_S = chr(17)
A_S = chr(4)


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def write_char(char, amount):
    for i in list(range(amount)):        
        write_report(NULL_CHAR*2 + char + NULL_CHAR*5)
        write_report(NULL_CHAR*8)
        time.sleep(DELAY)


def write_sequence(sequence):
    for ch in sequence:        
        write_char(ZERO, 1)        
        time.sleep(SHORT_DELAY)        

def sleeep(title, secs):
    for sec in list(range(secs)):
        time.sleep(1)
        print(str(title) + ": " + str(sec+1) + " sekunda")

def write_char_fast(char, amount):
    global DELAY
    tmp = DELAY
    global SHORT_DELAY
    DELAY = SHORT_DELAY
    write_char(char, amount)
    DELAY = tmp

def write_win_with_char(char):
    write_report(chr(8) + NULL_CHAR*7)
    write_report(chr(8) + NULL_CHAR + char + NULL_CHAR*5)
    write_report(chr(8) + NULL_CHAR*7)
    write_report(NULL_CHAR*8)


write_char(ENTER, 1)
sleeep("Odblokowywanie", 3)
write_char(ENTER, 1)
time.sleep(3)

# wyjscie z dziwnych okien
write_char(ESCAPE, 5)
time.sleep(2)
write_char(ESCAPE, 3)


# wejscie w ustawienia przez powiadomienia

write_win_with_char(N_S)
time.sleep(2)
write_char(TAB, 1)
write_char(ENTER, 1)
time.sleep(2)

#  wejscie w info o tel

write_char_fast(DOWN_ARROW, 30)
write_char(ENTER, 1)
time.sleep(2)

# info o oprogramowaniu
write_char_fast(DOWN_ARROW, 4)
write_char(ENTER, 1)
time.sleep(2)

# numer kompilacji
write_char_fast(DOWN_ARROW, 6)
write_char_fast(ENTER, 8)
time.sleep(2)

# cofnij
write_char(ESCAPE, 2)
time.sleep(3)

# w dol
write_char(DOWN_ARROW, 1)
write_char(ENTER, 1)
time.sleep(2)

# debugging
write_char_fast(DOWN_ARROW, 14)
write_char(ENTER, 1)
time.sleep(2)
write_char(ENTER, 1)

