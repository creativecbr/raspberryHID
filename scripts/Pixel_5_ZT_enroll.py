from Controller import Controller
import time

c = Controller()


c.unlock(1)

#pierwszy ekran
c.write(c.TAB, 4, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Poczekaj na wifi", 12)
c.write(c.UP_ARROW, 20, 1)
c.write(c.ENTER, 1, 0)
c.sleep("Czekaj na popup z wifi", 3)
c.sequence("o:FUhRrY7imk5!GGb82pj", 0)
c.write(c.ENTER, 1, 0)
c.sleep("Przygotowuje telefon", 70)


#to urzadzenie nalezy do twojej organizacji

c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na konfiguracje profilu sluzbowego", 15)

c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na dodaj konto osobiste", 15)

c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na logowanie do google", 15)

c.write(c.TAB, 5, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na licencje googlowe", 15)

c.write(c.TAB, 10, 1)
c.sleep("Czekam przed kliknieciem kontynuj", 3)
c.write(c.ENTER, 2, 0)
c.sleep("Czekaj na blokade ekranu", 15)

# ustaw blokade
c.write(c.TAB, 3, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na popup ze pomijam blokade", 8)
c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na wszystkie aplikacje", 10)

c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam po odznaczeniu", 3)
c.write(c.DOWN_ARROW, 20, 1)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na ciemny motyw", 10)


# ciemny motyw
c.write(c.TAB, 3, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na wyswietl ekran glowny", 5)

c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na przelaczaj aplikacje", 5)

c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekaj na wroc", 5)

c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekaj na asystenta google", 5)

c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na wszystko gotowe", 8)

c.move_down(1500)
c.move_right(1500)
c.sleep("Keep calm", 3)
c.move_left(100)
c.swipe_up(180)

c.sleep("Czekam na pulpit i bajery", 60)


def unlock():
    c.write(c.ENTER, 1, 0)
    c.move_down(2000)
    c.move_right(2000)
    c.move_left(120)
    c.sleep("Czekam", 1)
    c.swipe_up(200)
    c.sleep("Odblokowalem, czekam", 3)

def famoc_work():
    c.swipe_up(70)
    c.sleep("Czekam na menu wysuniete", 3)
    c.move_up(100)
    time.sleep(1)
    c.move_right(105)
    c.sleep("Laduje na sluzbowych", 1)
    c.click(2)
    c.sleep("Pomijam ikonki", 3)
    c.click(1)
    c.sleep("Czekam na ewentualny blad", 3)
    c.click(1)
    c.sleep("Czekam na przejscie w sluzbowe", 3)
    c.move_down(130)
    time.sleep(1)
    c.move_left(130)
    c.sleep("Jestem na famoczku", 2)
    c.click(1)
    c.sleep("Czekam na wlaczenie famoca", 3)

def refresh_famoc():

    c.move_right(2000)
    c.move_up(2000)
    c.move_down(140)
    c.move_left(18)
    c.click(1)
    c.sleep("Czekam na znikniecie okienka", 2)
    c.click(1)
    c.sleep("Odswieza sie", 15)

def accept_permission():
    c.write(c.TAB, 3, 0)
    c.write(c.ENTER, 1, 0)
    c.sleep("Czekam na popup", 2)
    c.write(c.TAB, 1, 0)
    c.write(c.ENTER, 1, 0)
    c.sleep("Czekam na suwak", 3)
    c.write(c.TAB, 1, 0)
    c.write(c.ENTER, 1, 0)
    c.sleep("Czekam po akceptacji", 2)
    c.move_up(2000)
    c.move_left(2000)
    c.move_right(40)
    c.move_down(125)
    c.click(1)
    c.sleep("Czekam na druga strzalke", 3)
    c.click(1)
    c.sleep("Czekam na wyjscie z BA/Ustawien", 3)

def install_agent():
    c.write(c.TAB, 3, 0)
    c.write(c.ENTER, 1, 0)
    c.sleep("Czekam na popup instalacji", 5)
    c.write(c.TAB, 1, 0)
    c.write(c.ENTER, 1, 0)
    c.sleep("Czekam na przetworzenie instalacji", 5)


unlock()
famoc_work()
refresh_famoc()
accept_permission()
c.sleep("Czekam na install BA", 60)


unlock()
famoc_work() # tutaj czy on dobrze aby wchodzi
refresh_famoc()
install_agent()

c.sleep("Czekam po instalacji BA na instalacje RA", 90)

unlock()
famoc_work()
refresh_famoc()
install_agent()

c.sleep("Czekam na instalacje LM", 60)

unlock()
refresh_famoc()
install_agent()

c.sleep("Czekam na instalacje BA numer 2", 60)

unlock()
refresh_famoc()
install_agent()

c.sleep("FINISH", 1)

