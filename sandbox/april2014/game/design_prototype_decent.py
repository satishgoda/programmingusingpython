#!/usr/bin/env python

import os
import signal
import argparse

from pprint import pprint as pp

input = raw_input

class Mode(object):

    def __init__(self):
        self.modes = list()
        self.parent = None

    def menu(self): return self.modes

    def __call__(self, *args, **kwargs):
        return self.menu, self.view

    @property
    def is_top_level(self):
        return False

    def has_sub_modes(self):
        return len(self.modes)

    def menu(self):
        return [mode.name for mode in self.modes]

    def view(self): pass


class QuitMode(Mode):
    def __init__(self):
        super(QuitMode, self).__init__()
        self.name = "Quit"

    def view(self):
        print('Do you really want to Exit? (y/n)')


class HelpMode(Mode):
    def __init__(self):
        super(HelpMode, self).__init__()
        self.name = "Help"

    def view(self):
        print('This is how you use this application')


class GameMode(Mode):
    def __init__(self):
        super(GameMode, self).__init__()
        self.name = "Game"

    def view(self):
        print('Let us play this game')


class MainMode(Mode):
    def __init__(self):
        super(MainMode, self).__init__()
        self.name = "Main"
        self.modes = None

    @property
    def is_top_level(self):
        return True

    def view(self):
        print('Welcome to the application')


class Context(object):

    def update(self, next):
        next = self.modes[next]

        current = self.mode

        if next.is_top_level or current.parent is next:
            current.parent = None
        elif next in current.modes:
            next.parent = current

        self.mode = next


class InteractionHandler(object):

    def __init__(self, context):
        self.context = context
        self.updateModes()

    def updateModes(self):
        context = self.context
        mode = context.mode
        parent = mode.parent

        self.modes = []

        if parent:
            self.modes.append(parent)

        if mode.modes:
            self.modes.extend(mode.modes)

    def valid_mode(self, what_user_typed):
        return what_user_typed in [mode.name for mode in self.modes]

    def menu(self):
        context = self.context
        mode = context.mode

        menuText = ['{0} //'.format(context.appName)]

        if (not mode.is_top_level) and mode.parent:
            menuText.append(mode.parent.name)

        menuText.extend(mode.menu())

        print(' | '.join(menuText))

    def view(self):
        self.context.mode.view()

    def interact(self):
        try:
            what_user_typed = input(">>> ").strip()
        except EOFError as eofe:
            return None
        else:
            return what_user_typed and what_user_typed.lower().capitalize()

    def update(self, result):
        self.context.update(result)
        self.updateModes()

    def __call__(self):
        os.system('clear')

        while True:
            self.menu()
            self.view()

            what_user_typed = self.interact()

            if what_user_typed and self.valid_mode(what_user_typed):
                self.update(what_user_typed)

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
    context.mode = main
    context.args = args

    try:
        InteractionHandler(context)()
    except KeyboardInterrupt as e:
        print('Bye bye')
