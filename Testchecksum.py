from checksum import hextat_complement
from checksum import internet_checksum

v = hextat_complement(300)
#print(v)

result = internet_checksum(bytes([0, 1, 242, 3, 244, 245, 246, 247]))
print(hex(int(result, 2)))
