
lst = [1, 2, 3, 5, 32, 56]

# Insert two numbers at 3rd position
lst.insert(2, 12)
lst.insert(3, 45)

# Append one name
lst.append('neha')

print("Original list:", lst)

# Convert list into string
s = str(lst)
print("Type:", type(s))

# Split the list into two parts at 45
pos = lst.index(45)

first = lst[:pos]
second = lst[pos:]

print("First part:", first)
print("Second part:", second)