def f_to_c(f):
    return 5*(f-32)/9

f = int(input('enter temperature in F: '))
c = f_to_c(f)
print(f'{round(c , 2)}..°C')    #by using round and 2 after comma it will round to two decimal points
