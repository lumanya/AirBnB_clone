#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB
    """
    prompt = '(hbnb) '

    # The do_quit and do_EOF methods are used to exit the program
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    # An empty line + ENTER shouldn't execute anything
    def emptyline(self):
        """Do nothing on an empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
