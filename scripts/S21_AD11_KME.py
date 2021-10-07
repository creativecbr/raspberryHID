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

def sleeep(title, secs):
    i = 0
    for sec in list(range(secs)):
        time.sleep(1)
        if secs > 20:
            if i % 4 == 0:
                print(str(title) + ": " + str(sec+1) + "/" + str(secs) + " sekund")
        else:
            print(str(title) + ": " + str(sec+1) + "/" + str(secs) + " sekund")
        i = i + 1

def write_char_fast(char, amount):
    global DELAY
    tmp = DELAY
    global SHORT_DELAY
    DELAY = SHORT_DELAY
    write_char(char, amount)
    DELAY = tmp



write_char(ENTER, 1)
sleeep("Odblokowywanie", 5)

#wyjscie z okien
write_char(ESCAPE, 5)
time.sleep(3)

# 1 
write_char(TAB, 4)
write_char(ENTER, 1)
time.sleep(3)



#  jezyki
write_char_fast(DOWN_ARROW, 40) 
write_char(ENTER, 1) #polski

write_char_fast(DOWN_ARROW, 70)
write_char(ENTER, 1)
time.sleep(3)

# laczenie z siecia
write_char(TAB, 3)
write_char(ENTER, 1)
time.sleep(2)

# umowa
write_char(TAB, 2)
write_char(ENTER, 1)
write_char(TAB, 12)
write_char(ENTER, 1)
time.sleep(3)

# wifi
write_char(ENTER, 1) # popup
time.sleep(3)
write_char(UP_ARROW, 1)
#write_char(DOWN_ARROW, 1) # druga sieć wtedy
write_char(ENTER, 1) 

#sleeep("Rozpoznawanie sieci", 20)
#write_char(ESCAPE, 1)
#write_char(UP_ARROW, 1)
#write_char(DOWN_ARROW, 1)
#write_char(ENTER, 1)
sleeep("Czekanie na zalaczenie activity wifi", 4)

print("sekwencja podawana")

#pass
write_sequence("00000000")
write_char(ENTER, 1)
sleeep("Laczenie z wifi", 24)

# po hasle
write_char_fast(DOWN_ARROW, 25)
write_char(ENTER, 1)

sleeep("Aktualizacja", 120) #  aktualizacje


write_char(ENTER, 1) # mozliwe ze sie nie blokuje, sprawdzic
sleeep("Odblokowanie po aktualizacji", 3)
write_char(TAB, 4)
write_char(ENTER, 1)

 
sleeep("Konfiguracja profilu roboczego", 60)
write_char(ENTER, 1)
sleeep("Odblokowanie po konf. roboczego", 3)

# gotowe
write_char(TAB, 1)
write_char(ENTER, 1)
sleeep("Czekanie na licencje i menagera", 45)

# unlock
write_char(ENTER, 1)
time.sleep(2)
write_char(ENTER, 1)
sleeep("Odblokowanie po enrolu", 3)

#taryfy
write_char(TAB, 2)
write_char(ENTER, 1)
sleeep("Przeladowanie po odrzuceniu taryf", 15)

# menager kart sim
write_char(TAB, 3)
write_char(ENTER, 1) 
sleeep("Czekanie przed licencja", 6)

#licencja
write_char(ENTER, 1)
time.sleep(5)
write_char(ESCAPE, 3)
print("GOTOWE")
