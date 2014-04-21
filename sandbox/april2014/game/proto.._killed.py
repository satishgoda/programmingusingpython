#!/usr/bin/env python

assert __name__ == '__main__', "One does not simply import a game. One needs to run it"


class Application(object):
    pass


class ApplicationMode(object):
    pass


class Help(ApplicationMode):

    def display(self, context):
        print ("Just type 'play' and press enter to play")


class Game(ApplicationMode):

    def display(self, context):
        print ("Play the game")


class Context(object):
    pass



context = Context()
context.current = 'menu'
context.previous = None


app = Application()

app.context = context

Application.run()
