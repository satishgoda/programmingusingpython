#!/usr/bin/env python

running_main = (__name__ == '__main__')

assert running_main, 'You cannot import "{0}" as a module'.format(__name__)

if running_main:
    import os
    import signal
    
    def exit_gracefully(_signal, frame):
        print ('\n {0}'.format(_signal))
        print frame
        raise KeyboardInterrupt
        
    
    signal.signal(signal.SIGINT, exit_gracefully)
    
    os.system('clear')
    
    try:
        while True:
            try:
                p = raw_input("Enter some name> ")
            except EOFError as eof:
                print('^D')
            else:
                if p.lower() in ('clear', 'cls'):
                    os.system('clear')
                else:
                    if p.strip():
                        print(p)
    except KeyboardInterrupt as e:
        pass
    
    print("Bye bye")


