#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    def do_EOF(self, line):
        return True
        "exit the program"

    def do_quit(self, line):
        return True
        "exit the program"
    
    prompt = "(hbnb)"

    def help_quit(self):
        print("Quit command to exit the program")
        print ("\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()