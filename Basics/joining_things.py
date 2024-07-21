flowers = [
    'daffodil' ,
    'evining primrose' ,
    'hydrangea' ,
    'lavender' ,
    'sunflower' ,
    'tiger lily' ,
]

#for flower in flowers:
#    print(flower)

separator = ' | '  #in this semi colon if you give comma it will give code with seperating words with comma or a slash it gives slash as result
output = separator.join(flowers)
print(output)

print(', '.join(flowers))  #you have to be careful to use join all those should be strings it should not be a integer
