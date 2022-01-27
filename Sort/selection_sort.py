input = [15, 2, 43, 17, 4, 8, 47]

for i in range(len(input)):
    min = i
    for j in range(i + 1, len(input)):
        if input[min] > input[j]:
            min = j

    input[i], input[min] = input[min], input[i] 

print(input)