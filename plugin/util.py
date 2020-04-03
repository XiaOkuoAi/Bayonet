#!/usr/bin/python3
# -*- coding: utf-8 -*-
# auther = Syst1m

import random
import hashlib
import requests
import socket
import re
from string import ascii_lowercase,digits

"""
ascii_letters方法的作用是生成全部字母，包括a-z,A-Z
digits方法的作用是生成数组，包括0-9
"""
#from urlparse import urlparse
from urllib import parse

def randomString(length=8):
	"""
	生成随机字母串

	:param length:生成字符串长度
	:return 字母串

	join 将指定字符串用特定字符连接起来
	随机八位小写字母
	"""

	return ''.join([random.choice(ascii_lowercase) for _ in range(length)])

def randomDigits(length=8):
	"""
	随机数字串
	"""
	return ''.join([random.choice(digits) for _ in range(length)])

def randomMD5(length=10, hex=True):
    """
    生成随机MD5键值对

    :param length:指定明文长度
    :param hex:指定密文长度为32位
    :returns 原文，密文(32位或16位)
    """
    plain = randomDigits(length)
    m = hashlib.md5()
    m.update(plain)
    cipher = m.hexdigest() if hex else m.hexdigest()[8:-8]
    return [plain, cipher]


def redirectURL(url,timeout=3):

	"""
	获取跳转后的真实url

	:param url:原始url
	:param timeout:超时时间
	:return 跳转后的真实url
	"""
	try:
		url = url if '://' in url else 'http://' + url
		r= requests.get(url,allow_redirects=False, timeout=timeout)
		return r.headers.get('localtion') if r.status_code == 302 else url
	except Exception:
		return url


def host2IP(url):

	"""
	URL转IP

	:param url:原始url
	:return IP：post
	:expect 返回原始url
	"""

	for offset in url:
		if offset.isalpha(): #isalpha()检测字符串中是否只包含字母
			break
	else:
		return url
	try:
		url = url if '://' in url else 'http://' + url
		url = paese.urlparse(url).netloc # 域名
		ans = [i for i in socket.getaddrinfo(url.split(':')[0], None)[0][4] if i != 0][0]
		print(ans)
		if ':' in url:
			ans += ':' + url.split(':')[1]
		return ans
	except Exception:
		return url

def IP2domain(base, timeout=3):

    """
    IP转域名
    :param base:原始IP
    :param timeout:超时时间
    :return 域名 / False
    :except 返回False
    """
    try:
        domains = set()
        ip = base.split(':')[0] if ':' in base else base
        q = "https://www.bing.com/search?q=ip%3A" + ip
        c = requests.get(url=q,
                         headers={
                             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'},
                         timeout=timeout
                         ).content
        p = re.compile(r'<cite>(.*?)</cite>') # 生成正则，避免重复生成使用
        l = re.findall(p, c)
        for each in l:
            domain = each.split('://')[-1].split('/')[0]
            domains.add(domain)
        if len(domains) > 0:
            ans_1 = base + ' -> '
            for each in domains:
                ans_1 += '|' + each
            return ans_1
        else:
            return False
    except Exception:
        return False


def checkPortTcp(target,port,timeout=3):

	"""
	return True / False
	except 返回False
	"""
	sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sk.settimeout(timeout)
	try:
		sk.connect((target,port))
		return True
	except Exception:
		return False
