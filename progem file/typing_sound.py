from pynput.keyboard import Listener, Key
from playsound import playsound
import threading
import os

def split_data_in_lost(Nlist):
    result_list = []
    for i in Nlist:
        result_list.append(i.split('=')[1].split('\n')[0])
    return result_list

def sound_setting():
    f = open('Setting.txt','r')
    h = f.readlines()
    return split_data_in_lost(h)

remember = set()
setting_list = sound_setting()
    
def sound_play(check):
    playsound(check)
    
def handlePress( key ):
    setting_list = sound_setting()
    if (key in remember) == False:
        if key == Key.enter:
            t = threading.Thread(target=sound_play, args=(setting_list[0],))
            t.start()
        elif key == Key.shift_l or key == Key.shift_r:
            t = threading.Thread(target=sound_play, args=(setting_list[1],))
            t.start()
        elif key == Key.ctrl_l or key == Key.ctrl_r:
            t = threading.Thread(target=sound_play, args=(setting_list[2],))
            t.start()
        elif key == Key.alt_l or key == Key.alt_r or key == Key.alt or key == Key.alt_gr:
            t = threading.Thread(target=sound_play, args=(setting_list[3],))
            t.start()
        elif key == Key.space:
            t = threading.Thread(target=sound_play, args=(setting_list[4],))
            t.start()
        elif key == Key.tab:
            t = threading.Thread(target=sound_play, args=(setting_list[5],))
            t.start()
        elif key == Key.delete:
            t = threading.Thread(target=sound_play, args=(setting_list[6],))
            t.start()
        elif key == Key.backspace:
            t = threading.Thread(target=sound_play, args=(setting_list[7],))
            t.start()
        elif key == Key.cmd:
            t = threading.Thread(target=sound_play, args=(setting_list[8],))
            t.start()
        elif key == Key.caps_lock:
            t = threading.Thread(target=sound_play, args=(setting_list[9],))
            t.start()
        elif key == Key.esc:
            t = threading.Thread(target=sound_play, args=(setting_list[10],))
            t.start()
        else:
            t = threading.Thread(target=sound_play, args=(setting_list[11],))
            t.start()
        remember.add(key)
 
def handleRelease( key ):
    if (key in remember):
        remember.remove(key)
 
with Listener(on_press=handlePress, on_release=handleRelease) as listener:
    listener.join()

os.system('pause')
