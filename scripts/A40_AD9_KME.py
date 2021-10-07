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
A_KEY_SMALL = chr(4)


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

def write_char_fast(char, amount):
    global DELAY
    tmp = DELAY
    global SHORT_DELAY
    DELAY = SHORT_DELAY
    write_char(char, amount)
    DELAY = tmp



# 2 tab, enter
write_char(TAB, 2)
write_char(ENTER, 1)
time.sleep(3)

# laczenie z siecia komorkowa, 3 tab, enter
write_char(TAB, 4) # 1 added
write_char(ENTER, 1)
time.sleep(2)

# umowa, 2 tab, enter, 5 arrow down, enter
write_char(TAB, 2)
write_char(ENTER, 1)
write_char(DOWN_ARROW, 5)
write_char(TAB, 1) # added
write_char(ENTER, 1)
time.sleep(2)

#dost. star. danych. w celu przysp. konf, 6 tab, enter, 2 tab, enter, 5 sec, enter
write_char(TAB, 6)
write_char(ENTER, 1)
write_char(TAB, 3) # 1 added
write_char(ENTER, 1)
time.sleep(7)
write_char(ENTER, 1)
time.sleep(2)

# wifi
write_char(UP_ARROW, 3)
time.sleep(1)
write_char(PAGE_UP, 1)
write_char(DOWN_ARROW, 1)
write_char(ENTER, 1)
time.sleep(2)

#haslo
write_sequence("00000000")
write_char(ENTER, 1)
time.sleep(18)

# po hasle, 5 sec, arrowdown, enter
write_char(DOWN_ARROW, 1)
write_char(TAB, 1)
write_char(ENTER, 1)
time.sleep(20)
write_char(ENTER, 1)
print("Czekam na accept, teraz trwa aktualizacja")
time.sleep(380)
print("po accepcie, aktualizacja wgrana")
# aktualizacja ok. , minuta i 20 sec, czekaj 3 minuty

write_char(ENTER, 1)
time.sleep(3)
write_char(TAB, 4)
write_char(ENTER, 1) 
print("czekam na licencje knox")
time.sleep(180) # czekanie na licencje i ladowanie pierwszego ekranu
print("po licencji")
# czekamy na ustawienie wszystkiego
#  akcept knox
# ekran sie blokuje, tab, enter, 3 tab, enter
write_char(ENTER, 1) # unlock
time.sleep(5)
write_char(ENTER, 1)
time.sleep(2)

write_char(ENTER, 1)
write_char(TAB, 3)
write_char(ENTER, 1) 
