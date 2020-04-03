#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author = syst1m

import os
import subprocess

VERSION = '1.0.0'
PROJECT = "Bayonet"
AUTHOR = 'syst1m'
MAIL = '1990758989@qq.com'
PLATFORM = os.name
IS_WIN = subprocess._mswindows

# essential methods/functions in custom scripts/PoC (such as function poc())
ESSENTIAL_MODULE_METHODS = ['poc']

# Encoding used for Unicode data
UNICODE_ENCODING = "utf-8"

# String representation for NULL value
NULL = "NULL"

# Format used for representing invalid unicode characters
INVALID_UNICODE_CHAR_FORMAT = r"\x%02x"

ISSUES_PAGE = ""
GIT_REPOSITORY = ""
GIT_PAGE = ""

BANNER = """\033[01;34m
 __                           \033[01;31m__/\033[01;34m
 )_)  _       _   _   _  _)_ \033[01;33m/ \033[01;31m__/\033[01;34m
/__) (_( (_( (_) ) ) )_) (_  \033[01;33m_/\033[01;34m
           _)       (_       


        \033[01;37m{\033[01;m Version %s by %s mail:%s \033[01;37m}\033[0m            
\n"""% (VERSION, AUTHOR, MAIL)