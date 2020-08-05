#!/usr/bin/env python3
import sys
import os
import numpy as np
from utility import get_terminal_size
import tty
import termios

class Screen:
	def __init__(self):
		os.system('tput reset')
		os.system('setterm -cursor off')
		self.fd = sys.stdin.fileno()
		self.old_settings = termios.tcgetattr(self.fd)
		tty.setraw(sys.stdin.fileno())
		self.columns,self.rows =  get_terminal_size()
		self.rows-=2
		self.available=self.rows+1
		self.jetpack = np.empty([self.rows,self.columns], dtype='U25')
		self.jetpack[:,:] = " " 

	def s_print(self):
		print('\033[0;0f',end='')
		# os.system('tput reset')
		for i in range(self.rows):
			for j in range(self.columns):
				print(self.jetpack[i][j], end='')
			print('\n\r',end='')

	def s_b_exit(self):
		termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)
		os.system('setterm -cursor on')






