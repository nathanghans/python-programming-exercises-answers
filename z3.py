n = int(raw_input())
print(n)
#get the number
number = int(input("What number would you like to use: > "))
#define the dictionary
dict = {}

#loop and add i to the dictionary
for i in range(number):
    dict[i] = i * i

#print dictionary
print(dict)
