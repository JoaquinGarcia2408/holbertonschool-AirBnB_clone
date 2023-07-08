#!/usr/bin/python3
"""
Console for the project
"""
import cmd
import sys
import os
import shlex
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command line for work in front and backend"""

    prompt = '(hbnb) '
    file = None
    classes = {'BaseModel': BaseModel, 'User': User}

    def emptyline(self):
        """nothing when empty argument and enter"""
        pass

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def help_quit(self):
        print("This function is a door to exit the infinit loop")

    def do_EOF(self, line):
        """ End of file ctrl +d"""
        return True

    def help_EOF(self):
        print("ctrl + d == end of the infinite loop")

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        En este caso se usa el shlex.split, para dividir la
        cadena ingresada al promt al estilo de la shell"""
        if len(args) < 1:
            print("** class name missing **")
            return
        try:
            args = shlex.split(args)
            ninstance = eval(args[0])()
            ninstance.save()
            print(ninstance.id)
        except Exception:
            print("** class doesn't exist **")

    def help_create(self):
        """ information about create"""
        print(" Usage : create BaseModel")

    def do_show(self, argv):
        """Prints the string representation of an
        instance based on the class name and id"""
        enter = argv.split()
        if not enter:
            print("** class name missing **")
        elif enter[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(enter) < 2:
            print("** instance id missing **")
        else:
            key = enter[0] + '.' + enter[1]
            storage.reload()
            if key not in storage.all():
                print("** no instance found **")
            else:
                objects = storage.all()
                if key in objects.keys():
                    print(objects[key])

    def help_show(self):
        """help show"""
        print("Usage: Show BaseModels 1244345345(id)")

    def do_destroy(self, argv):
        """Deletes an instance based on the class name and id"""
        input = shlex.split(argv)
        if not input:
            print("** class name missing **")
        elif input[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(input) < 2:
            print("** instance id missing **")
        else:
            key = input[0] + '.' + input[1]
            storage.reload()
            if key not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(key)
                storage.save()

    def help_destroy(self):
        print("USage: show BaseModel 1234-1234-1234(id)")

    def do_all(self, argv):
        """ do all"""
        input = argv.split()
        if not input:
            b = []
            for o_id in storage.all().keys():
                b.append(str(storage.all()[o_id]))
            print(b)
        elif input[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            list_all = []
            for o_id in storage.all().keys():
                if o_id.split(".")[0] == input[0]:
                    list_all.append(str(storage.all()[o_id]))
            print(list_all)

    def help_all(self):
        """ help for all"""
        print("Usage: all BaseModel\n" "Alternative Usage: all")

    def do_update(self, argv):
        """ update"""
        enter = argv.split()
        if not enter:
            print("** class name missing **")
        elif enter[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(enter) < 2:
            print("** instance id missing **")
        else:
            key = enter[0] + '.' + enter[1]
            storage.reload()
            if key not in storage.all():
                print("** no instance found **")
            elif len(enter) < 3:
                print("** attribute name missing **")
            elif len(enter) < 4:
                print("** value missing **")
            else:
                # setattr(storage.all()[key], enter[2], enter[3])
                storage.all()[key].__dict__[enter[2]] = eval(enter[3])
                storage.save()

    def help_update(self):
        print("Usage:update <class name> <id> <attr name> '<attr value>' ")


if __name__ == '__main__':
    """infinity loops"""
    HBNBCommand().cmdloop()
