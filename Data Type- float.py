x = 10.0
print(x.is_integer())

y = 10.5
print(y.is_integer())

x = 10.5
print(x.as_integer_ratio())

x = 10.5
print(x.hex())

x = float.fromhex('0x1.5000000000000p+3')
print(x)

x = 10.5678
print(round(x))
print(round(x, 2))

x = -10.5
print(abs(x))

import math

x = 10.2
print(math.ceil(x))

import math

x = 10.9
print(math.floor(x))

import math

x = 10.9
print(math.trunc(x))