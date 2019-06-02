from checksum import hextat_complement
from checksum import internet_checksum

v = hextat_complement(300)
#print(v)

result = internet_checksum(bytes.fromhex('B9 C9 D9'))
print(hex(int(result, 2)))
print(int(result, 2))
