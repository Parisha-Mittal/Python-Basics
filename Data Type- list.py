lst = [10, 20, 30, 40]

print("Append:", lst)

lst.extend([50, 60])
print("Extend:", lst)

lst.insert(1, 15)
print("Insert:", lst)

lst.remove(30)
print("Remove:", lst)

print("Pop:", lst.pop(-1))
print("After Pop:", lst)

lst.clear()
print("Clear:", lst)

lst = [10, 20, 30, 20, 40]

print("Index:", lst.index(20, 1, 4))

print("Count:", lst.count(20))

lst.sort(reverse=False)
print("Sort:", lst)

lst.reverse()
print("Reverse:", lst)

new_lst = lst.copy()
print("Copy:", new_lst)