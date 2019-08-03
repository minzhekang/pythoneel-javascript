import eel
import sys

eel.init('web')


#cow = sys.argv[1] # this is the first argument from sys, 0 is the file dir.

@eel.expose
def printme(cow ,duck):
    print('This is in python ' + cow + ' ' + duck)
    return ('You have sent me ' + cow + ' ' + duck)
    

try:
    eel.start('main.html', size = (800,800))
except (SystemExit):
    pass


