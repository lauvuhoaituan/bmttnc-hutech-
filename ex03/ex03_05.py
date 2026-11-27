numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

result = {}

for n in numbers:
    if n in result:
        result[n] += 1
    else:
        result[n] = 1

print("Dictionary:", result)