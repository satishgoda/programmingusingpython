#!/usr/bin/env python

import cmd
import os
import sys
import employee


class MyCmd(cmd.Cmd):
    intro = "Command interpreter for my commands"
    ruler = "^"

    def _do_who(self, who):
        """For internal use only

        I really mean it.
        """
        try:
            e = employee.Employee(who)
        except employee.EmployeeDoesNotExistError as e:
            print (e)
        else:
            print('{0}\n    {1}'.format(e, e.title))

    def do_whoami(self, arg):
        """Who am i really?

        What is my login?
        """
        self._do_who(os.getlogin())

    def do_whois(self, arg):
        """Who are they?

        I am always curious about them
        """

        thems = arg.split()

        for them in thems:
            self._do_who(them)

    def do_bye(self, arg):
        """Say bye bye by typing "bye"

        Bye bye bye
        """
        raise KeyboardInterrupt('command "bye"')


if __name__ == '__main__':
    mycmd = MyCmd()
    try:
        mycmd.cmdloop()
    except KeyboardInterrupt as e:
        print('\nProgram interrupted by user with {0}'.format(''.join(e.args) if e.args else '^C'))
