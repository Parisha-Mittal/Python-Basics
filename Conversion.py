print("Integer:", int('21'))
print("Integer from Float:", int(8.2))
print("Integer from Bool:", int(False))

print("Float:", float('9.81'))
print("Float from Int:", float(100))

print("String from Int:", str(21))
print("String from Float:", str(9.8))
print("String from Bool:", str(False))

print("Boolean from Zero:", bool(0))
print("Boolean from Empty String:", bool(''))
print("Boolean from Empty List:", bool([]))

print("List from String:", list('happy'))
print("List from Tuple:", list((1, 2, 3, 4, 5)))

print("Tuple from List:", tuple([1, 2, 3, 3, 4, 5]))

print("Set from List:", {1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6})

print("Dictionary:", dict(a=1, b=2))

x = 1
z = bool(x)
print("Implicit Conversion:", z)

a = True
b = int(a)
print("Explicit Conversion:", b)