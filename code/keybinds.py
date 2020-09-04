import keyboard
import threading
from sound import *

hero = None
pressed_key = ""
is_stereo_on = False
key_list = ['', '+k', '+g', '+capslock', '+shift', '+w', '+a', '+s', '+d']


def key_on_press(name):
    global pressed_key
    print(name)
    pressed_key = name


keyboard.on_press(key_on_press)


def stereoKeyBind():
    keyboard.add_hotkey('Ctrl + Alt + Up', soundProfile, args=('/Enable', False))
    keyboard.add_hotkey('Ctrl + Alt + Down', soundProfile, args=('/Disable', True))


def heroKeyBind(count, name):
    keyboard.unhook_all_hotkeys()
    for i in range(count):
        for extra_key in key_list:
            keyboard.add_hotkey('Ctrl + {}{}'.format(i, extra_key),
                                lambda i=i: threading.Thread(target=heroSound, args=(name, i)).start())
