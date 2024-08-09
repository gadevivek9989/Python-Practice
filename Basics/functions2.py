def multiply(x,y):
    result = x * y
    return result


def is_palindrome(string):
    #backwards = string[::-1]
    #return backwards == string
    return string[::-1].lower() == string.lower()


word = input('please enter a word to check: ')
if is_palindrome(word.lower()):                #if you not enter lower() or casefold() then if you enter mixed captial and small letter words it gives you worng output or you can add these near return string and near string
    print("'{}' is a palindrome ".format(word))
else:
    print("'{}' is not a palindrome".format(word))
