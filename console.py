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
        """Intercepts commands to test for class.syntax()"""
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command
    
    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()
        

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
       
        if line == "" or line is None:
            print("** class name missing **")
            return
        else:
            words = line.split(' ')        
            if words[0] not in HBNBCommand.all_classes:
                print("** class doesn't exist **")
                return
            elif len(words) < 2:
                print("** instance id missing **")        
            else:               
                key = words[0] + '.' + words[1]
                if key not in storage.all():
                    print("** no instance found **")
                    return
                else:
                    print(storage.all()[key])

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
        key = "{}.{}".format(words[0], words[1])
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
