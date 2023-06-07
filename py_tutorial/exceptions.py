#!/usr/bin/python3
import sys
import traceback
try:
	raise ValueError("Error testing")
except ValueError as tb:
	#print(tb)
	traceback.print_tb(tb.__traceback__)
	pass
