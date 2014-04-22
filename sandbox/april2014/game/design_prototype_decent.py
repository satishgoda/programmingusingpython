#!/usr/bin/env python

import os
import signal
import argparse

from pprint import pprint as pp

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
        self.modes = None

    def menu(self): return []

    def view(self):
        print('Do you really want to Exit? (y/n)')


class HelpMode(Mode):
    def __init__(self):
        super(HelpMode, self).__init__()
        self.name = "Help"
        self.modes = None

    def menu(self): return []

    def view(self):
        print('This is how you use this application')


class GameMode(Mode):
    def __init__(self):
        super(GameMode, self).__init__()
        self.name = "Game"
        self.modes = None

    def view(self):
        print('Let us play this game')


class MainMode(Mode):
    def __init__(self):
        super(MainMode, self).__init__()
        self.name = "Main"
        self.modes = None

    def view(self):
        print('Welcome to the application')


class Context(object):

    def update(self, next):
        self.parent, self.mode = self.mode, self.modes[next]


class InteractionHandler(object):

    def __init__(self, context):
        self.context = context
        self.updateModes()

    def updateModes(self):
        context = self.context

        parent = context.parent
        mode = context.mode
        self.modes = []
        if parent:
            self.modes.append(parent)
        if mode.modes:
            self.modes.extend(mode.modes)

    def menu(self):
        context = self.context
        menuText = ['{0} //'.format(context.appName)]
        if not context.mode.name == 'Main' and context.parent:
            menuText.append(context.parent.name)
        menuText.extend(context.mode.menu())
        print(' | '.join(menuText))

    def view(self):
        self.context.mode.view()

    def interact(self):
        try:
            what_user_typed = input(">>> ").lower().capitalize()
        except EOFError as eofe:
            return None
        else:
            return what_user_typed

    def update(self, result):
        if result:
            context = self.context
            if result in [mode.name for mode in self.modes]:
                context.update(result)
                self.updateModes()
            else:
                pass

    def __call__(self):
        os.system('clear')

        while True:
            self.menu()
            self.view()
            self.update(self.interact())

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

    game = GameMode()
    modes[game.name] = game
    game.modes = [help]

    main = MainMode()
    main.modes = [game, help, quit]
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
