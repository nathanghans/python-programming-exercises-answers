#all numbers
allnum = range(2000,3201)
#try it with a set
y = set()
#try it with an array
a = []

#loop
for i in allnum:
    #nested ifs... should have used and
    if i % 7 == 0:
        if i % 5 == 1:
            #add values
            y.add(i)
            a.append(str(i))

#print values
print(y)
print(a)

#print without brackets
print(','.join(a))