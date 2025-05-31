### FACTORIAL



n=int(input("ENTER A NUMBER TO FIND ITS FACTORIAL: "))

def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
    
result=factorial(n)
print(result)



#####""" USING FOR LOOP"""

# n = int(input('ENTER A NUMBER TO FIND ITS FACTORIAL: '))
# a=1
# for i in range(1,n+1):
#     a*=i

# print(f'factorial of {n} is {a}')