#!/usr/bin/python3
# -*- coding: utf-8 -*-
# auther = Syst1m

import random
import time 

def poc(str):
	time.sleep(3)
	if random.randint(1,10)>5:
		return True
	return False