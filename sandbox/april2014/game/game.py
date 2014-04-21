#!/usr/bin/env python

import sys
import os
import signal

assert __name__ == '__main__', "One does not simply import a game. One needs to run it"

input = raw_input


class ApplicationMode(object):
    def __init__(self, label, *args):
        self.app = args[0]
        self.app.modes['list'][label] = self


class ApplicationHelpMode(ApplicationMode):
    def __init__(self, *args):
        super(ApplicationHelpMode, self).__init__("Help", *args)

    def view(self):
        print("This is how you use the application")

    def user_interaction(self):
        pass


class ApplicationQuitMode(ApplicationMode):
    def __init__(self, *args):
        super(ApplicationQuitMode, self).__init__("Quit", *args)

    def user_interaction(self):
        print("{0} application {1}".format("Quitting", self.app.name))
        sys.exit(0)


class Application(object):
    def __init__(self, name):
        self.name = name

        self.modes = {}
        self.modes['previous'] = None
        self.modes['current'] = 'app'
        self.modes['list'] = {}

    def menu(self):
        menuText = ["{0} # ".format(self.name)]

        mode = self.modes['current']

        if  mode == 'app':
            modes = self.modes['list']
            others = ' | '.join(modes.keys())
            menuText.append(others)
        else:
            next = self.modes['list'][mode]
            menuText = next.menu()
        print(''.join(menuText))

    def user_interaction(self):
        if self.modes['current'] == 'app':
            try:
                command = input("user says >>> ").strip().capitalize()
            except EOFError as e:
                return
            if not command: return

            mode = self.modes['list'].get(command, None)
            if not mode:
                pass
            else:
                mode.user_interaction()

    def view(self):
        mode = self.modes['current']
        if mode == 'app':
            print("Welcome to this application")


    def execute(self):
        os.system('clear')
        while True:
            self.menu()
            print('-'*79)
            self.view()
            print('-'*79)
            self.user_interaction()
            print('-'*79)
            os.system('clear')

    def handle_signal_SIGINT(self, signal, frame):
        raise KeyboardInterrupt(self)


if __name__ == '__main__':
    app = Application("Test")

    ApplicationHelpMode(app)
    ApplicationQuitMode(app)

    signal.signal(signal.SIGINT, app.handle_signal_SIGINT)

    try:
        app.execute()
    except KeyboardInterrupt as e:
        print("\nApplication {0} exiting..".format(e.args[0].name))

