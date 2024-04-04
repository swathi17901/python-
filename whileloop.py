'''
#while loop
count=4
while count<20:
    print(count)
    count+=3

#while using break
i=1
while i<6:
    print(i)
    if i==7:
     break
    i+=1

#while using else
i=1
while i<6:
        print(i)
        i+=1
else:
    print("i is no longer less than 6") 



count=2
while count <8:
    print(count)
    count=1
   
s=3
while s<5:
    print(s)
    if s==9:
        break
    s+=1


i=1
while i<9:
    print(i)  
    i+=2
else:
    print("i is longer than 9")
 '''
#break
a=7
while a>4:
    print(a)
    if a==6:
        break
    a-=1

a=5
while a>3:
    print(a)
    if a==4:
        break
    a-=1
    
    
#continue
#print all letter except '0' and 'l'
i=0
a="hello world"
while i<len(a):
    if a[i]=='o' or a[i]=='l':
        i+=1
        continue
    print('balance letter:',a[i])
    i+=1
#pass statement
a=7
while a>0:
    pass

    





