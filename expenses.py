expenses = [10.30,8,5,15,19,5,3]
sum = 0

#For each one in the loop 
for x in expenses:
    sum = sum + x
# is the same --> sum(expenses)
 
print('You spent $',sum, sep = '')