s1 = {1 , 24 ,56}
s2 = {26 ,89 ,1 ,45}

print(s1.union(s2))
print(s1.intersection(s2))

print({1 , 24}.issubset(s1))

s3 = { 45 , 43 , 67}
s4 = { 45 , 43 , 67 , 56 , 89}
print(s4.issuperset(s3))

s5 = {1 , 2 , 3}
s6 = {3 , 4 , 5}
print(s5.symmetric_difference(s6))  #Returns a new set with elements in either set but not in both.

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.difference(s2))  # Returns a new set with elements in the set that are not in any of the other sets provided as arguments

