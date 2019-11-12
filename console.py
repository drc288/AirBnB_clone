#!/usr/bin/python3
from models.base_model import BaseModel
import cmd
"""
HBNBCommand - create command to print a interpreter
for AirBnB
"""
base = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):

    # Create a prompt hbnb
    prompt = '(hbnb) '
    def do_quit(self, line):
        """Quit command to exit the program
        """
        # Exit the command line
        return True

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        # Exit program
        return True

    def do_create(self, line):
        try:
            if base[line]:
                bs = base[line]()
                bs.save()
                print(bs.id)
        except KeyError:
            if line is "":
                print("** class name missing **")
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        try:
            for data in line:
                print(data)
        except:
            pass






if __name__ == '__main__':
    # Run a infinithe loop
    HBNBCommand().cmdloop()
