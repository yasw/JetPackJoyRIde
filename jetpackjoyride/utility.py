import sys
import os
import numpy as np

def split(word): 
    return [char for char in word]

def get_obj(obj):
    string_obj=[]
    d=obj.splitlines()
    d.pop(0)
    length=len(d)
    for i in range(length):
        string_obj.append(split(d[i]))
    return string_obj 

def get_terminal_size(fallback=(80, 24)):
	for i in range(0, 3):
	    try:
	        columns, rows = os.get_terminal_size(i)
	    except OSError:
	        continue
	    break
	else:  # set default if the loop completes which means all failed
	    columns, rows = fallback
	return columns, rows
