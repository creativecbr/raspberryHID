#!/usr/bin/env python3
import time

NULL_CHAR = chr(0)

DELAY=0.5
SHORT_DELAY=0.1

TAB = chr(43)
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
        write_char(ZERO,1)        
        time.sleep(SHORT_DELAY)        

def write_char_fast(char, amount):
    global DELAY
    tmp = DELAY
    global SHORT_DELAY
    DELAY = SHORT_DELAY
    write_char(char, amount)
    DELAY = tmp

# tab enter
write_char(TAB, 1)
write_char(ENTER,1)
time.sleep(2)

# strzlka w dol 70, enter
write_char_fast(DOWN_ARROW, 70)
write_char(ENTER,1)
time.sleep(2)

# laczenie z siecia komorkowa
write_char(TAB, 3)
write_char(ENTER,1)
time.sleep(2)

# tab x 2 licencja
write_char(TAB, 2)
write_char(ENTER,1)  #accept 1 regulaminu

# tab x 2, enter, strzalka x 7, enter
write_char_fast(DOWN_ARROW, 8)
write_char(ENTER, 1)
time.sleep(2)

#wifi
write_char(TAB, 1)
write_char(ENTER,1)
write_sequence("00000000")
write_char(ENTER,1)
time.sleep(5)

# strzalka w dol x 20, enter
write_char_fast(DOWN_ARROW, 20)
write_char(ENTER, 1)
time.sleep(30)

# tab x 1?, enter
write_char(TAB, 1)
write_char(ENTER, 1)
time.sleep(10)


write_char(TAB, 2)
write_char(ENTER, 1)
time.sleep(10)

#akceptuj
write_char(TAB, 5)
write_char(ENTER, 1)
time.sleep(20)

write_char(TAB, 2)
write_char(ENTER, 1)
time.sleep(3)
# godzina i data
#write_char(TAB, 4)
#write_char(ENTER, 1)
#time.sleep(2)

# tab x 10, enter, encter
write_char(TAB, 9)
write_char(ENTER, 2)
time.sleep(2)



# ochrona telefonu strzalka w dol x 7, enter, strzalka w prawo, enter
# write_char_fast(DOWN_ARROW, 7)
# write_char(ENTER, 1)
# write_char(RIGHT_ARROW, 1)
# write_char(ENTER, 1)
# time.sleep(4)

# # tab  x 5, polecane
# write_char_fast(TAB, 6)
# write_char(ENTER, 1)
# time.sleep(2)

# # samsung account tab x 7, enter
# write_char_fast(TAB, 7)
# write_char(ENTER, 1)
# time.sleep(2)

# # strzalka w dol, strzalka w prawo, enter
# write_char(DOWN_ARROW, 2)
# write_char(RIGHT_ARROW, 1)
# write_char(ENTER, 1)
# time.sleep(2)

# # tab x 2, ENTER(NIEPISAC)
# write_char(TAB, 2)
# write_char(ENTER, 1)

# czas na załadowanie ekranu głównego
# time.sleep(17)


# # wpisanie a i wejscie w ustawienia
# write_char(A_KEY_SMALL, 1)
# time.sleep(3)
# write_char(A_KEY_SMALL, 1)
# time.sleep(1)
# write_char(ENTER,1)
# time.sleep(2)
# write_char(TAB, 5)
# write_char(ENTER,1)
# time.sleep(2)

# #wyjscie do glownego menu ustawien
# write_char(ENTER,2)
# write_char(DOWN_ARROW, 20)
# write_char(ENTER, 1)

# # o telefonie
# write_char(TAB, 6)
# write_char(ENTER, 1)

# #numer wersji
# write_char(TAB,5)
# write_char(ENTER, 8)

# # do glownego menu ustawien
# write_char(ESCAPE, 2)
# write_char(DOWN_ARROW, 1)
# write_char(ENTER, 1)


# # debuging
# write_char(DOWN_ARROW, 15)
# write_char(ENTER, 1)
# write_char(TAB, 1)
# write_char(ENTER, 1)

print("GOTOWE")
