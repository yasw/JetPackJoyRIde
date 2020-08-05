from utility import get_obj
import numpy as np
import config
from utility import get_terminal_size
from time import sleep
import time

class Mando:
	def __init__(self,xcord,ycord,col,in_map):
		self._desc='mando'
		self.player = config.player
		self.man=get_obj(self.player)
		self.man=np.array(self.man)
		self.xco = xcord
		self.player_s = config.player_s
		self.man_s=get_obj(self.player_s)
		self.man_s=np.array(self.man_s)
		self.ground = xcord
		self.right=col
		self.yco = ycord
		self.gravity=0
		self.__lives=5
		self.__coins=0      
		self.in_map=in_map
		self.speed=0
		self._shield='of'
		self.start_shield=0
	
	def move_mando(self,dx=0, dy=0):
		self.xco+=dx
		self.yco+=dy
		# self.in_map.map_array[0,8]=self.coins

	def move_left(self):
		if (self.yco>self.in_map.l_pointer):
			dx=0
			dy=-1
			if (self.in_map.obj_array[self.xco+dx,self.yco+dy]!=' '):
				if (self.in_map.obj_array[self.xco+dx,self.yco+dy]._desc=='coin'):
					self.in_map.obj_array[self.xco+dx,self.yco+dy].kill()
					self.__coins+=1
				elif(self.in_map.obj_array[self.xco+dx,self.yco+dy]._desc=='laser'):
					self.kill()
					return 1
				elif(self.in_map.obj_array[self.xco+dx,self.yco+dy]._desc=='speed'):
					self.speed=1
				elif(self.in_map.obj_array[self.xco+dx,self.yco+dy]._desc=='shield'):
					self.start_shield=time.time()
					self._shield='on'
			if (self.in_map.obj_array[self.xco+1+dx,self.yco+dy]!=' '):
				if (self.in_map.obj_array[self.xco+1+dx,self.yco+dy]._desc=='coin'):
					self.in_map.obj_array[self.xco+1+dx,self.yco+dy].kill()
					self.__coins+=1
				elif(self.in_map.obj_array[self.xco+1+dx,self.yco+dy]._desc=='laser'):
					self.kill()
					return 1
				elif(self.in_map.obj_array[self.xco+1+dx,self.yco+dy]._desc=='speed'):
					self.speed=1
				elif(self.in_map.obj_array[self.xco+1+dx,self.yco+dy]._desc=='shield'):
					self.start_shield=time.time()
					self._shield='on'
			self.move_mando(dx,dy)

	def move_right(self):
		if (self.yco< (self.in_map.l_pointer + self.right)):
			dx=0
			dy=1
			if (self.in_map.obj_array[self.xco+dx,self.yco+dy+1]!=' '):
				if (self.in_map.obj_array[self.xco+dx,self.yco+dy+1]._desc=='coin'):
					self.in_map.obj_array[self.xco+dx,self.yco+dy+1].kill()
					self.__coins+=1
				elif (self.in_map.obj_array[self.xco+dx,self.yco+dy+1]._desc=='laser'):
					self.kill()
					return 1
				elif (self.in_map.obj_array[self.xco+dx,self.yco+dy+1]._desc=='boss'):
					self.kill()
					return 1
				elif (self.in_map.obj_array[self.xco+dx,self.yco+dy+1]._desc=='speed'):
					self.speed=1
				elif (self.in_map.obj_array[self.xco+dx,self.yco+dy+1]._desc=='shield'):
					self.start_shield=time.time()
					self._shield='on'
			if (self.in_map.obj_array[self.xco+1+dx,self.yco+dy+1]!=' '):
				if (self.in_map.obj_array[self.xco+1+dx,self.yco+dy+1]._desc=='coin'):
					self.in_map.obj_array[self.xco+1+dx,self.yco+dy+1].kill()
					self.__coins+=1
				elif (self.in_map.obj_array[self.xco+1+dx,self.yco+dy+1]._desc=='laser'):
					self.kill()
					return 1
				elif (self.in_map.obj_array[self.xco+1+dx,self.yco+dy+1]._desc=='boss'):
					self.kill()
					return 1
				elif (self.in_map.obj_array[self.xco+1+dx,self.yco+dy+1]._desc=='speed'):
					self.speed=1
				elif (self.in_map.obj_array[self.xco+1+dx,self.yco+dy+1]._desc=='shield'):
					self.start_shield=time.time()
					self._shield='on'
			self.move_mando(dx,dy)


	def move_up(self):
		if (self.xco>3):
			dx=-1
			dy=0
			if (self.in_map.obj_array[self.xco+dx,self.yco+dy]!=' '):
				if (self.in_map.obj_array[self.xco+dx,self.yco+dy]._desc=='coin'):
					self.in_map.obj_array[self.xco+dx,self.yco+dy].kill()
					self.__coins+=1
				elif (self.in_map.obj_array[self.xco+dx,self.yco+dy]._desc=='laser'):
					self.kill()
					return 1
				elif (self.in_map.obj_array[self.xco+dx,self.yco+dy]._desc=='boss'):
					self.kill()
					return 1
			if (self.in_map.obj_array[self.xco+dx,self.yco+dy+1]!=' '):
				if (self.in_map.obj_array[self.xco+dx,self.yco+dy+1]._desc=='coin'):
					self.in_map.obj_array[self.xco+dx,self.yco+dy+1].kill()
					self.__coins+=1
				elif (self.in_map.obj_array[self.xco+dx,self.yco+dy+1]._desc=='laser'):
					self.kill()
					return 1
				elif (self.in_map.obj_array[self.xco+dx,self.yco+dy+1]._desc=='boss'):
					self.kill()
					return 1
			self.move_mando(dx,dy)


	def update(self):
		# print(self.xco,self.ground)
		if (self.xco < self.ground):
			dx=1
			dy=0
			if (self.in_map.obj_array[self.xco+dx+1,self.yco+dy]!=' '):
				if (self.in_map.obj_array[self.xco+dx+1,self.yco+dy]._desc=='coin'):
					self.in_map.obj_array[self.xco+dx+1,self.yco+dy].kill()
					self.__coins+=1
				elif (self.in_map.obj_array[self.xco+dx+1,self.yco+dy]._desc=='laser'):
					self.kill()
					return 1
				elif (self.in_map.obj_array[self.xco+dx+1,self.yco+dy]._desc=='bose'):
					self.kill()
					return 1
			if (self.in_map.obj_array[self.xco+dx+1,self.yco+dy+1]!=' '):
				if (self.in_map.obj_array[self.xco+dx+1,self.yco+dy+1]._desc=='coin'):
					self.in_map.obj_array[self.xco+dx+1,self.yco+dy+1].kill()
					self.__coins+=1
					self.move_mando(dx,dy)
				elif (self.in_map.obj_array[self.xco+dx+1,self.yco+dy+1]._desc=='laser'):
					self.kill()
					return 1
				elif (self.in_map.obj_array[self.xco+dx+1,self.yco+dy+1]._desc=='boss'):
					self.kill()
					return 1
			self.move_mando(dx,dy)


	def kill(self):
		if (self._shield=='of'):
			self.__lives-=1
			self.in_map.map_array[self.xco:self.xco+2:1,self.yco:self.yco+2:1]=' '
			self.in_map.obj_array[self.xco:self.xco+2:1,self.yco:self.yco+2:1]=' '
		sleep(1.25)
		self.xco=self.in_map.rows-4

	def get_lives(self):
		return self.__lives

	def get_coins(self):
		return self.__coins


