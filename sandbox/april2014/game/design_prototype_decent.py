#!/usr/bin/env python

import os
import signal
import argparse


# Python 3 compatibility
input = raw_input


class Mode(object):
    def __init__(self):
        self._modes = list()
        self.parent = None

    @property
    def is_top_level(self): return False

    @property
    def modes(self):
        _modes = []

        _modes.extend(self._modes)

        if self.parent:
            _modes.insert(0, self.parent)

        return _modes

    @modes.setter
    def modes(self, submodes):
        self._modes = submodes

    @property
    def menu(self):
        return [mode.name for mode in self.modes]

    def view(self): pass

    def set_parent(self, mode):
        self.parent = mode

    def remove_parent(self):
        self.parent = None


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

    @property
    def is_top_level(self): return True

    def view(self):
        print('Welcome to the application')


class Context(object):

    def update(self, what_user_typed):
        next = self.modes[what_user_typed]

        current = self.mode

        if next.is_top_level or (current.parent is next):
            current.remove_parent()
        elif next in current.modes:
            next.set_parent(current)

        self.mode = next


class InteractionHandler(object):

    def __init__(self, context):
        self.context = context

    def valid_mode(self, what_user_typed):
        return what_user_typed in self.context.mode.menu

    def menu(self):
        context = self.context

        menuText = ['{0} //'.format(context.appName)] + context.mode.menu

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

    def mainloop(self):
        os.system('clear')

        while True:
            self.menu()
            self.view()

            what_user_typed = self.interact()

            if what_user_typed and self.valid_mode(what_user_typed):
                self.update(what_user_typed)

            if not self.context.args.debug:
                os.system('clear')

    def handle_SIGINT(self, signal, frame):
        mode = self.context.mode

        if mode.is_top_level:
            raise KeyboardInterrupt
        else:
            print('\nWARNING: Cannot quit in this mode "{0}"'.format(mode.name))
            raise EOFError


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

    application = InteractionHandler(context)

    signal.signal(signal.SIGINT, application.handle_SIGINT)

    try:
        application.mainloop()
    except KeyboardInterrupt as e:
        print('Bye bye')
