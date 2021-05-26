# Raspberry hid controller
#
# mouse    on /dev/hidg0
# keyboard on /dev/hidg1
#
# Author: Lesniewski Pawel
# Supported OS: Windows, Linux, Android
# Version 1.0.0

import time



class Controller(object):

    DEFAULT_DELAY = 0.5
    FAST_DELAY = 0.1
    DELAY = DEFAULT_DELAY
    # alphabet
    a = chr(4)
    b = chr(5)
    c = chr(6)
    d = chr(7)
    e = chr(8)
    f = chr(9)
    g = chr(10)
    h = chr(11)
    i = chr(12)
    j = chr(13)
    k = chr(14)
    l = chr(15)
    m = chr(16)
    n = chr(17)
    o = chr(18)
    p = chr(19)
    q = chr(20)
    r = chr(21)
    s = chr(22)
    t = chr(23)
    u = chr(24)
    v = chr(25)
    w = chr(26)
    x = chr(27)
    y = chr(28)
    z = chr(29)

    # numbers and symbols
    n1 = chr(30)  # !
    n2 = chr(31)  # @
    n3 = chr(32)  # #
    n4 = chr(33)  # $
    n5 = chr(34)  # %
    n6 = chr(35)  # ^
    n7 = chr(36)  # &
    n8 = chr(37)  # *
    n9 = chr(38)  # (
    n0 = chr(39) # ) 

    # others symbols
    NULL_CHAR = chr(0)
    MINUS = chr(45) # _
    EQUAL = chr(46) # +
    LSQUARE = chr(47) # {
    RSQUARE = chr(48) # }
    LSLASH = chr(49) # |
    LSLASH_NON = chr(50)  # ~
    SEMICOLON = chr(51) # :
    ASTROPHE = chr(52) # "
    GACCENT = chr(54) # ~
    COMMA = chr(54) # <
    DOT = chr(55) # >
    RSLASH = chr(56) # ?

    # special keys
    ENTER = chr(40)
    ESCAPE = chr(41)
    BACKSPACE = chr(42)
    TAB = chr(43)
    SPACEBAR = chr(44)
    CAPSLOCK = chr(57)
    SCREEN = chr(70)
    PAUSE = chr(72)
    INSERT = chr(73)
    HOME = chr(74)
    PAGE_UP = chr(75)
    DELETE = chr(76)
    END = chr(77)
    PAGE_DOWN = chr(78)
    RIGHT_ARROW = chr(79)
    LEFT_ARROW = chr(80)
    DOWN_ARROW = chr(81)
    UP_ARROW = chr(82)

    # F-KEYS
    F1 = chr(58)
    F2 = chr(59)
    F3 = chr(60)
    F4 = chr(61)
    F5 = chr(62)
    F6 = chr(63)
    F7 = chr(64)
    F8 = chr(65)
    F9 = chr(66)
    F10 = chr(67)
    F11 = chr(68)
    F12 = chr(69)

    def _getChar(self, x):
        return {
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'd': self.d,
            'e': self.e,
            'f': self.f,
            'g': self.g,
            'h': self.h,
            'i': self.i,
            'j': self.j,
            'k': self.k,
            'l': self.l,
            'm': self.m,
            'n': self.n,
            'o': self.o,
            'p': self.p,
            'q': self.q,
            'r': self.r,
            's': self.s,
            't': self.t,
            'u': self.u,
            'v': self.v,
            'w': self.w,
            'x': self.x,
            'y': self.y,
            'z': self.z,
            '1': self.n1,
            '2': self.n2,
            '3': self.n3,
            '4': self.n4,
            '5': self.n5,
            '6': self.n6,
            '7': self.n7,
            '8': self.n8,
            '9': self.n9,
            '0': self.n0,
            '!': "shift1",
            '@': "shift2",
            '#': "shift3",
            '$': "shift4",
            '%': "shift5",
            '^': "shift6",
            '&': "shift7",
            '*': "shift8",
            '(': "shift9",
            ')': "shift0",
            'A': "shifta",
            'B': "shiftb",
            'C': "shiftc",
            'D': "shiftd",
            'E': "shifte",
            'F': "shiftf",
            'G': "shiftg",
            'H': "shifth",
            'I': "shifti",
            'J': "shiftj",
            'K': "shiftk",
            'L': "shiftl",
            'M': "shiftm",
            'N': "shiftn",
            'O': "shifto",
            'P': "shiftp",
            'Q': "shiftq",
            'R': "shiftr",
            'S': "shifts",
            'T': "shiftt",
            'U': "shiftu",
            'V': "shiftv",
            'W': "shiftw",
            'X': "shiftx",
            'Y': "shifty",
            'Z': "shiftz",
            '-': self.MINUS,
            '=': self.EQUAL,
            '[': self.LSQUARE,
            ']': self.RSQUARE,
            '\\': self.LSLASH_NON,
            ';': self.SEMICOLON,
            '"': self.ASTROPHE,
            ',': self.COMMA,
            '.': self.DOT,
            '/': self.RSLASH,
            '_': "shift-",
            '+': "shift=",
            '{': "shift[",
            '}': "shift]",
            '|': "shift\\",
            '~': "shift`",
            ':': "shift;",
            '"': "shift'",
            '<': "shift,",
            '>': "shift.",
            '?': "shift/",
            '`': '`',
            ' ': self.SPACEBAR
                    
        }.get(x, self.SPACEBAR)

    def sleep(self, title, seconds):
        i = 0
        for sec in list(range(seconds)):
            if seconds > 10:
                if i % 5 == 0:
                    print(str(title) + ": " + str(sec+1) + "/" + str(seconds) + " sekund")
            else:
                    print(str(title) + ": " + str(sec+1) + "/" + str(seconds) + " sekund")
            time.sleep(1)
            i = i + 1

    
    def _write_report(self, report):
        with open('/dev/hidg1', 'rb+') as fd:
            fd.write(report.encode())
    
    def _mouse(self, report):
        with open('/dev/hidg0', 'wb+') as fd:
            fd.write(report)

    def move_right(self, x):
        for i in list(range(x)):
            self._mouse(b'\x00\x01\x00')            
        time.sleep(self.FAST_DELAY)
        self._mouse(b'\x00\x00\x00')
    
    def move_left(self, x):
        for i in list(range(x)):
            self._mouse(b'\x00\xfe\x00')            
        time.sleep(self.FAST_DELAY)
        self._mouse(b'\x00\x00\x00')
    
    def move_down(self, x):
        for i in list(range(x)):
            self._mouse(b'\x00\x00\x01')            
        time.sleep(self.FAST_DELAY)
        self._mouse(b'\x00\x00\x00')
    
    def move_up(self, x):
        for i in list(range(x)):
            self._mouse(b'\x00\x00\xfe')            
        time.sleep(self.FAST_DELAY)
        self._mouse(b'\x00\x00\x00')
    
    def click(self, amount):               
        for i in range(amount):
            self._mouse(b'\x01\x00\x00')
            time.sleep(self.FAST_DELAY)
            self._mouse(b'\x00\x00\x00')
            time.sleep(self.FAST_DELAY)
            
    def write_win_with_char(self, char):
        self._write_report(chr(8) + self.NULL_CHAR*7)
        self._write_report(chr(8) + self.NULL_CHAR + char + self.NULL_CHAR*5)
        self._write_report(chr(8) + self.NULL_CHAR*7)
        self._write_report(self.NULL_CHAR*8)
    
    def _write_normal_char(self, char, amount):
        for i in list(range(amount)):        
            self._write_report(self.NULL_CHAR*2 + char + self.NULL_CHAR*5)
            self._write_report(self.NULL_CHAR*8)
            time.sleep(self.DELAY)
            
    def _write_shift_char(self, char, amount):
        for i in list(range(amount)):
            self._write_report(chr(32) + self.NULL_CHAR + char + self.NULL_CHAR*5)
            self._write_report(self.NULL_CHAR*8)
            time.sleep(self.DELAY)

    def unlock(self, number_of_clicks):        
        for i in list(range(number_of_clicks)):
            self.write(self.ESCAPE, 1, 0)
            self.sleep("Unlock " + str(i+1) +" of " + str(number_of_clicks), 3)
        
    def write_char(self, char, amount, faster):
        if faster == 1:
             self._changeDelay()
        type = self._getChar(char)        
        type = type[0:5]
        if type == "shift":
            char = self._getChar(char)[5:6]
            self._write_shift_char(self._getChar(char), amount)
        else:
            self._write_normal_char(self._getChar(char), amount)
        self._restoreDelay()
            
    def sequence(self, sequence, faster):
        self.write_char(sequence[0], 1, 0)
        time.sleep(0.5)
        for i in range(1, len(sequence)):
            self.write_char(sequence[i], 1, faster)        
            
    def _changeDelay(self):
        self.DELAY = self.FAST_DELAY
        
    def _restoreDelay(self):
        self.DELAY = self.DEFAULT_DELAY
                              
    def write(self, char, amount, faster):
        if faster == 1:
            self._changeDelay()
        for i in list(range(amount)):
            self._write_report(self.NULL_CHAR*2 + char + self.NULL_CHAR*5)
            self._write_report(self.NULL_CHAR*8)
            time.sleep(self.DELAY)
        self._restoreDelay()
           
    def setDefaultDelay(self, _delay):
          self.DEFAULT_DELAY = _delay
          self.DELAY = _delay
          
    def setFastDelay(self, _delay):
          self.FAST_DELAY = _delay
          
# Uncomment to test.

#c = Controller()



#c.write_char(c.TAB, 5, 0)

#c.move_up(100)
#c.move_right(50)
#c.move_down(50)
#c.move_left(50)
#c.click(5)



#c.write_win_with_char(c.n)
#c.write_char("5", 5, 0)
#c.write(c.TAB, 5, 0)
#c.sequence("TESting !@12:;", 1)

#c.sleep("Log message", 25)
        
