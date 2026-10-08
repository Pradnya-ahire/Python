lst = [1, 'neha', 'riya', 33, 21, 'yash', 12, 23, 1, 'hii']

num = []

for i in lst:
    if type(i) == int:
        num.append(i)

max_num = num[0]

for j in num:
    if j > max_num:
        max_num = j

print("Highest number:", max_num)

pos = lst.index(max_num)

first = lst[:pos]
second = lst[pos:]

print("First list:", first)
print("Second list:", second)