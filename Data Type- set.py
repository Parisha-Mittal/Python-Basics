s = {1, 2, 3}

s.add(4)
print("Add:", s)

s.update([5, 6])
print("Update Iterable:", s)

s.remove(2)
print("Remove:", s)

s.discard(4)
print("Discard:", s)

print("Pop:", s.pop())
print("After Pop:", s)

s2 = s.copy()
print("Copy:", s2)

a = {1, 2}
b = {2, 3}

print("Union:", a.union(b))

print("Intersection:", a.intersection(b))

print("Difference:", a.difference(b))

print("Symmetric Difference:", a.symmetric_difference(b))

a.update({4, 5})
print("Update Other:", a)

c = {1, 2, 3}
c.intersection_update({2, 3, 4})
print("Intersection Update:", c)

d = {1, 2, 3}
d.difference_update({2})
print("Difference Update:", d)

e = {1, 2, 3}
e.symmetric_difference_update({3, 4})
print("Symmetric Difference Update:", e)

print("Is Subset:", {1, 2}.issubset({1, 2, 3}))

print("Is Superset:", {1, 2, 3}.issuperset({1, 2}))

print("Is Disjoint:", {1, 2}.isdisjoint({3, 4}))