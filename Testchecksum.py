from checksum import hextat_complement
from checksum import internet_checksum

if __name__ == '__main__':
    data = bytes.fromhex('0001f203f4f5f6f7')
    checksum = internet_checksum(data)
    assert checksum == 0x0d22
    print('Test 1 passed')

    data = bytes.fromhex('e34f2396442799f3')
    checksum = internet_checksum(data)
    assert checksum == 0xff1a
    print('Test 2 passed')