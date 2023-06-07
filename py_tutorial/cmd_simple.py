#!/usr/bin/python3

import cmd

class HelloWorld(cmd.Cmd):

    def do_greet(self, person):
        '''
        greet [person]
        Greet the named person
        '''
        if person:
            print("hello", line)
        else:
            print('hi')

    def help_greet(self):
        print('\n'.join(['greet [person]', 'Greet the named person']))


    def do_say(self, line):
        '''
        say something to person
        '''
        print(line)

    def do_EOF(self, line):
        '''
        EOF ends cmd session
        '''
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
