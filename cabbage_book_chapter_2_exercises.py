'''
# Exercise 1
number = input("Give me your number: ")
dict = {}
for digit in number:
    if digit in dict.keys():
        dict[digit]+=1
    else:
        dict[digit] = 1
print(dict)


# Exercise 2
number_1 = input("Please input a whole number: ")
result = ""
for digit in number_1:
    result += f"{9-int(digit)}"
print(result)

# Exercise 3
a = [12,3,456,78]
b = ""
for el in a:
    b+= str(el)
print(int(b))

# Exercise 4
def is_equal(list1, list2):
    cnt = 0
    if len(list1) == len(list2):
         for index in range(len(list1)):
            if list1[index] == list2[index]:
                cnt +=1
    if cnt == len(list1):
        return True
    else:
        return False
print(is_equal([3,4,5,6], [3,4,5,6]))             
print(is_equal([3,4,5,6], [3,4,5,7]))   

# Exercise 5
summation = 0
list_numbers = input("Provide me with exceptional numbers: ")
boundary = input("Provide me with an upper boundary: ")
for number in range(1, int(boundary)+1):
    if str(number) not in list_numbers:
        summation+=number
print(summation)

# Exercise 6
a = float(input("Give side 1: "))
b = float(input("Give side 2: "))
c = float(input("Give side 3: "))
if a > b:
    p = b
    b = a
    a = p
if b > c:
    p = c
    c = b
    b = p
if a+b > c:
    print(True)
else:
    print(False)

# Exercise 7
a = int(input("Give me a number: "))
b = int(input("Give me a number: "))
c = int(input("Give me a number: "))

if a > b:
    p = a
    a = b
    b = p
if b > c:
    p = c
    c = b
    b = p
if (a+c)/2 == b:
    print(True)
else:
    print(False)

# Exercise 8

number = int(input("Give me a numeric day of the week: "))

weekdays = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5 : "Friday", 6: "Saturday", 7: "Sunday"}

print(weekdays[number])


# Exercise 9

try:
    a = float(input("Provide me with the first number: "))
    b = float(input("Provide me with the second number: "))
    print("First number is bigger.") if  a > b else print("Second number is bigger or equal to the first")
except ValueError:
    print("Are you sure that you put in a valid number?")
'''
# Exercise 10
a = int(input("First parameter is: "))
b = int(input("Second parameter is: "))
print((b-1)/a - 1) if a != 0 else print("All numbers are solutions") if a == 0 and b == 1 else print("No solution")