# coding: utf-8
import eel
import sys


@eel.expose
def connection():
    print("Connection Between python and javascript is working")
 

#Run Eel
if __name__ == '__main__':
    if sys.argv[1] == '--develop':
        eel.init('client')
        eel.start({"port": 3000}, host="localhost", port=8888)
    else:
        eel.init('build')
        eel.start('index.html')
