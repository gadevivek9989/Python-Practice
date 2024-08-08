p1 = 'subscribe now'
p2 = 'purchase now'
p3 = 'click here'
p4 = 'make a lot of money'

message = input('enter your comments')

if(p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print('your comment is spam')

else:
    print('your comment is not spam')