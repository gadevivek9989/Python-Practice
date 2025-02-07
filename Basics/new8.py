r = range(1,100000)
s=0
print(r)
for i in r:
    s=s+i
print(s)


num1 = range(1,30,4)
num2 = range(10,0,-1)
values = list(num1)
integer = list(num2)

print(integer)
print(values)

vivek = [1,6,1,4,9,5,6,8,3,1]

vivek.sort()
print(vivek)

vikas = ['rhino','cat','monkey','tiger']
vikas.pop(0)     #removes the word at index 0
vikas.remove('rhino')    #sme as upperline
vikas.sort()
sorted_vivek=sorted(vikas)
print(sorted_vivek)
print(vikas)

