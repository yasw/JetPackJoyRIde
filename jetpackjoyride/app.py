#!/usr/bin/env python3
import sys
import os
import numpy as np
# from read import getch
from color import color_text
from Mando import Mando
from Screen import Screen
from Map import Map
import tty
import termios
import select
from time import sleep
import time
# from Boss import Boss
import random
from Powerup import Boss,Bullet,Magnet

def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

f=0
n=0
start=time.time()
start_b=time.time()
start_v=time.time()
start_p=time.time()
start_q=time.time()
screen = Screen()
level1_map=Map(screen.rows,screen.columns)
mando = Mando(level1_map.rows-4,8,screen.columns,level1_map)
boss=Boss(level1_map.rows-18,1480,level1_map)
screen.jetpack[:,:]=level1_map.map_array[0:screen.rows:1,0:level1_map.l_pointer + screen.columns:1]
magnet=Magnet(2,300,level1_map)
level1_map.map_array[magnet.xco,magnet.yco]=magnet.magnet_d
level1_map.map_array[mando.xco:mando.xco+2:1,mando.yco:mando.yco+2:1]=mando.man
level1_map.map_array[boss.xco:boss.xco+boss.boss.shape[0]:1,boss.yco:boss.yco+boss.boss.shape[1]:1]=boss.boss
level1_map.obj_array[boss.xco:boss.xco+boss.boss.shape[0]:1,boss.yco:boss.yco+boss.boss.shape[1]:1]=boss
level1_map.map_print()
v=0
k=0.01
l=0
c=0
mini_time = k/2
cnt = 0
cnt_x=0

MUSIC_FILES_PATH = "music/"
filename =  "song2"

