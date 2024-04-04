'''
liststack=[3,4,5]
print(liststack)

liststack.append(7)
print(liststack)

liststack.append(9)
print(liststack)

liststack.pop()
print(liststack)

#list queue

from collections import deque
queue=deque(["apple","orange","kiwi"])
print(queue)

queue.append("banana")
print(queue)

queue.popleft()
print(queue)
'''

#del

a=[1,2,3,4,5,6,7,8,9]
print(a)

del a[0]
print(a)

del a[2:5]
print(a)

del a[:]
print(a)

del(a)
print(a)
