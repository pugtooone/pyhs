# coding: utf-8
import eel
import sys
import pyhs

@eel.expose
def hello():
    print("Hello World")
    
@eel.expose
def getJob():
    x = pyhs.ProductionPlan.get_job_status()
    return x


#Run Eel
if __name__ == '__main__':
    if sys.argv[1] == '--develop':
        eel.init('client')
        eel.start({"port": 3000}, host="localhost", port=8888)
    else:
        eel.init('build')
        eel.start('index.html')
