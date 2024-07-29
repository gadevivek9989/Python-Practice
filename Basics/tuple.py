tup = (1 , 2 , 76 , 342 , 42 ,'green' , True)
print(type(tup),tup)
print(tup[0])
print(tup[-1])
print(tup[5])


if 342 in tup:
    print('yes 342 is in this tuple')

tup2 = tup[0:4:2]
print(tup2)

tup3 = (2 , 3 , 4 ,5 , 6,7 ,8 ,9)
print(len(tup3))
print(max(tup3))
print(min(tup3))
print(sum(tup3))

tup4 = tup + tup2 + tup3
print(tup4)