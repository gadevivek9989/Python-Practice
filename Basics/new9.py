sentence = input("Give a sentence :")

spaces = sentence.count(" ")

print(f"the no.of words in the sentence is {spaces+1}")

list = [1,3,4,4,4,4,4,6,7,8,2,3,5,1,1,1,1,4,4,4]

fours = list.count(4)
print(fours)

sentence1 = 'red dog ran on road though not died'

sentence2=sentence1.replace('dog','cat')
print(sentence2)

name = 'livingstone'

name = name[0].upper() + name[1:]
print(name)