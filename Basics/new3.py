#name = 'G.Vivek Reddy'
#print(len(name))

#index = 0
#while index< len(name):
#    print(name[index])
#    index = index + 1


name = input('please give a sentence\n')
words = 0
index = 0

while index < len(name):
    if (name[index]==" "):
        words = words + 1
    print(name[index])
    index = index + 1
    


print('the no.of words in the string are {}'.format(words+1))




