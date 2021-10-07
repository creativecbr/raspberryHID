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
c.write(c.TAB, 15, 1)
c.write(c.ENTER, 1, 0)
#c.sleep("Ladowanie knox", 5)


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
c.sleep("Potwierdzenie, czekanie na wifi", 10)
c.write(c.UP_ARROW, 1, 0)
#c.write(c.DOWN_ARROW, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekanie na siec", 3)
c.sequence("o:FUhRrY7imk5!GGb82pj", 1)
c.write(c.ENTER, 1, 0)

#c.sleep("czekam na wpiecie w siec", 15)
#c.unlock(2)


c.sleep("Ladowanie po wczytaniu sieci", 10)
c.write(c.DOWN_ARROW, 20, 1)
#c.sleep("Czekam na ustawienie kursora", 2)
#c.write(c.DOWN_ARROW, 2, 1)
#c.sleep("Czekam na poprzedni ekran", 3)
#c.write(c.TAB, 17, 1)
c.write(c.ENTER, 1, 1)
c.sleep("Czekam na konfiguracje pierwsza", 60)

# kopiowanie danych
#c.unlock(1)
c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na skonfigurowanie urzadzenia - sprawdzam dane", 70)

# wysyp ostatni sprawdzam d

c.unlock(1)
c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na konfiguracje druga", 18)

# 
#c.unlock(2)
c.write(c.TAB, 3, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na konfiguracje ZT  z wygaszeniem", 150)
#c.sleep("Zaaktualizowanie knox", 5)
#c.sleep("Czekam na manager SIM", 3)
# karta sim accept

#c.write(c.TAB, 2, 1)
#c.write(c.ENTER, 1, 0)

# licencja
c.unlock(2)
c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na konfigurujemy reszte", 5)

# konfigurujemy reszte
c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na reszte konfiguracji", 90)

# googel
c.unlock(2)
c.write(c.TAB, 6, 1)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na okno gooogle", 3)
c.write(c.ENTER, 1, 0)
c.sleep("Licencje googlowe ladowanie", 10)
c.write(c.TAB, 10, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na potwierdzenie google", 1)
c.write(c.ENTER, 1, 0)
c.sleep("Ochrona telefonu", 5)

c.write(c.DOWN_ARROW, 15, 1)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na ostatni ekran", 3)

c.write(c.TAB, 1, 0)
#c.sleep("Przeladowanie", 2)
c.write(c.ENTER, 1, 0)
c.sleep("Konczenie", 90)

c.unlock(2)
c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Zaczekaj na launcher", 15)


c.sleep("FINISH", 1)


