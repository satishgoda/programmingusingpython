#!/usr/bin/env python

import sys
import os
import signal

assert __name__ == '__main__', "One does not simply import a game. One needs to run it"

input = raw_input

class Application(object):
    def __init__(self, name):
        self.name = name
        self.modes = None
        self.actions = {}
        self.actions['quit'] = self.quit

    def quit(self):
        print("{0} application {1}".format("Quitting", self.name))
        sys.exit(0)

    def menu(self):
        menuText = ["{0} | ".format(self.name)]
        if not self.modes:
            menuText.append('{0}'.format("Quit"))
        print(''.join(menuText))

    def user_interaction(self):
        if not self.modes:
            command = input("user says >>> ").strip()
            if not command: return

            if command not in self.actions:
                pass
            else:
                self.actions[command]()

    def execute(self):
        os.system('clear')
        while True:
            self.menu()
            self.user_interaction()
            print('-'*79)
            os.system('clear')

    def handle_signal_SIGINT(self, signal, frame):
        raise KeyboardInterrupt(self)

if __name__ == '__main__':
    app = Application("Test")

    signal.signal(signal.SIGINT, app.handle_signal_SIGINT)

    try:
        app.execute()
    except KeyboardInterrupt as e:
        print("\nApplication {0} exiting..".format(e.args[0].name))

