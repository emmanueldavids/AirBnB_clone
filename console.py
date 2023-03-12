#!/usr/bin/python3
import cmd
import sys

class Shell(cmd.Cmd):
    #The shell console
    intro = "Shell Console. Type help or ? to list commands.\n"
    prompt = " (hbnb) "
    file = None
    
    def do_EOF(self, line):
        #End Of File to list commands
        'Type help to list commands'
        return True
    
    def do_quit(self, line):
        #To quit the shell console
        'Type quit to exit'
        return True
    
if __name__ == '__main__':
    Shell().cmdloop()