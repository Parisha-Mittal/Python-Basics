d = {"name": "Parisha", "age": 21}

print("Keys:", d.keys())

print("Values:", d.values())

print("Items:", d.items())

print("Get:", d.get("name", "Unknown"))

print("Set Default:", d.setdefault("city", "Ahmedabad"))

d.update({"country": "India"})
print("Update:", d)

print("Pop:", d.pop("age"))
print("After Pop:", d)

print("Popitem:", d.popitem())
print("After Popitem:", d)

d2 = d.copy()
print("Copy:", d2)

print("Fromkeys:", dict.fromkeys(["a", "b"], 0))

print("Length:", len(d))

print("Sorted:", sorted(d))

keys = ["x", "y", "z"]
values = [1, 2, 3]
print("Zip Dict:", dict(zip(keys, values)))

print("Any:", any(d))

print("All:", all(d))