
n = []
for i in range(0, 3):
    n.append((int(input())))
max = n[0]
for i in range(1, 3):
    if max < n[i]:
        max = n[i]
print (max)
