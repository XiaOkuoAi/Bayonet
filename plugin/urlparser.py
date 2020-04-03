#!/usr/bin/python3
# -*- coding: utf-8 -*-
# auther = Syst1m

from urllib import parse

def get_domain(url):

    """
    added by cdxy May 8 Sun,2016

    Use:
    get_domain('http://cdxy.me:80/cdsa/cda/aaa.jsp?id=2#')

    Return:
    'http://cdxy.me:80'
    """
    p = parse.urlparse(url)
    return parse.urlunsplit([p.scheme, p.netloc, '', '', ''])

def iterate_path(ori_str):
    """

    Use:
    iterate_path_to_list('http://xxx.com:80/cdsa/cda/aaa.jsp?id=2#')

    Return:
    ['http://xxx.com:80/cdsa/cda/aaa.jsp?id=2#',
     'http://xxx.com:80/'
     'http://xxx.com:80/cdsa',
     'http://xxx.com:80/cdsa/cda',
     'http://xxx.com:80/cdsa/cda/aaa.jsp']

    """
    parser = parse.urlparse(ori_str)
    _path_list = parser.path.replace('//', '/').strip('/').split('/')
    _ans_list = set()
    _ans_list.add(ori_str)

    if not _path_list[0]:
        return _ans_list

    _ans_list.add(get_domain(ori_str))
    s = ''
    for each in _path_list:
        s += '/' + each
        _ans_list.add(parse.urljoin(ori_str, s))
    return _ans_list



if __name__ =='__main__':
    

    url = "http://xxx.com:80/cdsa/cda/aaa.jsp?id=2#"

    iterate_path(url)

  #   print(parse.urlparse(url))
  #   print(get_domain(url))

  #   for each in iterate_path(url):
		# print(each)



