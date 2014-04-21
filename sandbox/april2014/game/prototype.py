#!/usr/bin/env python

import readline
import os


class CloseGame(Exception):
    pass


def quit(context):
    raise CloseGame(context)


def play(context):
    context['score'] += 1


if __name__ == '__main__':
    context = {'score': 0}

    os.system('clear')

    try:
        while True:
            try:
                ui = input("{0}: (score is {1})  >> play >> quit -- $ ".format("Game", context['score']))
            except NameError as ne:
                pass
            except SyntaxError as se:
                pass
            except EOFError as eofe:
                pass
            else:
                ui(context)
            finally:
                os.system('clear')
    except CloseGame as cg:
        print("Your score is {0}".format(cg.args[0]['score']))
        print("Cleaning up game")
    except KeyboardInterrupt as e:
        print("Your score is {0}".format(context['score']))
        print("Abnormal game termination")

