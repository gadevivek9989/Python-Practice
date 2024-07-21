pangram = 'The quick brown fox jumps over the lazy dog'

letters = sorted(pangram)
print(letters)

numbers = [2.3 , 4.5 , 8.7 , 3.1 , 9.2 , 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers) 
print(numbers) 

#by using sorted(stringword) it will be in alphabetical order and if it is in numbers it will be in inreasing order
#to sort we can use this method also srtingword.sort()



#another_sorted_numbers = numbers.sort()
#print(numbers)
#print(another_sorted_numbers)
#by attaching this to line 22 we will get none


numbers.sort()
print(numbers)

#henever you want to perfom a case insentive sort, just add key = str.casefold

missing_letter = sorted('The quick brown fox jumped over the lazy dog',
                        key=str.casefold)
print(missing_letter) 

names = ['Graham',
         'John',
         'eric',
         'Terry',
         'micheal',
         ]
names.sort(key=str.casefold)
print(names)