#!/usr/bin/env python

import os

if __name__ == '__main__':
    os.system('clear')
    
    try:
        while True:
            try:
                p = raw_input("Enter some name> ")
            except Exception as e:
                if isinstance(e, KeyboardInterrupt):
                    print('\n')
                    import sys
                    sys.exit(1)
                elif isinstance(e, EOFError):
                    print('^D')
            else:
                if p.lower() in ('clear', 'cls'):
                    os.system('clear')
                else:
                    if p.strip():
                        print(p)
    except KeyboardInterrupt as e:
        print("\n")
    
    print("Bye bye")


