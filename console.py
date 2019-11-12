#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage
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
        models = line.split()
        id_ins = False
        if len(models) < 1:
            print("** class name missing **")
        elif  len(models) < 2:
            if not models[0] in base.keys():
                print("** class doesn't exist **")
            else:
                print('** instance id missing **')
        else:
            new_dict = storage.all()
            for key in new_dict.keys():
                nd = key.split(".")
                if models[1] == nd[1]:
                    print(new_dict[key])
                    id_ins = True
            if id_ins is False:
                print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance based on the class name and id"""
        # Splits line by the spaces
        ins =  line.split()
        # Flag
        id_ins = False
        # if no arguments happen
        if len(ins) < 1:
            print("** class name missing **")
        # if you just pass the class name
        elif len(ins) < 2:
        # Compare class name with key of base
            if not ins[0] in base.keys():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        # if the instance of the class name doesn't exist for the id
        else:
            # take all the variables
            new_dict = storage.all()
            # iterate new_dict
            for key in new_dict.keys():
            # splits each key
                nd = key.split(".")
                # if classname is equal a nd remove it
                if ins[1] == nd[1]:
                    id_ins = True
                    del new_dict[key]
                    # save in file json
                    storage.save()
                    return
            # if it does not exist
            if id_ins is False:
                print("** no instance found **")

if __name__ == '__main__':
    # Run a infinithe loop
    HBNBCommand().cmdloop()
