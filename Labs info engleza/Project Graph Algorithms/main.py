from ui import UI
import sys
import threading

sys.setrecursionlimit(400000)
threading.stack_size(2**27)

def startMain():
    ui = UI()
    ui.start()

threading.Thread(target=startMain).start()

