#!/usr/bin/python

import cmd
import argparse

from employee import Employee
from employee import EmployeeDoesNotExistError


class WhoCmd(cmd.Cmd):
    intro = "Welcome to the who program"
    ruler = '-'

    # Command action
    def do_bye(self, args):
        """Get out of the interpreter"""
        return True

    def do_whois(self, args):
        """Information about users

      whois user1 user2 user3

      This method queries the employee database
      """

        loginnames = args.split()

        for loginame in loginnames:
            try:
                employee = Employee(loginame)
            except EmployeeDoesNotExistError as emp:
                print(emp)
            else:
                print("{0}\n   {1}".format(employee.uname, employee.title))
            finally:
                print("Good")

    def help_bye(self):
        print """bye bye

        Good riddance

        sdkfjsdlkfj
        """

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=WhoCmd.intro)

    args = parser.parse_args()

    w = WhoCmd()

    try:
        w.cmdloop()
    except KeyboardInterrupt as e:
        print("Caught Exception ^C")
        print(e)
