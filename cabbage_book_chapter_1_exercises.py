# Exercise 1
day = input("Give me a day: ")
month = input("Give me a month: ")
if day == "1" or day == "21" or day == "31":
    print(f"Today is {day}st of {month}.")
elif day == "2" or day == "22":
    print(f"Today is {day}nd of {month}.")
elif day == "3" or day == "23":
    print(f"Today is {day}rd of {month}.")
else:
    print(f"Today is {day}th of {month}.")

# Exercise 2
present_year = input("What year are we in now? ")
year_of_birth = input("What is your year of birth? ")
years = int(present_year)- int(year_of_birth)
print(f"You are {years} years old.")

# Exercise 3
miles = input("Type in the distance in miles: ")
kilometers = int(miles)*1.6
print(f"The distance is {kilometers} kilometers.")

# Exercise 4
l = input("Tell me the length of the list: ")
print([2**i for i in range(int(l))])

# Exercise 5
a = [5*k+3 for k in range(10)]
print(a)
print(a[-1:-len(a):-1])

# Exercise 6
number = input("What is your number? ")
if int(number) % 3 == 0:
    print("Your number is divisible by three.")
else:
    print("Your number is not divisible by three.")

# Exercise 7
def factorial(a):
    if a == 0:
        return 1
    else:
        return a*factorial(a-1)
number = int(input("Please provide a whole number: "))
if number < 0:
    print("Please provide a non-negative whole number")
else:
    print(factorial(number))

# Exercise 8
def fibonacci(a):
    if a == 0:
        return 1
    elif a == 1:
        return 1
    else:
        return fibonacci(a-1)+fibonacci(a-2)
    
fib_number = int(input("How many members does the sequence have? "))
print([fibonacci(i) for i in range(fib_number)])

# Exercise 9
# Implement a quicksort


items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]


def second_largest(dataset, first, last):
    if first < last:
        # calculate the split point
        pivotIdx = partition(dataset, first, last)

        # now sort the two partitions
        second_largest(dataset, first, pivotIdx-1)
        second_largest(dataset, pivotIdx+1, last)
    return dataset[-2]


def partition(datavalues, first, last):
    # choose the first item as the pivot value
    pivotvalue = datavalues[first]
    # establish the upper and lower indexes
    lower = first + 1
    upper = last

    # start searching for the crossing point
    done = False
    while not done:
        # advance the lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1

        # advance the upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1

        # if the two indexes cross, we have found the split point
        if upper < lower:
            done = True
        else:
            # exchange the two values
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # when the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point index
    return upper

print(second_largest(items, 0, len(items)-1))

# Exercise 10
def oddsum(count):
    summation = 0
    for i in range((count)):
         summation+=(i*2+1)
    return summation
print(oddsum(7))
    
    
