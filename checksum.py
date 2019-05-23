# -*- coding: utf-8 -*-

def internet_checksum(data, total=0x0):
    '''
    Internet Checksum of a bytes array.
    Further reading:
    1. https://tools.ietf.org/html/rfc1071
    2. http://www.netfor2.com/checksum.html
    '''
	# TODO: Implement this function and return the checksum

def hextat_complement(x):
    mask = 0xffff
    return bin(~x & mask)[2:]