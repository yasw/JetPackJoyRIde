#!/usr/bin/env python3
from utility import get_obj
import sys
import os
import config
import numpy as np
from color import color_text
from Enemy import Enemy
# from Coin import Coin
from time import sleep
from Powerup import Speed,Shield,Coin,Magnet
class Map:
	def __init__(self,rows_m,columns_m):
		self.rows=rows_m
		self.screen_columns=columns_m
		self.columns=1524
		self.map_array = np.empty([self.rows,self.columns], dtype='U25')
		self.map_array[:,:] = " " 
		self.obj_array = np.empty([self.rows,self.columns], dtype='object')
		self.obj_array[:,:] = " " 
		self.l_pointer=0
		self.enemies=[]
		self.coins=[]
		self.speed=[]
		self.shield=[]
		self.bullets=[]
		self.bulletsb=[]
		self.speed.append(Speed(self.rows-4,200,self))
		self.shield.append(Shield(self.rows-4,400,self))
		self.shield.append(Shield(self.rows-4,700,self))
		self.map_array[self.speed[0].xco,self.speed[0].yco]=self.speed[0].speed_d
		self.obj_array[self.speed[0].xco,self.speed[0].yco]=self.speed[0]
		self.map_array[self.shield[0].xco,self.shield[0].yco]=self.shield[0].shield_d
		self.obj_array[self.shield[0].xco,self.shield[0].yco]=self.shield[0]
		self.map_array[self.shield[1].xco,self.shield[1].yco]=self.shield[1].shield_d
		self.obj_array[self.shield[1].xco,self.shield[1].yco]=self.shield[1]
		self.i=0
		self.r=0
		for q in range(45,1350,70):
			for w in range(20):
				self.coins.append(Coin(self.rows-20,q+w,self))
				self.coins.append(Coin(self.rows-19,q+w,self))
				self.map_array[self.coins[self.r].xco,self.coins[self.r].yco]=self.coins[self.r].coin_d
				self.map_array[self.coins[self.r+1].xco,self.coins[self.r+1].yco]=self.coins[self.r+1].coin_d
				self.obj_array[self.coins[self.r].xco,self.coins[self.r].yco]=self.coins[self.r]
				self.obj_array[self.coins[self.r+1].xco,self.coins[self.r+1].yco]=self.coins[self.r+1]
				self.r+=2
		for q in range(55,1350,70):
			for w in range(20):
				self.coins.append(Coin(self.rows-47,q+w,self))
				self.coins.append(Coin(self.rows-46,q+w,self))
				self.map_array[self.coins[self.r].xco,self.coins[self.r].yco]=self.coins[self.r].coin_d
				self.map_array[self.coins[self.r+1].xco,self.coins[self.r+1].yco]=self.coins[self.r+1].coin_d
				self.obj_array[self.coins[self.r].xco,self.coins[self.r].yco]=self.coins[self.r]
				self.obj_array[self.coins[self.r+1].xco,self.coins[self.r+1].yco]=self.coins[self.r+1]
				self.r+=2

		for j in range(30,1330,70):
			if(self.i%3 == 0):
				self.enemies.append(Enemy(self.rows-15,j))
			elif(self.i%3 == 1):
				self.enemies.append(Enemy(self.rows-12,j))
			else:
				self.enemies.append(Enemy(self.rows-43,j))
			self.i+=1
		for i in range(len(self.enemies)):
			if (i%3== 0):
				self.map_array[self.enemies[i].xco:self.enemies[i].xco+11:1,self.enemies[i].yco:self.enemies[i].yco+2:1]=self.enemies[i].light_beam_v
				self.obj_array[self.enemies[i].xco:self.enemies[i].xco+11:1,self.enemies[i].yco:self.enemies[i].yco+2:1]=self.enemies[i]
				self.enemies[i]._v=0
			elif(i%3==1):
				self.map_array[self.enemies[i].xco:self.enemies[i].xco+2:1,self.enemies[i].yco:self.enemies[i].yco+11:1]=self.enemies[i].light_beam_h
				self.obj_array[self.enemies[i].xco:self.enemies[i].xco+2:1,self.enemies[i].yco:self.enemies[i].yco+11:1]=self.enemies[i]
				self.enemies[i]._v=1
			else:
				self.map_array[self.enemies[i].xco:self.enemies[i].xco+11:1,self.enemies[i].yco:self.enemies[i].yco+11:1]=self.enemies[i].light_beam_x
				b=10
				self.enemies[i]._v=2
				for c in range(0,11,1):
					self.obj_array[self.enemies[i].xco+c,self.enemies[i].yco+b]=self.enemies[i]
					b-=1
		for i in range(1, 3, 1):
			for j in range(self.columns):
				self.map_array[i][j] = color_text('^','Fg Black Bg Blue')
		for i in range(self.rows - 1, self.rows - 3, -1):
			for j in range(self.columns):
				self.map_array[i][j] = color_text('_','Fg Red Bg Green')
		for i in range(self.rows - 3, 2, -1):
			for j in range(1522,1523,1):
				self.map_array[i][j] = color_text('_','Fg Black Bg Red')
		# self.magnet=Magnet(2,100,self)
		# self.map_array[self.magnet.xco,self.magnet.yco]=self.magnet.magnet_d

	def map_print(self):
		print('\033[0;0f',end='')
		# os.system('tput reset')
		if (self.l_pointer+self.screen_columns<1524):
			for i in range(self.rows):
				for j in range(self.l_pointer,self.l_pointer+self.screen_columns,1):
					print(self.map_array[i][j], end='')
				print('\n\r',end='')

