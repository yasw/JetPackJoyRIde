#!/usr/bin/env python3
from utility import get_obj
import sys
import os
import config
import numpy as np
from color import color_text

class Bullet:
	def __init__(self,xcor,ycor,level1_map):
		self._desc='bullet'
		self.xco=xcor
		self.start=ycor
		self.yco=ycor
		self.level1_map=level1_map
		self.bullet_d=config.COLORS['Red'] + '>' + config.Reset
		self._killed=0
		self.bullet_c='●'
		self._curve=0



	def kill(self):
		self._killed=1
		self.level1_map.map_array[self.xco,self.yco]=' '