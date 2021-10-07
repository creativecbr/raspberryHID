from Controller import Controller

c = Controller()

c.move_right(100)
c.move_left(100)
c.move_right(100)
c.move_left(100)
c.move_right(100)

c.sleep("FINISH", 1)
