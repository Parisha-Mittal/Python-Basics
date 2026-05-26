n = 10
print(n.bit_length())

n = 10
print("Bit count:",n.bit_count())

n = 1024
b = n.to_bytes(2, byteorder='big')
print(b)

b = b'\x04\x00'
n = int.from_bytes(b, byteorder='big')
print(n)

n = 10
print(n.as_integer_ratio())

print(abs(-15))

print(pow(2, 3))

print(divmod(17, 5))

print(bin(10))

print(oct(10))

print(hex(10))