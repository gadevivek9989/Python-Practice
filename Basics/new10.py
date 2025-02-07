import math
#nested loops
#1 2 3
#4 5 6
#7 8 9

matrix = [[1,2,3],[4,5,6],[7,8,9]]


row1 = matrix[0]

first_item = row1[0]

print(first_item)
#same
print(matrix[0][0])
print(matrix[1][1])

print("---------------------------------------------")

for row in matrix:
    for num in row:
        print(num)

print("-------------------------------")
grades = [4, 3, 4, 2]
for grade in grades:
    grade += 1
    print(grade)
print(grades)

print("--------------------------------")

for i in range(len(grades)):
    grades[i]+=1
print(grades)

print("--------------------------------")

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"i : {i}, j : {j}, value: {matrix[i][j]}")
        matrix[i][j] +=1

print(matrix)