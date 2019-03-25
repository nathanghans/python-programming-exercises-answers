#get user input
answer = int(input("insert a number > "))
i = 1

#set loop variable
loop = answer - 1
#make a constant for the while loop
constant = answer
#factorial loop
while i < constant:
    #factorial equation
    answer = answer * loop
    #decrement the loop
    loop = loop - 1
    #increment the while.
    i = i +1

#print answer
print(answer)
