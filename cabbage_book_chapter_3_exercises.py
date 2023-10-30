from random import *
'''
# Exercise 1
diff = int(input("Provide me with integer step: "))
text = input("Show me your text\n") 
print(tuple(text[index] for index in range(len(text)) if index % diff == 0))

# Exercise 2
number = input("Provide me with a whole number: ")
print(tuple(number), tuple(number)[-1::-1])

# Exercise 3
seed(42)
def symbs (m,n):
    val = "A"
    return [[chr(ord(val)+randint(1,10)) for i in range(n)] for j in range(m)]
print(symbs(4,3))


# Exercise 4

# Exercise 5
a = [[randint(1,10) for i in range(5)] for j in range(5)]
print(a)
b = int(input("Give me the column you want to delete: "))
for i in range(5):
    del(a[i][b-1])  
del(a[b-1])
print(a)

# Exercise 6

def bubble(a):
    b = len(a)
    for j in range(b):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                temp = a[i+1]
                a[i+1] = a[i]
                a[i] = temp
        b-=1
    return a
print(bubble([3,2,4,8,5,9,1,3,6]))

# Exercise 7

def bobba (mando):
    return [max(mando), mando.index(max(mando))]

print(bobba([3,2,4,8,5,9,1,3,6]))

# Exercise 8 

a = [randint(1,100) for i in range(15)]
print(a)
b = [a[i] for i in range(15) if i % 2 == 0]
c = [a[i] for i in range(15) if i % 2 != 0]
c.sort(reverse = True)
b.sort()
for i in range(len(b)):
    a[i*2] = b[i]
for i in range(len(c)):
    a[i*2+1] = c[i]
print(a)

# Exercise 9

a = [randint(1, 10) for k in range(15)]
print(a)
[a.insert(i+1, a[i]+a[i+1]) for i in range(27) if i % 2 == 0]
print(a)

# Exercise 10
a = [randint(1, 10) for k in range(15)]
b = [randint(1, 10) for k in range(15)]
c = [a[i] if i%2 == 0 else b[i] for i in range(15)]
d = []
for i in range(15):
    d.append(a[i])
    d.append(b[i])
print(a)
print(b)
print(c)
print(d)
'''


