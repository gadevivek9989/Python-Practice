#numbers=[1,2,3,4,5,6]

#index=0
#while True:
#    if index<len(numbers):
#        print(numbers[index])
#        index+=1
         

animals=['cat','dog','rat','tiger','buffalo']
all_animals=' '
for animal in animals:
    print(animal)
    all_animals+=animal + ' '
print(all_animals)


number = [3,4,5,6,7,8,9]

sum_number=0
for i in number:
    sum_number+=i

print(sum_number)


list = 'peter is a good boy'

for i in list:
    if i == ' ':
        break
    print(i)