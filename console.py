#!/usr/bin/python3
import cmd
"""
Class prube - create command to print a interpreter
"""


class HBNBCommand(cmd.Cmd):
    # Create a prompt hbnb
    prompt = '(hbnb) '
    def do_quit(self, line):
        """Quit command to exit the program
        """
        # Exit the command line
        return True

    def do_EOF(self, line):
        """Quit program
        """
        # Exit program
        return True


if __name__ == '__main__':
    # Run a infinithe loop
    HBNBCommand().cmdloop()
