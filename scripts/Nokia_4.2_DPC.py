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
#write_char(ESCAPE, 5)
#time.sleep(3)

# 1 
write_char(TAB, 2)
write_char(ENTER, 1)
time.sleep(3)

# jezyk
write_char(DOWN_ARROW, 25)
write_char(ENTER, 1)
sleeep("Oczekiwanie na ekran pierwszy", 3)

#dalej z pierwszego ekranu
write_char(TAB, 2)
write_char(ENTER, 1)
sleeep("Czekanie na nowy screeen", 3)

# nowy screen
write_char(TAB, 3) 
write_char(ENTER, 1)
time.sleep(3)

#sim 
write_char(TAB, 2)
write_char(ENTER, 1)
time.sleep(3)

#polaczenie 
write_char(TAB, 1)
write_char(ENTER, 1)
sleeep("Czekam na polaczenia wifi", 10)

#wifi
write_char(DOWN_ARROW, 1)
write_char(ENTER, 1)
time.sleep(3)

#klawiatura ekranowa
write_char(TAB, 2)
write_char(ENTER, 1)
sleeep("Czekanie na zalaczenie activity wifi", 4)

#pass
write_sequence("00000000")
write_char(ENTER, 1)
sleeep("Laczenie z wifi", 10)

# po hasle
write_char_fast(DOWN_ARROW, 25)
write_char(ENTER, 1)

sleeep("Aktualizacja", 40) #  aktualizacje

#write_char(ENTER, 1) # mozliwe ze sie nie blokuje, sprawdzic
#sleeep("Odblokowanie po aktualizacji", 3)

# kopiowanie aplikacji i danych
write_char(TAB, 1)
write_char(ENTER, 1)

#  sprawdza dane i idzie do konta google
sleeep("Oczekiwanie na konto google", 65)
write_char(ENTER, 1)
sleeep("Odblokowanie do konta google", 3)

# podaj email
write_char(TAB, 2)
#write_afw()
sleeep("PODAJ MI LOGIN", 20)
write_char(ENTER, 1)
sleeep("Android Enterprise zaraz bedzie", 60)

# unlock
write_char(ENTER, 1)
sleeep("Odblokowanie do zezwolenia na enterprise", 3)

#Enterprise
write_char(TAB, 3)
write_char(ENTER, 1)
sleeep("Przeladowanie po zaakceptowaniu enterprise, pobieranie famoca", 60)

# unlock
write_char(ENTER, 1)
time.sleep(3)
write_char(TAB, 2)
write_char(ENTER, 1)
sleeep("Czekanie na famoca", 60)
time.sleep(3)

# unlock 
write_char(ENTER, 1)
time.sleep(3)
write_char(TAB, 2)
write_char(ENTER, 1)
sleeep("Pobieram informacje o koncie", 60)

#unlock 
write_char(ENTER, 1)
time.sleep(3)

# dokumenty prawne
write_char(TAB, 2)
write_char(ENTER, 1)
write_char(TAB, 4)
write_char(ENTER, 1) 
sleeep("Czekanie przed licencja", 6)

#licencja
write_char_fast(TAB, 24)
write_char(ENTER, 1)
time.sleep(2)
write_char(ENTER, 1)

sleeep("Czekanie na skonfigurowanie launchera", 50)
write_char(ENTER, 1)
write_char(ESCAPE, 3)
print("GOTOWE")
