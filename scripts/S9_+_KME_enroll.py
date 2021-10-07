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
c.write(c.TAB, 2, 0) # po wipe chyba 1
c.write(c.ENTER, 1, 0)
c.sleep("Ladowanie sieci", 5)

# Siec

c.write(c.TAB, 3, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na licencje", 5)
#c.write(c.TAB, 1, 0)
#c.write(c.ENTER, 1, 0)
#c.write(c.TAB, 3, 0) # nie 2?
#c.write(c.ENTER, 1, 0)
#c.sleep("Ladowanie licencji", 3)


# Licencja
c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Keep calm", 3)
c.write(c.TAB, 15, 1)
c.write(c.ENTER, 1, 0)
c.sleep("Ladowanie knox", 5)


#  uzyc danych kom
#c.write(c.TAB, 1, 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("Sprawdzanie szczegolow", 130)

#Dostarczanie 

#c.write(c.TAB, 6, 0)
#c.write(c.ENTER, 1, 0)
#c.write(c.TAB, 3, 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("Czekam na knox", 5)

#potwierdzenie knox cloud
c.write(c.ENTER, 1, 0)
c.sleep("Potwierdzenie, czekanie na wifi", 5)

# siec 00Testers
c.write_shift(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na okno - Dodaj siec", 3)
c.sequence("FF Developer", 1)
c.sleep("Czekam po wprowadzeniu", 3)
c.write(c.TAB, 1, 0)
c.sleep("Keep calm", 2)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na WPA2", 2)
c.write(c.TAB, 2, 0)
c.sleep("Keep calm", 2)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na input hasla", 5)
c.write(c.TAB, 2, 0)
c.sleep("Czekam na wprowadzenie", 2)
c.sequence("1gp8ja3mw", 1)
c.write(c.ENTER, 1, 0)


#c.sleep("czekam na wpiecie w siec", 15)
#c.unlock(2)


c.sleep("Ladowanie po wczytaniu sieci", 12)
c.write(c.ESCAPE, 1, 0)
#c.sleep("Czekam na ustawienie kursora", 2)
#c.write(c.DOWN_ARROW, 2, 1)
c.sleep("Czekam na poprzedni ekran", 3)
c.write(c.TAB, 17, 1)
c.sleep("Keep calm", 2)
c.write(c.ENTER, 1, 1)
c.sleep("Czekam na konfiguracje pierwsza", 140)


# Konfiguracja urzadzenia bo nalezy do org
c.unlock(1)
c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na przygotowanie profilu pracy", 25 )

c.write(c.TAB, 4, 0) # nie 5?
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na skonfigurowanie urzadzenia", 60)

c.unlock(2)
c.write(c.TAB, 1, 0)
c.sequence("xvc_automat", 1)
c.sleep("Keep calm", 3)
c.write(c.TAB, 1, 0)
c.sequence("123123123", 1)
c.write(c.ENTER, 1, 0)
c.sleep("Czekaj na pass", 5)
c.write(c.ENTER, 1, 0)

c.sleep("Czekaj na knox", 90)
c.unlock(2)
c.sleep("Czekaj sekunde na knox dluzej", 3)
c.write(c.ENTER, 1, 0)

c.sleep("Czekam na gotowe", 2)
c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
#c.sleep("Czekaj na knoxa", 45)

# knox after changes
#c.unlock(2)
#c.move_up(1000)
#c.move_down(90)
#c.click(1)
#c.move_right(30)
#c.click(1)
#c.move_right(30)
#c.click(2)
#c.move_right(30)
#c.click(1)

#c.sleep("Czekaj na famoca", 6)

#c.write(c.TAB, 3, 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("Czekaj na popup z knox", 3)

#c.write(c.ENTER, 1, 0)

#c.sleep("Czekam sekundke na wyjscie z Famoca", 5)
#c.move_right(1500)
#c.move_down(2000)
#c.move_left(20)
#c.move_up(10)
#c.click(3)
#c.sleep("Czekam na wyjscie z apki i zablokowanie telefonu", 60)

# knox after changes second attempt
#c.unlock(2)
#c.move_up(1000)
#c.move_down(90)
#c.click(1)
#c.move_right(30)
#c.click(1)
#c.move_right(30)
#c.click(2)
#c.move_right(30)
#c.click(1)

#c.sleep("Czekaj na famoca", 6)

#c.write(c.TAB, 3, 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("Czekaj na popup z knox", 3)

#c.write(c.ENTER, 1, 0)




c.sleep("FINISH", 1)


