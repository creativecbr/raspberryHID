# Raspberry as HID device

Autoconfiguration bash script to set appropriate hid drivers and simple python controller for emulating mouse/keyboard inputs.

</br>

> Works on: **Raspberry Pi OS 2021-03-04**.
>
> Author: **FAMOC - by Pawel Lesniewski**.
>
> Supported OS: **Windows, Linux, Android**.
>
> Version: **1.0.0**.


</br>

## Raspberry configuration

Simple instructions to config raspberry as HID device by setting libcomposite and upload appropriate drivers.

- Clone this repository on your raspberry.
- Extract *auto.tar.gz* with autoconfiguration script.
```
tar -xzvf auto.tar.gz 
```
- Go into **autoconfig** folder.
```
cd autoconfig
```
- Make **autoconfig** script as root. Remember that this script will automatically reboot your raspberry!
```
sudo ./autoconfig.sh
```

Now you can connect your device to Raspberry and start simulating!

</br>

## Controller API

Controller.py is a class in **Python3** with methods that enable you to simply use a raspberry hid interface.
Controller support moving and clicking the mouse, writing special keys, and writing text.

**Important**, you should configure your raspberry at first, if you didn't do it, go to the above point - **Raspberry configuration**.

</br>

### Mouse


Moving mouse cursor by x pixels to **RIGHT**. <br>
**Params:**<br>
*x* - number of pixels to move.
``` 
move_right(int x)
```

<br>

Moving mouse cursor by x pixels to **LEFT**. <br>
**Params:**<br>
*x* - number of pixels to move.
``` 
move_left(int x)
```

<br>

Moving mouse cursor by x pixels to **UP**. <br>
**Params:**<br>
*x* - number of pixels to move.
``` 
move_up(int x)
```

<br>

Moving mouse cursor by x pixels to **DOWN**. <br>
**Params:**<br>
*x* - number of pixels to move.
``` 
move_down(int x)
```

<br>

Swipe mouse (keeps mouse button pressed and then moves) to **UP** by x pixels. <br>
**Params:**<br>
*x* - number of pixels to swipe.
``` 
swipe_up(int x)
```

<br>

Clicking mouse left button for x times in actual position. <br>
**Params:**<br>
*x* - how many times mouse should click.
``` 
click(int x)
```

<br>

### Keyboard


Using Win Key in combination with any character, that can be useful when we want to call special methods or windows.</br>
**Params:**</br>
*x* - a character like "n" which will be combined with Win Key.
``` 
write_win_with_char(char x)
```
</br>

Writing only single character like "a", "5", "C", "#", "\\", etc.
It doesn't work with special keys like ENTER, BACKSPACE, F2, etc.</br>
**Params:**</br>
*x* - Character which will be written, for example, "c".</br>
*amount* - How many times character *x* should be written </br>
*faster* - Integer which takes 0 or 1. 
- For 1 - write will be done faster (*FAST_DELAY*), 
- For 0 or else, write will be done with normal speed (*DEFAULT_DELAY*)
``` 
write_char(char x, int amount, int faster)
```
> **For example:**
> ```
> write_char("@", 5, 1)
> ```
</br>

Writing a sequence of characters on the device, for example, "afw@account".</br>
**Params:**</br>
*line* - sequence to write on the device. </br>
*faster* - Integer which takes 0 or 1. 
- For 1 - write will be done faster (*FAST_DELAY*), 
- For 0 or else, write will be done with normal speed (*DEFAULT_DELAY*)
``` 
sequence(string line, int faster)
```
</br>

Writing special keys on the device, like enter, backspace, caps lock, etc. That method will work correctly only with that keys. The list of available keys is located below.
</br>
**Params:**</br>
*key* - special key to write on the device.</br>
*amount* - How many times *key* should be written </br>
*faster* - Integer which takes 0 or 1. 
- For 1 - write will be done faster (*FAST_DELAY*), 
- For 0 or else, write will be done with normal speed (*DEFAULT_DELAY*)
``` 
write(const key, int amount, int faster) 
```
> **For example:**
> ```
> write(controllerObject.TAB, 2, 0)
> ```

</br>

### Tools and Setters

Stops main thread of program with logging on every second. If the second parameter is greater than 10, the method will print a log once for 5 seconds. </br>
**Params:**</br>
*title* - Title of the log, will be ended by a colon. </br>
*seconds* - On how many seconds the program will be delayed.
``` 
sleep(string title, int seconds)
```

</br>

Methods help with unlocking devices without pin/passcode.
It clicks ESCAPE and then waits three seconds to wake up. </br> Allows one parameter *number_of_clicks*, which repeats the mentioned sequence. </br>
**Params:**</br>
*number_of_clicks* - Describes how many times operation click and wait should be repeated, integer. </br>
``` 
unlock(int number_of_clicks)
```

</br>

Setting default delay for clicking and writing in seconds. </br>On start value is 0.5 [sec].</br>
**Params:**</br>
*newDelay* - New normal(default) delay in seconds, type double.
```
setDefaultDelay(double newDelay)
```

</br>

Setting fast delay for clicking and writing in seconds. </br>On start value is 0.1 [sec].</br>
**Params:**</br>
*newDelay* - New fast delay in seconds, type double.
```
setFastDelay(double newDelay)
```

</br>

## Supported keys & characters

Names of fields in Controller class are on the left side, whereas their descriptions on the right side.

### Keys: 
- ENTER - enter, 
- ESCAPE - esc, escape,
- BACKSPACE - backspace, 
- TAB - tabulator,
- SPACEBAR - spacebar,
- CAPSLOCK - caps lock,
- SCREEN - print screen,
- PAUSE - pause,
- INSERT - insert,
- HOME - home,
- PAGE_UP - page up,
- DELETE - delete,
- END - end,
- PAGE_DOWN - page down,
- RIGHT_ARROW - right arrow,
- LEFT_ARROW - left arrow,
- DOWN_ARROW - down arrow,
- UP_ARROW - up arrow,
- F1 → F12 - functional keys.

### Characters:
- [a-z]
- [A-Z]
- [0-9]
- [ @ # $ % ^ & * ( ) _ + ]
- [ { } | : " < > ? ]
- [ [ ] \ ; ' , . / ]


## Documentation 

- [Unibersal Serial Bus HID Usage Table](https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf)
- [Composite USB gadget configs](https://wiki.tizen.org/USB/Linux_USB_Layers/Configfs_Composite_Gadget/Usage_eq._to_g_hid.ko)
- [USB gadget configs](https://www.kernel.org/doc/Documentation/usb/gadget_configfs.txt)
- [USB gadget configs testing](https://www.kernel.org/doc/Documentation/ABI/testing/configfs-usb-gadget)
- [Serial driver](https://www.kernel.org/doc/Documentation/usb/gadget_serial.txt)
- [Raspberry documentation](https://www.raspberrypi.org/documentation/)
- [isticktoit tutorial](https://www.isticktoit.net/?p=1383)


