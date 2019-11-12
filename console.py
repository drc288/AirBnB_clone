#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):

    def do_EOF(self, line):
        return True

    def do_prompt(self):
        self.prompt = "(hbnb)"

    def do_emptyline(self):
        return cmd.Cmd.emptyline(self)

    def help_quit(slef):
        print("Quit command to exit the program")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
