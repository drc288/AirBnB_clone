#!/usr/bin/python3
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
import cmd
"""
HBNBCommand - create command to print a interpreter
for AirBnB
"""
base = {'BaseModel': BaseModel, 'User': User}


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
        """create new object
        use 'create [NAME_OBJECT]'
        """
        try:
            # Verify if base in line exists
            if base[line]:
                # Create new object
                # BaseModel()
                bs = base[line]()
                # Save the file
                storage.new(bs)
                bs.save()
                # Print id
                print(bs.id)
        except KeyError:
            # Exception for KeyError
            if line is "":
                print("** class name missing **")
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """ show the object base the id
        use 'show [NAME_OBJECT] [ID]'
        """
        # Create list of line
        models = line.split()
        # Create a flag
        id_ins = False
        # Verify if len is 0
        if len(models) < 1:
            print("** class name missing **")
        # Verify if len is 1
        elif  len(models) < 2:
            # If is 1, check if the name of model are in
            # base
            if not models[0] in base.keys():
                print("** class doesn't exist **")
            else:
                # If not instance id is missing
                print('** instance id missing **')
        else:
            # Create new dict and get the storage of the obj
            new_dict = storage.all()
            # Iterate key
            for key in new_dict.keys():
                # Split the key
                nd = key.split(".")
                # Verify if the id is equal in the kays
                if models[1] == nd[1]:
                    # Print the value of the key
                    print(new_dict[key])
                    id_ins = True
            # Verify if the flag are False or True
            if id_ins is False:
                print("** no instance found **")

    def do_all(self, line):
        """ all return all attributes of a object
        use 'all [NAME_OBJECT]' - NAME_OBJECT is any name of de object
        """
        # Create new object an put te storage.all()
        # get any objects
        new_dict = storage.all()
        if line is "":
            print("** class doesn't exist **")
        for key in new_dict.keys():
            sp_data = key.split(".")
            if sp_data[0] == line:
                obj = new_dict[key]
                print(obj)

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
                # if classname is equal to nd remove it
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
