#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author = syst1m


import os 
import re

from subprocess import PIPE
from subprocess import Popen as execute

def getRevisionNumber():
	"""
	Returns abbreviated commit hash number as retrieved with "git rev-parse --short HEAD"
	"""

	retval = None
	filePath = None
	_ = os.path.dirname(__file__)

	while  True:
		filePath = os.path.join(_,".git","HEAD")
		if os.path.exists(filePath):
			break
		else:
			filePath = None
			if _ == os.path.dirname(_):
				break
			else:
				_ = os.path.dirname(_)
	while True:
		if filePath and os.path.isfile(filePath):
			with open(filePath,"r") as f:
				content = f.read()
				filePath = None
				if content.startwith("ref: "):
					filePath = os.path.join(_,".git",content.replace("ref: ","").strip())
				else:
					match = re.match(r"(?i)[0-9a-f]{32}", content)
					retval = match.group(0) if match else None
		else:
			break

	if not retval:
		process = execute("git rev-parse --verify HEAD", shell=True, stdout=PIPE, stderr=PIPE)
		stdout, _ = process.communicate()
		match = re.search(r"(?i)[0-9a-f]{32}", stdout or "")
		retVal = match.group(0) if match else None

	return retval[:7] if retVal else None