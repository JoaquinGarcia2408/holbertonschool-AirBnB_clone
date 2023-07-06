#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    def emptyline(self):
        """Ignores empty prompts"""
        pass

    def do_EOF(self, line):
        """exit the program"""
        return True

    def do_quit(self, line):
        """exit the program"""
        return True

    prompt = "(hbnb) "

    def help_quit(self):
        """help quit command"""
        print("Quit command to exit the program")
        print("\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
