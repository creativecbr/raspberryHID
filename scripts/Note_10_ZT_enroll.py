from Controller import Controller

c = Controller()

c.unlock(1)


# start
c.write(c.TAB, 2, 0) # po wipe chyba 1
c.write(c.ENTER, 1, 0)
c.sleep("Ladowanie sieci", 5)


# Licencja
c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Keep calm", 3)
c.write(c.TAB, 15, 1)
c.write(c.ENTER, 1, 0)


#siec

c.sleep("Potwierdzenie, czekanie na wifi", 6) # byc moze recznie lepiej
c.write(c.UP_ARROW, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekanie na siec", 3)
c.sequence("o:FUhRrY7imk5!GGb82pj", 1)
c.write(c.ENTER, 1, 0)

c.sleep("Ladowanie po wczytaniu sieci", 7)
c.write(c.DOWN_ARROW, 55, 1)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na konfiguracje pierwsza", 100)

# nalezy do org
c.unlock(1)
c.move_down(1500)
c.move_right(1500)
c.sleep("Keep calm", 3)
c.move_up(40)
c.move_left(40)
c.sleep("Czekam sekundke", 2)
c.click(1)
c.sleep("Czekam na skonfigurowanie urzadzenia - sprawdzam dane", 45)

#akceptuje przynaleznosc famoca

c.unlock(1)
c.click(1)
c.sleep("Wlasnie zaakceptowalem to ze jestem Famocowy i na kreciolku czekam na knox lic", 27)


#  licencja
c.move_up(15)
c.click(1)
c.sleep("Czekam po licencji", 200)

c.unlock(1)
c.move_down(15)
c.click(2)
c.sleep("Czekam na ostatni klik", 2)
c.click(1)
c.sleep("Czekam na device is ready!", 50)


# sprawdzam dane po konfie
c.unlock(1)
c.click(1)
c.sleep("Czekam na pulpit ", 15)
c.sleep("FINISH", 1)

