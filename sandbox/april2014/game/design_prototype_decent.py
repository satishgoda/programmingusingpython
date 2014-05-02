#!/usr/bin/env python

import os
import signal
import argparse
import random


# Python 3 compatibility
input = raw_input


class Mode(object):
    def __init__(self):
        self._modes = list()
        self._parent = None

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
    def modes(self, submodes): self._modes = submodes

    @property
    def menu(self):
        return [mode.name for mode in self.modes]

    def view(self): pass

    @property
    def parent(self): return self._parent

    @parent.setter
    def parent(self, mode):
        self._parent = mode if not(mode is None) else None


class QuitMode(Mode):
    def __init__(self):
        super(QuitMode, self).__init__()
        self.name = "Quit"

    def view(self):
        print('Do you really want to Exit? (y/n)')

    def interact(self, context):
        try:
            what_user_typed = input(">>> ").strip()
        except EOFError as eofe:
            return None
        else:
            if what_user_typed and what_user_typed.lower().startswith('y'):
                import sys
                sys.exit(0)
            else:
                current = context.mode
                context.mode = current.parent
                current.parent = None
                return True 


class HelpMode(Mode):
    def __init__(self):
        super(HelpMode, self).__init__()
        self.name = "Help"

    def view(self):
        print('This is how you use this application')


class GamePlay(object):
    def __init__(self, tries, difficulty):
        self.difficulty = difficulty
        self.total_tries = tries

    def initialize(self):
        self.score = 0
        self.user_tries = 0
        extent = (self.difficulty*3)+1
        self.number_to_guess = random.randint(0, extent)

    def score(self, what_user_typed):
        if what_user_typed == self.number_to_guess:
            self.score += 1

    def to_end_game(self):
        return self.user_tries == self.total_tries


class GameMode(Mode):
    def __init__(self):
        super(GameMode, self).__init__()
        self.name = "Game"
        self.score = 0

    @property
    def not_yet_started(game):
        return not bool(game.score)

    @property
    def progress(game):
        if game.score < 3:
            return True
        else:
            game.score = 0
            return False

    # Display state, message
    # Ended? score (targer Number), message
    def view(game):
        if game.not_yet_started:
            print('Let us play this game')
        else:
            print('Your score is {0}'.format(game.score))

    def interact(game, context):
        try:
            what_user_typed = input(">>> ").strip()
        except EOFError as eofe:
            return None
        else:
            game.score += 1
        finally:
            return game.progress


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
            current.parent = None
        elif next in current.modes:
            next.parent = current

        self.mode = next


class InteractionHandler(object):

    def __init__(self, context):
        self.context = context

    def valid_mode(self, what_user_typed):
        return what_user_typed in self.context.mode.menu

    def update(self, result):
        self.context.update(result)

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

    def mainloop(self):
        os.system('clear')

        while True:
            self.menu()
            self.view()

            mode_interact = getattr(self.context.mode, 'interact', None)

            result = False

            if mode_interact:
                result = mode_interact(context)

            if not result:
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
