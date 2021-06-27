# Taken from pymotw entry for cmd: https://pymotw.com/3/cmd/

try:
    import gnureadline
    import sys
    sys.modules['readline'] = gnureadline
except ImportError:
    pass

import cmd
print('welcome!') # I put this here for the example.py

class HelloWorld(cmd.Cmd):

    def do_greet(self, person):
        if person:
            print("hi,", person)
        else:
            print('hi')

    def help_greet(self):
        print('\n'.join([
            'greet [person]',
            'Greet the named person',
        ]))

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HelloWorld().cmdloop()
    
