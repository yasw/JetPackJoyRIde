#!/usr/bin/env python3
from utility import get_obj
import sys
import os
import config
import numpy as np
from color import color_text
class Enemy:
	def __init__(self,xco,yco):
		self._desc='laser'
		self._v=-1
		self.light = config.light_beam_v
		self.light_beam_v=get_obj(self.light)
		self.light_beam_v=np.array(self.light_beam_v,dtype='object')
		self.xco=xco
		self.yco=yco
		self.light_beam_v = config.COLORS['Fg Gray Bg Yellow'] + self.light_beam_v  + config.Reset
		self.light = config.light_beam_h
		self.light_beam_h=get_obj(self.light)
		self.light_beam_h=np.array(self.light_beam_h,dtype='object')
		self.light_beam_h = config.COLORS['Fg Gray Bg Yellow'] + self.light_beam_h  + config.Reset
		self.light = config.light_beam_x
		self.light_beam_x=get_obj(self.light)
		self.light_beam_x=np.array(self.light_beam_x,dtype='object')
		self.light_beam_x = np.where(self.light_beam_x=='*',config.COLORS['Fg Gray Bg Yellow']+'*'+config.Reset,' ')


	def kill(self,level1_map):
		if (self._v==0):
			level1_map.map_array[self.xco:self.xco+11:1,self.yco:self.yco+2:1]=' '
			level1_map.obj_array[self.xco:self.xco+11:1,self.yco:self.yco+2:1]=' '
		if (self._v==1):
			level1_map.map_array[self.xco:self.xco+2:1,self.yco:self.yco+11:1]=' '
			level1_map.obj_array[self.xco:self.xco+2:1,self.yco:self.yco+11:1]=' '
		if (self._v==2):
			b=10
			# exit()
			for c in range(0,11,1):
				level1_map.obj_array[self.xco+c,self.yco+b]=' '
				b-=1
			b=10
			for c in range(0,11,1):
				level1_map.map_array[self.xco+c,self.yco+b]=' '
				b-=1

