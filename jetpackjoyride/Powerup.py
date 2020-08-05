#!/usr/bin/env python3
from utility import get_obj
import sys
import os
import config
import numpy as np
from color import color_text
class Powerup():
	def __init__(self,xco,yco,level1_map):
		self.xco=xco
		self.yco=yco
		self.level1_map=level1_map


class Killable():
	def __init__(self,xco,yco,level1_map):
		self.xco=xco
		self.yco=yco
		self.level1_map=level1_map	

	def kill(self):
		self.level1_map.map_array[self.xco,self.yco]=' '	

class Speed(Powerup):
	"""docstring Speed"""
	def __init__(self,xco,yco,level1_map):
		super().__init__(xco,yco,level1_map)
		self._desc='speed'
		self.speed_d=config.COLORS['Green'] + '+' + config.Reset

		
class Shield(Powerup):
	def __init__(self,xco,yco,level1_map):
		super().__init__(xco,yco,level1_map)		
		self._desc='shield'
		self.shield_d=config.COLORS['Purple'] + '^' + config.Reset

class Coin(Killable):
	def __init__(self,xco,yco,level1_map):
		super().__init__(xco,yco,level1_map)
		self._desc='coin'
		self.coin_d=config.COLORS['Green'] + '$' + config.Reset

	def kill(self):
		super().kill()
		self.level1_map.obj_array[self.xco,self.yco]=' '

class Boss(Powerup):
	def __init__(self,xco,yco,level1_map):
		super().__init__(xco,yco,level1_map)
		self._desc='boss'
		self.boss = config.boss_v
		self.boss=get_obj(self.boss)
		self.boss=np.array(self.boss)
		self.__lives=4
	def kill(self):
		self.__lives-=1

	def get_lives(self):
		return self.__lives

class Bullet(Killable):
	def __init__(self,xcor,ycor,level1_map):
		super().__init__(xcor,ycor,level1_map)
		self._desc='bullet'
		self.start=ycor
		self.bullet_d=config.COLORS['Red'] + '>' + config.Reset
		self._killed=0
		self.bullet_c='●'
		self._curve=0



	def kill(self):
		super().kill()
		self._killed=1


class Magnet(Powerup):
	def __init__(self,xco,yco,level1_map):
		super().__init__(xco,yco,level1_map)		
		self._desc='magnet'
		self.magnet_d=config.COLORS['Purple'] + 'M' + config.Reset
