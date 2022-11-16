import os
from time import sleep
from datetime import datetime
def padre():
    print("----------------------------------------------")
    for i in range(10):
        newPid = os.fork()
        if newPid == 0:
            hijo()
        else:
            pidPadre = os.getpid()
            print("Iniciado el porceso con PID: %d" % (newPid))
            sleep(3)
            print("Termiando el porceso con PID: %d" % (newPid))
            print("----------------------------------------------")
        sleep(7)


def hijo():
    print("Iniciado el poroceso: %d a las" % os.getpid() , datetime.now().hour ,":", datetime.now().minute,":", datetime.now().second)
    os._exit(0)

if __name__ == "__main__":
    padre()