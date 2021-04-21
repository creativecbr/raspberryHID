# Raspberry as HID device

Autoconfiguration script and simple python controller for emulating mouse/keyboard inputs.

</br>

> Works on: **Raspberry Pi OS 2021-03-04**.
>
> Author: **Pawel Lesniewski**.
>
> Supported OS: **Windows, Linux, Android**.
>
> Version: **1.0.0**.


</br>

## Raspberry configuration

Simple instructions to config raspberry as HID device by setting libcomposite and upload appropriate drivers.

- Clone this repository to your raspberry.
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

___

</br>

## Controller API

Controller.py is a class in **Python3** with methods that enable you to simple use a raspberry hid interface.
Controller support moving and clicking mouse, writing special keys and writing text.

**Important**, you should configure your raspberry at first, if you didn't do it, go to above point - **Raspberry configuration**.

</br>

### Mouse

</br>

Moving mouse cursor by x pixels to **RIGHT**. </br>
**Params:**</br>
*x* - number of pixels to move.
``` 
move_right(int x)
```

</br>

Moving mouse cursor by x pixels to **LEFT**. </br>
**Params:**</br>
*x* - number of pixels to move.
``` 
move_left(int x)
```

</br>

Moving mouse cursor by x pixels to **UP**. </br>
**Params:**</br>
*x* - number of pixels to move.
``` 
move_up(int x)
```

</br>

Moving mouse cursor by x pixels to **DOWN**. </br>
**Params:**</br>
*x* - number of pixels to move.
``` 
move_down(int x)
```

</br>

Clicking mouse left button for x times in actual position. </br>
**Params:**</br>
*x* - how many times mouse should click.
``` 
click(int x)
```

</br>

___

</br>

### Keyboard

</br>

Using Win Key in combination with any character, it can be usefull when we want call special windows.</br>
**Params:**</br>
*x* - a character like "n" which will be combined with Win Key.
``` 
write_win_with_char(char x)
```
</br>

Writing any single character like "a", "5", "C", "#" etc.
It doesn't work with special keys like ENTER, BACKSPACE etc.</br>
**Params:**</br>
*x* - Character which will be clicked, for example "c".</br>
*amount* - How many times character *x* should be writed </br>
*faster* - Integer which takes 0 or 1. For 1 - write will be done faster (*FAST_DELAY*), for 0 and else write will be done with normal speed (*DEFAULT_DELAY*)
``` 
write_char(char x, int amount, int faster)
```
</br>

Writing a sequence of characters on device, for example "afw@account".</br>
**Params:**</br>
*line* - sequence to write on the device.
``` 
sequence(string line)
```
</br>

Writing a special keys on device, like enter, backspace, capslock etc. 
List of available keys is located below.
That function also can write small alphabet characters, numbers, and the like, but for this purpose that you should use *write_char()*.</br>
**Params:**</br>
*char* - special key to write on the device.</br>
*amount* - How many times key *char* should be writed </br>
*faster* - Integer which takes 0 or 1. For 1 - write will be done faster (*FAST_DELAY*), for 0 and else write will be done with normal speed (*DEFAULT_DELAY*)
``` 
write(string char, int amount, int faster)
```
</br>

___

</br>

### Tools and Setters

</br>

Stops main thread of program with logging on every second.
If second parameter is greater than 10, the method will be print log once for 5 seconds. </br>
**Params:**</br>
*title* - Title of log, will be ended by colon. </br>
*seconds* - How many seconds program will be delayed.
``` 
sleep(string title, int seconds)
```

</br>

Setting default delay for clicking and writing. Starting is 0.5 of second.</br>
**Params:**</br>
*newDelay* - New normal(default) delay in double.
```
setDefaultDelay(double newDelay)
```


</br>

Setting fast delay for clicking and writing. Starting is 0.1 of second.</br>
**Params:**</br>
*newDelay* - New fast delay in double.
```
setFastDelay(double newDelay)
```





