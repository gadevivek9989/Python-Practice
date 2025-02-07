#def increase_all(values: list):
#    for i in range(len(values)):
#        values[i] += 1

#results = [5,2,4,7]
#r2 = results
#increase_all(results)
#print(results)

#using return
def second_smallest(value: list)->int:
    value2 = sorted(value)
    return value2[1]

num = [9,7,5,8,6,3]

s = second_smallest(num)
print(s)

print(num)

#dictonaries

results = {"paul" : 9, "peter" : 6, "paula" : 10, "jim" : 6}
print(results["jim"])

if "vivek" in results:
    print("its there\n")
else:
    print("its not there\n")

results["oliver"] = 5 #this adds into the dictonary

print(results)

students = {1234 : "peter", 2345 : "vivek" , 3456 : "oliver"}
removed = students.pop(1234)
print(students)
for key,values in students.items():
    print(key,values)

s1 = ('simon jones',45,'simonjones35@gmail.com')
s2 = ('vivek',36,'vivek35@gmail.com')
s3 = ('vikas',55,'vikas3@gmail.com')

students = [s1,s2,s3]
for student in students:
    print(student[2])

s1 = (s1[0],50,s2[1])

