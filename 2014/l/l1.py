>>> s = "01001000 01100101 01101100 01101100 01101111 00100001 00100000 01000001 01110011 00100000 01111001 01101111 01110101 01110010 00100000 01100001 01101110 01110011 01110111 01100101 01110010 00101100 00100000 01110011 01110101 01100010 01101101 01101001 01110100 00100000 01110100 01101000 01100101 00100000 01101100 01100001 01110010 01100111 01100101 01110011 01110100 00100000 01110000 01110010 01101001 01101101 01100101 00100000 01100110 01100001 01100011 01110100 01101111 01110010 00100000 01101111 01100110 00100000 01110100 01101000 01100101 00100000 01100110 01101111 01101100 01101100 01101111 01110111 01101001 01101110 01100111 00100000 01101110 01110101 01101101 01100010 01100101 01110010 00111010  ? 01010111 01100101 00100000 01110111 01101001 01110011 01101000 00100000 01111001 01101111 01110101 00100000 01100111 01101111 01101111 01100100 00100000 01101100 01110101 01100011 01101011 00100001"
>>> s.split()
['01001000', '01100101', '01101100', '01101100', '01101111', '00100001', '00100000', '01000001', '01110011', '00100000', '01111001', '01101111', '01110101', '01110010', '00100000', '01100001', '01101110', '01110011', '01110111', '01100101', '01110010', '00101100', '00100000', '01110011', '01110101', '01100010', '01101101', '01101001', '01110100', '00100000', '01110100', '01101000', '01100101', '00100000', '01101100', '01100001', '01110010', '01100111', '01100101', '01110011', '01110100', '00100000', '01110000', '01110010', '01101001', '01101101', '01100101', '00100000', '01100110', '01100001', '01100011', '01110100', '01101111', '01110010', '00100000', '01101111', '01100110', '00100000', '01110100', '01101000', '01100101', '00100000', '01100110', '01101111', '01101100', '01101100', '01101111', '01110111', '01101001', '01101110', '01100111', '00100000', '01101110', '01110101', '01101101', '01100010', '01100101', '01110010', '00111010', '?', '01010111', '01100101', '00100000', '01110111', '01101001', '01110011', '01101000', '00100000', '01111001', '01101111', '01110101', '00100000', '01100111', '01101111', '01101111', '01100100', '00100000', '01101100', '01110101', '01100011', '01101011', '00100001']
>>> entries = s.split()
>>> [int(b, 2) for b in entries]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 2: '?'
>>> [int(b, 2) for b in entries if '?' not in b]
[72, 101, 108, 108, 111, 33, 32, 65, 115, 32, 121, 111, 117, 114, 32, 97, 110, 115, 119, 101, 114, 44, 32, 115, 117, 98, 109, 105, 116, 32, 116, 104, 101, 32, 108, 97, 114, 103, 101, 115, 116, 32, 112, 114, 105, 109, 101, 32, 102, 97, 99, 116, 111, 114, 32, 111, 102, 32, 116, 104, 101, 32, 102, 111, 108, 108, 111, 119, 105, 110, 103, 32, 110, 117, 109, 98, 101, 114, 58, 87, 101, 32, 119, 105, 115, 104, 32, 121, 111, 117, 32, 103, 111, 111, 100, 32, 108, 117, 99, 107, 33]
>>> [chr(int(b, 2)) for b in entries if '?' not in b]
