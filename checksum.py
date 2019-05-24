# -*- coding: utf-8 -*-

def internet_checksum(data, total=0x0):
    '''
    Internet Checksum of a bytes array.
    Further reading:
    1. https://tools.ietf.org/html/rfc1071
    2. http://www.netfor2.com/checksum.html
    '''
	# TODO: Implement this function and return the checksum

    #Slicing bytes to iterate over it
    L = [data[i:i+1] for i in range(len(data))]
    sum = 0;

    #Getting sum
    for evens in L[::2]:
        sum+= int.from_bytes(evens, byteorder='big') * 256

    for odds in L[1::2]:
        sum+= int.from_bytes(odds, byteorder='big')


    hexsum = hex(sum)
    hexsum = hexsum[2:]

    carry, value = split_carry(hexsum)

    while carry is not '':
        hexsum = int(value, 16) + int(carry, 16)
        carry, value = split_carry(hex(hexsum)[2:])

    print(hex(hexsum))
    return hextat_complement(hexsum)

def hextat_complement(x):
    mask = 0xffff
    return bin(~x & mask)[2:]



def split_carry(sum):
    carry = sum[:-4]
    value = sum[-4:]
    return carry, value