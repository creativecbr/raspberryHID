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
c.sleep("Ladowanie dostarczania", 5)

# Siec

c.write(c.TAB, 4, 0) # lub 2
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
#c.write(c.TAB, 2, 0)
#c.write(c.ENTER, 1, 0)
c.write(c.TAB, 10, 1) # 9 ?
c.write(c.ENTER, 1, 0)
c.sleep("Ladowanie konfiguracji", 5)


#  uzyc danych kom
#c.write(c.TAB, 1, 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("Sprawdzanie szczegolow", 130)

#Dostarczanie 

c.write(c.TAB, 6, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Keep calm", 3)
c.write(c.TAB, 3, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na wifi", 8)

#potwierdzenie knox cloud

#c.write(c.ENTER, 1, 0)
#c.sleep("Potwierdzenie, czekanie na wifi", 5)

# moze dac mu siec  recznie podawana?

c.write(c.UP_ARROW, 30, 1)
c.sleep("Keep calm", 1)
c.write(c.DOWN_ARROW, 1, 0)
c.sleep("Czekam ze strzalka", 1)
c.write(c.ENTER, 1, 0)
c.sleep("Czekanie na siec", 3)
c.sequence("o:FUhRrY7imk5!GGb82pj", 1)
c.write(c.ENTER, 1, 0)

#c.sleep("czekam na wpiecie w siec", 15)
#c.unlock(2)


c.sleep("Ladowanie po wczytaniu sieci", 29)

#c.sleep("Czekam na ustawienie kursora", 2)
c.write(c.DOWN_ARROW, 30, 1)
c.sleep("Zaczekaj", 1)
c.write(c.DOWN_ARROW, 30, 1)
c.sleep("Zaczekaj", 2)
c.write(c.TAB, 1, 0)
c.sleep("Zaczekaj", 2)
#c.sleep("Czekam na poprzedni ekran", 3)
c.write(c.ENTER, 1, 1)

#c.move_right(600)
#c.move_down(1500)
#c.move_left(50)
#c.move_up(50)
#c.click(1)

c.sleep("Czekam na konfiguracje pierwsza", 120) #120?

#google
c.unlock(1)
c.write(c.TAB, 5, 0) # 4?
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na konfiguracje COSU", 45)
#tutaj juz polityki sie wdrazaja..

# Konfiguracja urzadzenia
#c.unlock(1)
#c.write(c.TAB, 3, 0) # nie 4?
#c.write(c.ENTER, 1, 0)
#c.sleep("Czekam na zgode instalacji", 15)

# ?? 
#c.write(c.TAB, 4, 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("teraz konfiguracja urzadzenia", 60) # ???

#c.write(c.TAB, 2, 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("Czekam na dokonczenie instalacji", 60) # TU SKONCZYLEM

# kredki
#c.unlock(1)
#c.write(c.TAB, 1, 0)
#c.sequence("xvc_automat_1", 0)
#c.write(c.TAB, 1, 0)
#c.sequence("123123123", 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("Czekam na logowanie", 60)

# Akceptowanie licencji knox
#c.unlock(2)
#c.write(c.ENTER, 1, 0)
#c.sleep("Czekam chwilke na aktywacje", 3)

#c.write(c.TAB, 3, 0)
#c.write(c.ENTER, 1, 0)
#c.sleep("Czekam na manager SIM", 3)
# karta sim accept

#c.write(c.TAB, 2, 1)
#c.write(c.ENTER, 1, 0)


c.sleep("FINISH", 1)


