from Controller import Controller

c = Controller()

c.unlock(1)

#c.sleep("Czekam na APN", 3)
#c.write(c.TAB, 4, 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("Ponownie to samo APN", 3)
#c.write(c.TAB, 4, 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("Czekam na start", 3) #zmiejszyc


# start
c.write(c.TAB, 1, 0) # po wipe chyba 1
c.write(c.ENTER, 1, 0)
c.write(c.DOWN_ARROW, 34, 1)
c.sleep("Calm down", 1)
c.write(c.ENTER, 1, 0)
c.write(c.DOWN_ARROW, 51, 1)
c.sleep("Calm down", 1)
c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam po jezyku", 3)
c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Ladowanie sieci", 5)

# Siec

#c.write(c.TAB, 4, 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("Czekam na licencje", 5)
#c.write(c.TAB, 1, 0)
#c.write(c.ENTER, 1, 0)
#c.write(c.TAB, 3, 0) # nie 2?
#c.write(c.ENTER, 1, 0)
#c.sleep("Ladowanie licencji", 3)


# Licencja

c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.write(c.TAB, 6, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Ladowanie dost", 5)


#  uzyc danych kom
#c.write(c.TAB, 1, 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("Sprawdzanie szczegolow", 130)

#Dostarczanie

c.write(c.TAB, 6, 0)
c.sleep("Calm down", 1)
c.write(c.ENTER, 1, 0)
c.write(c.TAB, 3, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na knox", 5)

#potwierdzenie knox cloud
c.write(c.ENTER, 1, 0)
c.sleep("Potwierdzenie, czekanie na wifi", 12)


c.write(c.PAGE_DOWN, 3, 1)
c.sleep("Keep calm", 3)
c.write(c.PAGE_DOWN, 3, 1)
c.write(c.ENTER, 1, 0)
c.sleep("Czekaj na dodanie sieci", 3)

c.sequence("FF Developer", 1)
c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Keep calm", 3)
c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Keep calm", 3)
c.write(c.TAB, 1, 0)
c.sleep("Czekanie na pass", 3)
c.sequence("1gp8ja3mw", 1)
c.write(c.ENTER, 1, 0)

#c.sleep("czekam na wpiecie w siec", 15)
#c.unlock(2)


c.sleep("Ladowanie po wczytaniu sieci", 10)
c.write(c.ESCAPE, 1, 0)
#c.sleep("Czekam na ustawienie kursora", 2)
#c.write(c.DOWN_ARROW, 2, 1)
c.sleep("Czekam na poprzedni ekran", 3)
c.write(c.ENTER, 1, 1)
c.sleep("Czekam na konfiguracje pierwsza", 170)


# Konfiguracja urzadzenia
c.unlock(1)
c.sleep("Keep calm przed klikaniem", 6)
#c.write(c.ESCAPE, 1, 0)
#c.sleep("Keep calm po escape", 6)
c.write(c.TAB, 4, 0) # nie 4?
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na skonfigurowanie urzadzenia i licencje", 50)

#c.unlock(1)
#c.write(c.TAB, 4, 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("teraz konfiguracja urzadzenia", 60) # ???

# kredki
#c.unlock(2)
#c.sleep("Czekam na ustawienie kursora", 10)
#c.sequence("xvc_automat_1", 1)
#c.write(c.TAB, 1, 0)
#c.sleep("Czekam na ustawienie kursora", 5)
#c.sequence("123123123", 1)
#c.write(c.ENTER, 1, 0)
#c.sleep("Czekam na logowanie", 75)

# Akceptowanie licencji knox
c.unlock(2)
#c.sleep("Czekam na licencje", 2)
#c.write(c.ENTER, 1, 0)
#c.sleep("Czekam chwilke na aktywacje", 3)

c.move_down(1500)
c.move_left(800)
c.move_up(120)
c.move_right(150)
c.sleep("Keep calm przed swipe", 1)
c.swipe_up(250)
c.sleep("Czekaj na ikony", 3)

c.move_up(1000)
c.move_down(100)
c.click(1)
c.sleep("Czekaj na wyszukajke", 5)
c.sequence("FAMOC", 0)
c.sleep("Odszukuje", 3)
c.write(c.TAB, 3, 0)
c.write(c.ENTER, 1, 0)

c.sleep("Keep calm, czekam na famoc", 6)
c.move_right(1000)
c.click(1)
c.sleep("Czekam na OK", 3)
c.write(c.TAB, 3, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na popup", 3)
c.write(c.ENTER, 1, 0)
c.write(c.TAB, 3, 0)
c.write(c.ENTER, 1, 0)
c.sleep("FINISH", 1)

