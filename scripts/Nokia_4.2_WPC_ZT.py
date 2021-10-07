from Controller import Controller
import time

c = Controller()

c.unlock(1)

# jezyki
c.write(c.TAB, 3, 0)
c.write(c.ENTER, 1 , 0)
c.sleep("Czekam na siec komorkowa", 3)


# siec komorkowa
c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na wifi", 10)

#siec wifi
c.write(c.DOWN_ARROW, 25, 0)
c.write(c.UP_ARROW, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam", 3)
c.write(c.DOWN_ARROW, 40, 0)
c.write(c.UP_ARROW, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na podanie sieci", 3)

# podaj siec
c.sequence("FF Developer", 1)
c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na select", 3)

c.write(c.DOWN_ARROW, 3, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na przeladowanie", 3)
c.write(c.TAB, 1, 0)
c.sequence("1gp8ja3mw", 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na blokady, sprawdza dostepnosc aktualizacji", 130)



c.move_right(1500)
c.move_down(1500)
c.move_up(35)
c.move_left(25)
c.sleep("Czekam przed kliknieciem", 2)
c.click(1)
#c.sleep("Przygotowanie profilu pracy", 45)
# urzadzenie nalezy do org
#c.write(c.TAB, 2, 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("Przygotowanie profilu pracy", 45)

# skonfiguruj profil pracy
#c.move_right(1500)
#c.move_down(1500)#
#c.move_up(25)
#c.move_left(15)
#c.sleep("Czekam na kursor", 2)
#c.click(1)
#c.write(c.TAB, 2, 0)
#c.write(c.ENTER, 1, 0)
c.sleep("przygotowuje sie do konfy profilu pracy", 90)
#c.move_right(800)

#c.unlock(1)

c.click(2)
c.sleep("Szykuje profil pracy", 45)
# dodaj konto osobiste aby korzystac

c.click(2)
c.sleep("Konfiguruje profil pracy", 45)

# leci na sprawdzam dane i dostaje google

#google

c.write(c.TAB, 5, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na uslugi google i akceptacje", 25)

# licencje google 

c.write(c.TAB, 10, 0)
c.write(c.ENTER, 2, 1)
c.sleep("Czekam na pulpit", 40)

def search(what):
    c.move_down(1500)
    c.move_right(1000)
    c.move_left(30)
    c.swipe_up(80)
    c.sleep("Czekam na panel", 3)

    c.move_down(90)
    c.swipe_up(50)
    c.sleep("Czekam na panel", 4)
    c.move_up(1500)
    c.move_down(80)
    c.move_right(15)
    c.click(1)
    c.sleep("Czekam na wyszukajke", 3)
    c.click(1)
    c.sleep("Czekaj na wyszukajke 2", 5)
    c.sequence("uuu", 0)
    c.write(c.BACKSPACE, 3, 0)
    c.sleep("Przymierzam sie do " + what, 3)
    c.sequence(what, 0)
    c.write(c.ENTER, 1, 0)
    c.sleep("SZUKAM", 3)
    c.write(c.ENTER, 1, 0)

    #c.move_up(150)
    #c.click(1)
    #c.sleep("Czekam", 1)
    #c.click(1)
    #c.sleep("Czekam znow", 1)
    #c.click(1)
    #c.sleep("Czekam na sluzbowe", 3)

    #c.move_down(80)
    #c.move_left(600)
    #c.move_right(50)
    #c.click(1)
    c.sleep("Czekam na wyszukana apke - " + what, 8)

def refresh_famoc():

    c.move_right(1000)
    c.move_up(1000)
    c.move_down(90)
    c.move_left(30)
    c.click(1)
    c.sleep("Czekam", 8)

def click_back(count):
    c.move_down(1500)
    c.move_left(500)
    c.move_up(10)
    c.move_right(110)
    for i in list(range(count)):
         c.click(1)
         time.sleep(1)

def unlock_swipe():
    c.unlock(1)
    c.move_down(1500)
    c.move_left(500)
    c.move_right(150)
    c.move_up(30)
    c.sleep("Czekamy", 1)
    c.swipe_up(100)
    c.sleep("Czekamy", 3)

def famoc_settings(how):
    unlock_swipe()
    search("ustawi")
    c.write(c.TAB, 2, 0)
    c.write(c.DOWN_ARROW, 3, 0)
    c.write(c.ENTER, 1, 0)
    c.sleep("Czekam na apki", 3)
    c.write(c.UP_ARROW, 3, 0)
    c.sleep("Czekam", 1)
    c.write(c.DOWN_ARROW, 1, 0)
    c.write(c.ENTER, 1, 0)
    c.sleep("Wszystkie apki", 4)
    c.write(c.UP_ARROW, 5, 0)
    c.sleep("Czekaj na cofaanie", 3)
    c.write(c.TAB, 1, 0)
    c.write(c.ENTER, 1, 0)
    c.sleep("Powinienem byc juz w sluzbowych, schodze w dol", 3)
    c.write(c.DOWN_ARROW, how, 0)
    c.write(c.ENTER, 1, 0)
    c.sleep("Witam w ustawieniach famoca", 3)
    c.write(c.ENTER, 1, 0)
    c.sleep("Czekam na Famoczka", 6)
    c.move_right(1500)
    c.move_left(15)
    c.click(1)
    c.sleep("Czekam z odswiezeniem", 3)
    refresh_famoc()

def famoc_notify():
    unlock_swipe()
    c.move_up(2500)
    c.move_down(80)
    c.click(2)
    c.sleep("Czekam na odpalenie FAMOCA", 7)
    c.move_right(1500)
    c.move_left(15)
    c.click(1)
    c.sleep("Czekam na znikniecie menu bara", 3)

def agent_install(agent):

    c.write(c.TAB, 3, 0)
    c.write(c.ENTER, 1, 0)
    c.sleep("Czekaj na popup z instalacją", 8)

    c.write(c.TAB, 1, 0)
    c.write(c.ENTER, 1, 0)
    c.sleep("Daje mu czas na przetworzenie instalacji " + agent, 5)
    refresh_famoc()
    click_back(16)
    c.sleep("Czekam na zainstalowanie sie agenta " + agent, 70)


famoc_settings(2)
c.write(c.TAB, 3, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na popup z instalacja", 6)
c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na suwak", 3)
c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na wyjscie", 3)
click_back(8)
c.sleep("Czekam na nomit o instalacji BA - 1", 70)


famoc_settings(2)
agent_install("BA 1")


famoc_settings(2)
agent_install("RA 1")


famoc_settings(2)
agent_install("LM 1")
c.sleep("FINISH", 2)


#c.sleep("Dodatkowa przerwa na restrykcje i update", 60)

#famoc_notify()
#agent_install("BA 2")


#famoc_notify()
#agent_install("RA 2")


#famoc_notify()
#agent_install("LM 2")

#c.sleep("FINISH", 1)
