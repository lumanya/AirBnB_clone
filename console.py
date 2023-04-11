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
import re
import json


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
    def precmd(self, line):
        """Intercepts commands to test for class.syntax() and class.all()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        
        if not match:
            return line
        
        if match:
            classname = match.group(1)
            method = match.group(2)
            if classname in HBNBCommand.all_classes:
                command = method + " " + classname              
                self.onecmd(command)                
                return command
            else:
                print("** class doesn't exist **")
                return ""
        
        

    def do_create(self, line):
        '''
        Creates a new instance of BaseModel and save it it to JSON file and
        print id
        '''
        if line == "" or line is None:
            print("** class name missing **")
            return
        else:
            try:
                obj = eval(line)()
                obj.save()
                print(obj.id)
            except NameError:
                print("** class doesn't exist **")
   

    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

   
    def do_create(self, line):
        '''
        Creates a new instance of BaseModel and save it it to JSON file and
        print id
        '''
        if line == "" or line is None:
            print("** class name missing **")
            return
        else:
            try:
                obj = eval(line)()
                obj.save()
                print(obj.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and id."""
        words = line.split()
        if line == "" or line is None:
            print("** class name missing **")
            return
        elif words[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        elif len(words) < 2:
            print("** instance id missing **")        
        objs = storage.all()
        key = words[0] + '.' + words[1]
        if key not in objs:
            print("** no instance found **")
            return
        print(objs[key])

    def do_all(self, line):
        """
        prints all string repersenation of all instances based or not on the
        class name. Ex all BaseModel or all .
        """
        
        if line != "":
            words = line.split(' ')
            if words[0] not in HBNBCommand.all_classes:
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)
       
    def do_count(self, line):
        """ Retrieve the number of instances of a class <class>.count()"""
        if line == "" or line is None:
            print("** class name missing **")
            return
        words = line.split()
        if words[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return 
        objs = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
        print(len(objs))

       

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
        (save the change into the Json file
        """
        if line == "" or line is None:
            print("** class name missing **")
            return
        words = line.split()
        if words[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(words) < 2:
            print("** instance id missing **")
            return
        key = words[0] + '.' + words[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        else:
            del storage.all()[key]
            storage.save()

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
