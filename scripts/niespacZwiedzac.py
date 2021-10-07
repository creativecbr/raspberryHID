from Controller import Controller

c = Controller()

c.move_right(100)
c.move_left(100)
c.move_right(100)
c.move_left(100)
c.move_right(100)
c.move_up(500)
c.move_right(200)
c.move_down(500)
c.move_down(300)
c.move_left(300)
c.move_down(150)

c.sleep("FINISH", 1)

