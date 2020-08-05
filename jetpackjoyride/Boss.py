from utility import get_obj
import numpy as np
import config
from utility import get_terminal_size
from time import sleep


class Boss:
	def __init__(self,xco,yco):
		self._desc='boss'
		self.boss = config.boss_v
		self.boss=get_obj(self.boss)
		self.boss=np.array(self.boss)
		self.__lives=3
		self.xco=xco
		self.yco=yco
	def kill(self):
		self.__lives-=1

	def get_lives(self):
		return self.__lives