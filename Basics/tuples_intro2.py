albums =[('welcome to my nightmare' , 'alice cooper' , 1975),
    ('bad company', 'bad company',1947),
    ('nightflight', 'budgie' , 1981),
    ('more mayhem', 'emilda may',2011),
    ('ride the lightning', 'metallica' , 1984)]

print(len(albums))



for album in albums:
    name,artist,year = (album[0],album[1],album[2])
    print("Album:{} , artist:{} , year:{}".format(name,artist,year))

print('space')

for album in albums:
    name,artist,year = album
    print("Album:{} , artist:{} , year:{}".format(name,artist,year))

print('space')

for name,artist,year in albums:
    print("Album:{} , artist:{} , year:{}".format(name,artist,year))

#this all gives same output but different ways of unpacking methods used above
