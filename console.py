#!/usr/bin/env python3
"""
 console module contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB
    """
    prompt = '(hbnb) '

    all_classes = [
        'BaseModel',
        'User',
        'State',
        'City',
        'Place',
        'Review',
        'Amenity'
    ]
    attr = ['created_at', 'id', 'updated_at']

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program\n'
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, cls):
        '''
        Creates a new instance of BaseModel and save it it to JSON file and
        print id
        '''
        if cls == "":
            print("** class name missing **")
            return
        else:
            try:
                obj = eval(cls)()
                obj.save()
                print(obj.id)
            except NameError:
                print("** class doesn't exists **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + '.' + args[1]
        if key not in objs:
            print("** no instance found **")
            return
        print(objs[key])

    def do_all(self, args):
        """
        prints all string repersenation of all instances based or not on the
        class name. Ex all BaseModel or all .
        """
        if not args:
            print([str(obj) for obj in storage.all().values()])
            return
        else:
            args_list = args.split()
            if args_list[0] not in HBNBCommand.all_classes:
                print("** class doesn't exists **")
                return
            else:
                print([str(obj) for obj in storage.all().values()])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
        (save the change into the Json file
        """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        if arg_list[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = arg_list[0] + '.' + arg_list[1]
        if key not in objs:
            print("** no instance found **")
            return
        del objs[key]

    def do_update(self, args):
        """ update an instance based on the class name and id by adding
        or updating attribute (save the chnage into JSON file)
        """
        if not args:
            print("** class name missing **")
            return
        arg = args.split()
        if arg[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = arg[0] + '.' + arg[1]
        if key not in objs:
            print("** no instance found **")
            return
        if len(arg) < 3:
            print("** attribute name missing **")
            return
        if len(arg) < 4:
            print("** value missing **")
            return
        obj = objs[key]
        attr_name = arg[2]
        attr_val = arg[3].strip('"')

        attr_type = type(getattr(obj, attr_name, None))
        try:
            attr_val = attr_type(attr_val)
        except (ValueError, TypeError):
            pass
        if attr_val.isdigit():
            attr_val = int(attr_val)
        setattr(obj, attr_name, attr_val)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
