#!/usr/bin/env python

import os
import signal
import argparse

input = raw_input

class Mode(object):
    name = None
    modes = None

    def __call__(self, *args, **kwargs):
        return self.menu, self.view

    def menu(self):
        return [mode.name for mode in self.modes]

    def view(self): pass


class QuitMode(Mode):
    def __init__(self):
        super(QuitMode, self).__init__()
        self.name = "Quit"

    def menu(self): pass


class HelpMode(Mode):
    def __init__(self):
        super(HelpMode, self).__init__()
        self.name = "Help"

    def menu(self): pass

    def view(self):
        print('This is how you use this application')


class MainMode(Mode):
    def __init__(self):
        super(MainMode, self).__init__()
        self.name = "Main"

    def view(self):
        print('Welcome to the application')


class Context(object):

    def __call__(self):
        return self.parent, self.mode


class InteractionHandler(object):

    def __init__(self, context):
        self.context = context

    def menu(self):
        context = self.context
        menuText = ['{0} //'.format(context.appName)]
        if context.parent:
            menuText.append(context.parent.name)
        menuText.extend(context.mode.menu())
        print(' | '.join(menuText))

    def view(self):
        self.context.mode.view()

    def interact(self):
        try:
            user_typed = input(">>> ")
        except EOFError as eofe:
            return None
        else:
            return user_typed

    def __call__(self):
        os.system('clear')
        while True:
            self.menu()
            self.view()
            result = self.interact()
            if result:
                pass
            else:
                pass
            if not self.context.args.debug:
                os.system('clear')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Console application framework test")

    parser.add_argument('--debug', '-d', action='store_true', help='Enable debugging mode')

    args = parser.parse_args()

    modes = {}

    quit = QuitMode()
    modes[quit.name] = quit

    help = HelpMode()
    modes[help.name] = help

    main = MainMode()
    main.modes = [help, quit]
    modes[main.name] = main

    context = Context()
    context.appName = 'Test'
    context.modes = modes
    context.parent = None
    context.mode = main
    context.args = args

    try:
        InteractionHandler(context)()
    except KeyboardInterrupt as e:
        print('Bye bye')
