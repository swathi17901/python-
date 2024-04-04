'''
#syntax error
x=43
if x==43
    print(x)
   
#runtime error
#name error
    print(x)

#type error
x='100'
y=56
z=x+y

#index error
x=['good','wealth','happy']
print(x[2])

#attributes error
x="pooja"
x.reverse()



#logical error
def fact(n):
    r=1
    for x in range(1,n+1):
        r=r*i
    return r
print(fact(n))

'''
try:
    x=int(input("Enter a number:"))
    y=10/x
    print("the result is :",y)
except valueerror:
    print("you must enter a valid integer")
except zerodivisionerror:
    print ("you cannot divide by zero")
    
    

