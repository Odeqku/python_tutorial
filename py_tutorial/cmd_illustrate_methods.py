#!/usr/bin/python3

# Set up gnureadline as readline if installed.

try:
	import gnureadline
	import sys
	sys.modules['readline'] = gnureadline

except ImportError:
	pass

import cmd

class Illustrate(cmd.Cmd):
	" Illustrate the base class method use."
	def cmdloop(self, intro=None):
		print('cmdloop({})'.format(intro))
		return cmd.Cmd.cmdloop(self, intro)

	def parseline(self, line):
		print('parseline({!r}) =>'.format(line), end='')
		ret = cmd.Cmd.parseline(self, line)
		print(ret)
		return ret

	def onecmd(self, s):
		print('onecmd({}))'.format(s))
		return cmd.Cmd.onecmd(self, s)

	def emptyline(self):
		print('emptyline()')
		return cmd.Cmd.emptyline(self)

	def default(self, line):
		print('default({})'.format(line))
		return cmd.Cmd.default(self, line)

	def precmd(self, line):
		print('precmd({})'.format(line))
		return cmd.Cmd.precmd(self, line)

	def do_greet(self, person):
		print('hello,', person)

	def do_EOF(self, line):
		"EXIT"
		return True


if __name__ == '__main__':
	Illustrate().cmdloop('Illustrating the methods of cmd.Cmd')
