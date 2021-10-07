from Controller import Controller

c = Controller()

c.unlock(1)

c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Ladowanie jezykow", 3)

# jezyk polski
c.write(c.DOWN_ARROW, 40, 1)
c.write(c.ENTER, 1, 0)

c.write(c.DOWN_ARROW, 50, 1)
c.write(c.ENTER, 1, 0)
c.sleep("Ladowanie laczenia z siecia komorkowa", 3)

c.write(c.TAB, 3, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Ladowanie licencji", 3)

c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.write(c.TAB, 15, 1)
c.write(c.ENTER, 1, 0)
c.sleep("Ladowanie wifi", 10)


#potwierdzenie knox cloud
c.write(c.ENTER, 1, 0)
c.sleep("Potwierdzenie, czekanie na wifi", 3)


c.write(c.UP_ARROW, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekanie na siec", 3)
c.sequence("1gp8ja3mw", 1)
c.write(c.ENTER, 1, 0)

c.sleep("Ladowanie po wczytaniu sieci", 10)
c.write(c.DOWN_ARROW, 25, 1)
c.write(c.ENTER, 1, 0)
c.sleep("Czekanie na sprawdzenie szczegolow i knox", 120)


c.unlock(1)
c.write(c.TAB, 4, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na skonfigurowanie urzadzenia", 60)

c.unlock(1)
c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Czekam na pulpit", 60)

# Akceptowanie licencji knox
c.unlock(2)
c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)

c.sleep("FINISH", 1)

