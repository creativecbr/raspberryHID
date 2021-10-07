from Controller import Controller

c = Controller()

c.unlock(1)

c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Ladowanie laczenia z siecia komorkowa", 3)

c.write(c.TAB, 3, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Ladowanie licencji", 3)

c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.write(c.TAB, 15, 1)
c.write(c.ENTER, 1, 0)
c.sleep("Ladowanie wifi", 5)


#potwierdzenie
c.write(c.ENTER, 1, 0)
c.sleep("Potwierdzenie", 3)


c.write(c.UP_ARROW, 1, 0)
c.write(c.ENTER, 1, 0)
c.sequence("1gp8ja3mw", 1)
c.write(c.ENTER, 1, 0)
c.sleep("Ladowanie po wczytaniu sieci", 8)
c.write(c.DOWN_ARROW, 20, 1)
c.write(c.ENTER, 1, 0)
c.sleep("Czekanie na sprawdzenie szczegolow i knox", 160)


c.unlock(1)
c.write(c.TAB, 4, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na skonfigurowanie urzadzenia", 90)

c.unlock(1)
c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na pulpit", 60)

# Akceptowanie licencji knox
c.unlock(2)
c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)

c.sleep("FINISH", 1)

