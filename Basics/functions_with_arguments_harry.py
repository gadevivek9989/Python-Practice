def goodday(name, ending):
    print('GOOD DAY' + name)
    print(ending)

goodday(' vivek', "thank you")
goodday(' vikas', "thank you")
goodday(' rohit', "thanks")

#def goodday(inside this you enter is called argument)


def goodday(name, ending):
    print('GOOD DAY' + name)
    print(ending)
    return "ok"

a = goodday(' vivek', "thank you")
print(a)
