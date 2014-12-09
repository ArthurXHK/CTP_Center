import eventlet
eventlet.monkey_patch()
import tasks

def tttest():
    line = raw_input("input: ")
    while line != 'end':
        print line
        line = raw_input("input: ")


tasks.set_func(tttest)
tasks.main()
