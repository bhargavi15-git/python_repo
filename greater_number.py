
#Four number comparison
print("Enter all four numbers to be compared")
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())

def compare(nu1:int,nu2:int,nu3:int,nu4:int):
    """This code will only work for positive,negative and zero numbers"""
    if nu1>nu2 and nu1>nu3 and nu1>nu4:
         greater=nu1
    elif nu2>nu3 and nu2>nu4:
         greater=nu2
    elif nu3>nu4:
         greater=nu3
    else:
         greater=nu4
    return greater

print("The greater number is:",compare(num1,num2,num3,num4))
'''
#Three number comparison:
print("Enter all Three numbers to be compared")
num1=int(input())
num2=int(input())
num3=int(input())


def compare(nu1:int,nu2:int,nu3:int):
     """This code will only work for positive,negative and zero numbers"""
     if nu1>nu2 and nu1>nu3:
         greater=nu1
     elif nu2>nu3:
         greater=nu2
     else:
         greater=nu3
     return greater

print("The greater number is:",compare(num1,num2,num3))'''