os.system('aplay -q --process-id-file aplay_pid.txt ' + MUSIC_FILES_PATH + filename + '.wav & > /dev/null 2>/dev/null')
# sleep(1)
# music_pid_f = open("aplay_pid.txt", "r")
# print(music_pid)
# music_pid_f.close()
# exit(1)
while(1):
	sleep(mini_time)
	cnt += 1

	for h in range(len(level1_map.bullets)):
		if (level1_map.bullets[h].yco - level1_map.bullets[h].start >= 80 or level1_map.bullets[h].yco>1500):
			level1_map.bullets[h].kill()
		if (level1_map.bullets[h]._killed!=1):
			y=0
			level1_map.map_array[level1_map.bullets[h].xco,level1_map.bullets[h].yco]=' '
			level1_map.obj_array[level1_map.bullets[h].xco,level1_map.bullets[h].yco]=' '
			if (level1_map.map_array[level1_map.bullets[h].xco,level1_map.bullets[h].yco+1]!=' '):
				if (level1_map.obj_array[level1_map.bullets[h].xco,level1_map.bullets[h].yco+1]._desc=='laser'):
					level1_map.obj_array[level1_map.bullets[h].xco,level1_map.bullets[h].yco+1].kill(level1_map)
				elif (level1_map.obj_array[level1_map.bullets[h].xco,level1_map.bullets[h].yco+1]._desc=='coin'):
					level1_map.bullets[h].kill()
					y=1
				elif (level1_map.obj_array[level1_map.bullets[h].xco,level1_map.bullets[h].yco+1]._desc=='boss'):
					level1_map.obj_array[level1_map.bullets[h].xco,level1_map.bullets[h].yco+1].kill()
					level1_map.bullets[h].kill()
					y=1

			if (y==0):
				level1_map.bullets[h].yco+=1
				level1_map.map_array[level1_map.bullets[h].xco,level1_map.bullets[h].yco]=level1_map.bullets[h].bullet_d
				level1_map.obj_array[level1_map.bullets[h].xco,level1_map.bullets[h].yco]=level1_map.bullets[h]

	for h in range(len(level1_map.bulletsb)):
		if (level1_map.bulletsb[h].start- level1_map.bulletsb[h].yco >= 120):
			level1_map.bulletsb[h].kill()
		if (level1_map.bulletsb[h]._killed!=1):
			level1_map.map_array[level1_map.bulletsb[h].xco,level1_map.bulletsb[h].yco]=' '
			level1_map.obj_array[level1_map.bulletsb[h].xco,level1_map.bulletsb[h].yco]=' '
			level1_map.bulletsb[h].yco-=1
			if (level1_map.bulletsb[h].xco<mando.xco and level1_map.bulletsb[h]._curve==1):
				level1_map.bulletsb[h].xco=level1_map.bulletsb[h].xco+1
				temp=random.randrange(-2,3,1)
				if (level1_map.bulletsb[h].xco+temp>3 and level1_map.bulletsb[h].xco+temp<level1_map.rows-3):
					level1_map.bulletsb[h].xco+=temp
			elif (level1_map.bulletsb[h].xco>mando.xco and level1_map.bulletsb[h]._curve==1):
				level1_map.bulletsb[h].xco-=1
				temp=random.randrange(-2,3,1)
				if (level1_map.bulletsb[h].xco+temp>3 and level1_map.bulletsb[h].xco+temp<level1_map.rows-3):
					level1_map.bulletsb[h].xco+=temp
			if (level1_map.map_array[level1_map.bulletsb[h].xco,level1_map.bulletsb[h].yco]!=' '):
				if (level1_map.obj_array[level1_map.bulletsb[h].xco,level1_map.bulletsb[h].yco]._desc=='mando'):
					mando.kill()
			level1_map.map_array[level1_map.bulletsb[h].xco,level1_map.bulletsb[h].yco]=level1_map.bulletsb[h].bullet_c
			level1_map.obj_array[level1_map.bulletsb[h].xco,level1_map.bulletsb[h].yco]=level1_map.bulletsb[h]
			cnt_x+=1
	
	if (cnt % 2):
		continue
	# continue
	m_lives=mando.get_lives()
	if (m_lives<=0):
		level1_map.map_print()
		print("\t❤️ : "+ str(m_lives) +"  \t\t\t\t\t 💰 : "+ str(m_coins)+"\tshield : "+mando._shield + "\tBoss health : "+str(b_lives),end='' )
		print("\tYou lost man",end='')
		print()
		os.system('killall aplay > /dev/null 2> /dev/null')
		screen.s_b_exit()
		# print("Game over man, Keep Playing")
		sys.exit()
	b_lives=boss.get_lives()
	if (b_lives<=0):
		level1_map.map_print()
		print("\tMando lives : "+ str(m_lives) +"  \t\t\t\t\t Mando coins : "+ str(m_coins)+"\tshield : "+mando._shield + "\tBoss health : 000%",end='' )
		print("\tYou won man",end='')
		print()
		os.system('killall aplay > /dev/null 2> /dev/null')

		screen.s_b_exit()
		sys.exit()
	level1_map.map_array[mando.xco:mando.xco+2:1,mando.yco:mando.yco+2:1]=' '
	level1_map.obj_array[mando.xco:mando.xco+2:1,mando.yco:mando.yco+2:1]=' '	
	if (level1_map.l_pointer>1520-level1_map.screen_columns):
		level1_map.map_array[boss.xco:boss.xco+boss.boss.shape[0]:1,boss.yco:boss.yco+boss.boss.shape[1]:1]=' '
		level1_map.obj_array[boss.xco:boss.xco+boss.boss.shape[0]:1,boss.yco:boss.yco+boss.boss.shape[1]:1]=' '
	if (level1_map.l_pointer+level1_map.screen_columns<1523):
		level1_map.l_pointer+=1
		mando.move_right()
	if (((magnet.yco>mando.yco) and (magnet.yco-mando.yco<10)) or ((mando.yco>magnet.yco) and (mando.yco-magnet.yco<10))):
		if (magnet.yco>mando.yco):
			mando.move_right()
		if (magnet.yco<mando.yco):
			mando.move_left()
		mando.move_up()
	if isData():
		move=sys.stdin.read(1)
		if (move == 'A' or move == 'a'):
			mando.move_left()
		elif (move == 'D' or move == 'd'):
			mando.move_right()
		elif (move == 'W' or move == 'w'):
			# mando.move_up()
			v=100
		elif (move == 'S' or move == 's'):
			level1_map.bullets.append(Bullet(mando.xco,mando.yco+10,level1_map))
			level1_map.map_array[level1_map.bullets[l].xco,level1_map.bullets[l].yco]=level1_map.bullets[l].bullet_d
			level1_map.obj_array[level1_map.bullets[l].xco,level1_map.bullets[l].yco]=level1_map.bullets[l]
			l+=1
		elif (move == 'Q' or move == 'q'):
			screen.s_b_exit()
			print()
			os.system('killall aplay > /dev/null 2> /dev/null')

			sys.exit()
	
	if (mando.speed==1 and k==0.01):
		k=0.00001
		mini_time = 0.000005
		start=time.time()
	if (mando.speed==1 and time.time()-start>=7.0):
		mando.speed=0
		k=0.02
		mini_time = k/2
	if (((magnet.yco>mando.yco) and (magnet.yco-mando.yco<5)) or ((mando.yco>magnet.yco) and (mando.yco-magnet.yco<5))):
		mando.move_up()
	if (v>0):
		v-=10
		mando.move_up()
	if (v<=0):
		# v=0
		mando.update()

	if (mando.yco == (level1_map.l_pointer+screen.columns-2)):
		mando.yco-=1
	if (level1_map.l_pointer>1520-level1_map.screen_columns):
		if (boss.xco+12<mando.xco and time.time()-start_b>=0.2):
			start_b=time.time()
			boss.xco+=1
		elif (boss.xco>mando.xco and time.time()-start_b>=0.2):
			start_b=time.time()
			boss.xco-=1
		level1_map.map_array[boss.xco:boss.xco+boss.boss.shape[0]:1,boss.yco:boss.yco+boss.boss.shape[1]:1]=boss.boss
		level1_map.obj_array[boss.xco:boss.xco+boss.boss.shape[0]:1,boss.yco:boss.yco+boss.boss.shape[1]:1]=boss
		if (time.time()-start_v>=0.8):
			level1_map.bulletsb.append(Bullet(boss.xco+6,boss.yco-3,level1_map))
			if (c%5==0):
				level1_map.bulletsb[c]._curve=1
			level1_map.map_array[level1_map.bulletsb[c].xco,level1_map.bulletsb[c].yco]=level1_map.bulletsb[c].bullet_c
			level1_map.obj_array[level1_map.bulletsb[c].xco,level1_map.bulletsb[c].yco]=level1_map.bulletsb[c]
			c+=1
			start_v=time.time()
	if (mando._shield=='of'):
		level1_map.map_array[mando.xco:mando.xco+2:1,mando.yco:mando.yco+2:1]=mando.man
		level1_map.obj_array[mando.xco:mando.xco+2:1,mando.yco:mando.yco+2:1]=mando
	else:
		level1_map.map_array[mando.xco:mando.xco+2:1,mando.yco:mando.yco+2:1]=mando.man_s
		level1_map.obj_array[mando.xco:mando.xco+2:1,mando.yco:mando.yco+2:1]=mando
	if (mando._shield=='on'):
		if ((time.time()-mando.start_shield)>=5.0):
			mando._shield='of'

	if (f>-10 and time.time()-start_p>=0.1):
		level1_map.map_array[level1_map.enemies[1].xco:level1_map.enemies[1].xco+2:1,level1_map.enemies[1].yco:level1_map.enemies[1].yco+11:1]=' '
		level1_map.obj_array[level1_map.enemies[1].xco:level1_map.enemies[1].xco+2:1,level1_map.enemies[1].yco:level1_map.enemies[1].yco+11:1]=' '
		level1_map.enemies[1].xco-=1
		level1_map.map_array[level1_map.enemies[1].xco:level1_map.enemies[1].xco+2:1,level1_map.enemies[1].yco:level1_map.enemies[1].yco+11:1]=level1_map.enemies[1].light_beam_h
		level1_map.obj_array[level1_map.enemies[1].xco:level1_map.enemies[1].xco+2:1,level1_map.enemies[1].yco:level1_map.enemies[1].yco+11:1]=level1_map.enemies[1]
		f-=1
		start_p=time.time()
	if (f==-10):
		f=0
		level1_map.map_array[level1_map.enemies[1].xco:level1_map.enemies[1].xco+2:1,level1_map.enemies[1].yco:level1_map.enemies[1].yco+11:1]=' '
		level1_map.obj_array[level1_map.enemies[1].xco:level1_map.enemies[1].xco+2:1,level1_map.enemies[1].yco:level1_map.enemies[1].yco+11:1]=' '
		level1_map.enemies[1].xco+=10
	if (n>-10 and time.time()-start_q>=0.1):
		level1_map.map_array[level1_map.enemies[7].xco:level1_map.enemies[7].xco+2:1,level1_map.enemies[7].yco:level1_map.enemies[7].yco+11:1]=' '
		level1_map.obj_array[level1_map.enemies[7].xco:level1_map.enemies[7].xco+2:1,level1_map.enemies[7].yco:level1_map.enemies[7].yco+11:1]=' '
		level1_map.enemies[7].xco-=1
		level1_map.map_array[level1_map.enemies[7].xco:level1_map.enemies[7].xco+2:1,level1_map.enemies[7].yco:level1_map.enemies[7].yco+11:1]=level1_map.enemies[7].light_beam_h
		level1_map.obj_array[level1_map.enemies[7].xco:level1_map.enemies[7].xco+2:1,level1_map.enemies[7].yco:level1_map.enemies[7].yco+11:1]=level1_map.enemies[7]
		n-=1
		start_q=time.time()
	if (n==-10):
		n=0
		level1_map.map_array[level1_map.enemies[7].xco:level1_map.enemies[7].xco+2:1,level1_map.enemies[7].yco:level1_map.enemies[7].yco+11:1]=' '
		level1_map.obj_array[level1_map.enemies[7].xco:level1_map.enemies[7].xco+2:1,level1_map.enemies[7].yco:level1_map.enemies[7].yco+11:1]=' '
		level1_map.enemies[7].xco+=10

	level1_map.map_print()
	m_lives=mando.get_lives()
	b_lives=boss.get_lives()
	m_coins=mando.get_coins()
	if (b_lives==1):
		asd='025%'
	elif (b_lives==2):
		asd='050%'
	elif (b_lives==3):
		asd='075%'
	elif (b_lives==4):
		asd='100%'
	print("\t" + color_text("❤️", "Red") + " :"+ str(m_lives) +"  \t\t\t\t\t" + color_text("$", "Green") +  " :"+ str(m_coins)+"\t"+color_text("🛡️", "Yellow")+" : "+mando._shield + "\t"+ color_text("😈", "Red") +" : "+asd,end='' )