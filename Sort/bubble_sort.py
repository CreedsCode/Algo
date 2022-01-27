input = [43, 2, 47, 17, 4, 8, 15]

for i in range(len(input)):
    for j in range(len(input) - 1):
        if input[j] > input[j+1]:
            input[j], input[j+1] = input[j+1], input[j]

print(input)