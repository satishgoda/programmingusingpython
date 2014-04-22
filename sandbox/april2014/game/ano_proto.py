

class ApplicationState(object):
    pass


# The state that displays help
# Can be accessed from MainState and GameState
class HelpState(ApplicationState):
    pass


# The actual game to be played
class GameState(ApplicationState):
    pass


# The state where User information is collected
# This user information is used just before the game starts or after
#     the game ends so as to record the score
class GameUserState(ApplicationState):
    pass


# This state gracefully exits the application
# Saves anything that needs to be saved
class QuitState(ApplicationState):
    pass


class ApplicationMode(object):
    pass


class MainMode(ApplicationMode):
    pass


class HelpMode(ApplicationMode):
    pass


class GameMode(ApplicationMode):
    pass


# The application class that is the starting point for all the action.
class Application(object):
    def mainloop(self):
        mode = self.context.mode
        mode.menu()
        mode.view()
        mode.interaction()


if __name__ == '__main__':
    app = Application("Test")


    # Application must handle process level interrupts SIGINT
    try:
        app.mainloop()
    except KeyboardInterrupt as e:
        pass

