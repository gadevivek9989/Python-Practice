A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]

c= [[0 for i in range(len(A[0]))] for i in range(len(A))]

for i in range (len(A)):
    for j in range (len(A[i])):
        c[i][j] = A[i][j] + B[i][j]

print(c)

def print_many_times(char,num):
    print(char*num)

print_many_times("hi\n",5)

char = "i am topper of the class\n"
num = 5
print_many_times(char,num)

def hash_square(num):
    for i in range(num):
        print("#"*num)

hash_square(5)
print()
hash_square(3)

def chessboard(num):
    for i in range(num):
        row=''
        for j in range(num):
            if (i+j)%2 == 0:
                row += '1'
            else:
                row+= '0'
        print(row)

chessboard(4)

a = [1,2,3]


a[0] = 10
print(a)