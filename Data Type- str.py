s = "hello world"
print(s.upper())

s = "HELLO"
print(s.lower())

s = "happy world"
print(s.title())

s = "sad world"
print(s.capitalize())

s = "Deary World"
print(s.swapcase())

s = "       apple  "
print(s.strip())

s = "      banana"
print(s.lstrip())

s = "Grapes   "
print(s.rstrip())

s = "hello world"
print(s.replace("hello", "happy"))

s = "apple,banana,mango"
print(s.split(","))

s = "apple,banana,mango"
print(s.rsplit(","))

s = "hello\nhappy\nworld"
print(s.splitlines())

words = ["hello", "world"]
print(" ".join(words))

s = "hello world"
print(s.find("world"))

s = "hello world world"
print(s.rfind("world"))

s = "hello world"
print(s.index("world"))

s = "hello world world"
print(s.rindex("world"))

s = "banana"
print(s.count("a"))

s = "hello world"
print(s.startswith("hello"))

s = "hello world"
print(s.endswith("world"))

s = "Hello"
print(s.isalpha())

s = "12345"
print(s.isdigit())

s = "Hello123"
print(s.isalnum())

s = "   "
print(s.isspace())

s = "HELLO"
print(s.isupper())

s = "hello"
print(s.islower())

s = "Hello World"
print(s.istitle())

s = "12345"
print(s.isnumeric())

s = "12345"
print(s.isdecimal())

s = "variable_name"
print(s.isidentifier())

s = "Hello World"
print(s.isprintable())

s = "hello"
print(s.center(20, "-"))

s = "hello"
print(s.ljust(20, "-"))

s = "hello"
print(s.rjust(20, "-"))

s = "42"
print(s.zfill(5))

s = "hello"
print(s.encode("utf-8"))

s = "hello\tworld"
print(s.expandtabs(4))

template = "Hello, {name}"
print(template.format_map({"name": "Alice"}))

table = str.maketrans("aeiou", "12345")
print(table)

s = "hello world"
table = str.maketrans("aeiou", "12345")
print(s.translate(table))

s = "hello-world-python"
print(s.partition("-"))

s = "hello-world-python"
print(s.rpartition("-"))

s = "unhappy"
print(s.removeprefix("un"))

s = "filename.txt"
print(s.removesuffix(".txt"))