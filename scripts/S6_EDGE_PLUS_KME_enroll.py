from Controller import Controller

c = Controller()


c.unlock(1)

#start
c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Wait for next screen", 5)

c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Wait for dialog", 5)
c.write(c.ENTER, 1, 0)
c.sleep("Wait for wifi", 5)

#wifi
c.write(c.TAB, 3, 1)
c.write(c.PAGE_DOWN, 2, 1)
c.move_down(1000)
c.move_up(50)
c.click(1)
c.sleep("Adding wifi, please wait", 3)
c.sequence("00Testers", 1)
c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Easy boy, wait a sec", 3)
c.write(c.TAB, 2, 0)
c.write(c.ENTER, 1, 0)
c.write(c.TAB, 1, 0)
c.sleep("Wait for pass",3)
c.sequence("o:FUhRrY7imk5!GGb82pj", 1)
c.write(c.ENTER, 1, 0)
c.write(c.TAB, 4, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Wait for connection", 15)
c.write(c.TAB, 3, 1)
c.write(c.PAGE_DOWN, 2, 1)
c.write(c.TAB, 1, 1)
c.write(c.ENTER, 1, 0)

#agreements
c.sleep("Wait for agreements screen", 5)
c.write(c.TAB, 9, 0)
c.write(c.ENTER, 1, 0)
c.write(c.TAB, 1, 0)
c.write(c.ENTER, 1, 0)
c.sleep("Wait for KME", 60)

#KME enroll
c.write(c.TAB, 3, 0)
c.write(c.ENTER, 1, 0)
c.move_down(1000)
c.move_right(1000)
c.move_up(20)
c.move_left(20)
c.click(1)
c.sleep("Wait for KME configuration",90)
c.sleep("FINITO! :)", 1)