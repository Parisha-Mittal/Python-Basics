lst = [10, 20, 30, 40, 50]

print("Append:", lst)

lst.extend([60, 70])
print("Extend:", lst)

lst.insert(1, 15)
print("Insert:", lst)

lst.remove(30)
print("Remove:", lst)

print("Pop:", lst.pop(-1))
print("After Pop:", lst)

print("Index:", lst.index(20, 1, 4))

print("Count:", lst.count(20))

lst.sort(reverse=False)
print("Sort:", lst)

lst.reverse()
print("Reverse:", lst)

new_lst = lst.copy()
print("Copy:", new_lst)

print("Membership:", 20 in lst)
print("Not Membership:", 50 not in lst)

lst1 = [1, 2]
lst2 = [3, 4]
print("Concatenation:", lst1 + lst2)

print("Repetition:", lst1 * 3)

print("Indexing:", lst[2])

print("Slicing:", lst[1:3])

print("Length:", len(lst))

print("Minimum:", min(lst))
print("Maximum:", max(lst))

print("Sum:", sum(lst))

del lst[1]
print("Delete Index:", lst)

lst = [10, 20, 30, 40]
del lst[1:3]
print("Delete Slice:", lst)

lst = ["a", "b", "c"]
print("Enumerate:", list(enumerate(lst)))

lst1 = [1, 2, 3]
lst2 = ["a", "b", "c"]
print("Zip:", list(zip(lst1, lst2)))

lst = [10, 20, 30]
lst.clear()
print("Clear:", lst)