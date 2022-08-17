# coding: utf-8
import eel
import sys
from pyhs import JobDir


@eel.expose
def hello():
    print('hello')

@eel.expose
def set():
    pass



if __name__ == '__main__':
    if sys.argv[1] == '--develop':
        eel.init('client')
        eel.start({"port": 3000}, host="localhost", port=8888)
    else:
        eel.init('build')
        eel.start('index.html')
