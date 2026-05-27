tup = (10, 20, 30, 40, 20)

print("Membership:", 20 in tup)
print("Membership:", 80 in tup)
print("Not Membership:", 50 not in tup)
print("Not Membership:", 10 not in tup)

tup1 = (1, 2)
tup2 = (3, 4)
print("Concatenation:", tup1 + tup2)

print("Repetition:", tup1 * 3)

print("Indexing:", tup[2])

print("Slicing:", tup[1:4])

print("Length:", len(tup))

print("Minimum:", min(tup))

print("Maximum:", max(tup))

print("Sum:", sum(tup))

print("Count:", tup.count(20))

print("Index:", tup.index(20, 1, 5))