#pythoon3 has 5 sequence types built in;

#the sring type
#list
#tuple
#range
#bytes and bytearray


string1 = "he's"
string2 = "probably"
string3 = "pining"
string4 = "for the"
string5 = "fjords"

print(string1 + string2 + string3 + string4  + string5)

print("he's" "probably" "pining" "for the"  " fjords")

print('hello'*5)
print('hello'* (5 + 4))
print('hello'*5 + ' 4')

today = 'friday'
print('day' in today)        #true
print('fri' in today)        #true
print('thur' in today)      #false
print('parrot' in "fjord")   #false