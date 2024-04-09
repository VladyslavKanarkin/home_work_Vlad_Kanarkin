elements = [5, 2, 9, 12, 24, 35, -9]

mins = elements[0]
for i in elements:
    if i < mins:
        mins = i

print(mins)
