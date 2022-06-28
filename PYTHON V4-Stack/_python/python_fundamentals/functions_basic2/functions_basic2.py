
print("Create a function that accepts a number as an input. Return a new list that counts down by one, from the number.")
# Example: countdown(5) should return [5,4,3,2,1,0]
def  countDown(num):
    newList = []
    for i in range(num, -1, -1):
        newList.append(i)
    return newList
print(countDown(5))

print("Create a function that will receive a list with two numbers.Print the first value and return the second. ")
# Example: print_and_return([1,2]) should print 1 and return 2
def printReturn(list):
    print(list[0])
    return list[1]
print (printReturn([1,2]))

print("Create a function that accepts a list and returns the sum of the first value in the list plus the list's length. ")

arr1=[1,2,3,4,5,6]

def first_plus_length(list):
    x=len(list) + list[0]
    # print(list.len+list[0])
    return x
print(first_plus_length(arr1))

# Write a function that accepts a list and creates a new list containing only the values 
# from the original list that are greater than its 2nd value. Print how many values this 
# is and then return the new list. If the list has less than 2 elements, have the function 
# return False

def valGrtsecond(list):
    if len(list)<2:
        return False
    newList = []
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList
print(valGrtsecond([75,6,3,54,6,78,15,1]))
print(valGrtsecond([8,0,3,54,0,78,15,1]))
print(valGrtsecond([3]))
print(valGrtsecond([]))



# Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, 
# and whose values are all the given value.

def lengthValue(size,value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList
print(lengthValue(5,2))