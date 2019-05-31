from checksum import hextat_complement
from checksum import internet_checksum

v = hextat_complement(300)
#print(v)

result = internet_checksum(bytes.fromhex('E34F2396442799F3'))
print(hex(int(result, 2)))
