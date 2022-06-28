print("Given a list, write a function that changes all positive numbers in the list to big")
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, 
# but whose values are now [-1, "big", "big", -5]
def biggie_size(list):
    for i in range(len(list)):
        if list[i]>0:
            list[i]="big"
    return list
print(biggie_size([-1, 3, 5, -5]))

print("Given a list of numbers, create a function to replace the last value with the number of positive values")
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(list):
    count = 0
    for i in list:
        if i > 0:
            count += 1
    list[len(list)-1] = count
    return list

print(count_positives([-1,1,1,1]))


print("Create a function that takes a list and returns the sum of all the values in the array.")
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(list):
    sum = 0
    for i in list:
        sum += i
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))


print("Create a function that takes a list and returns the average of all the values.")
# Example: average([1,2,3,4]) should return 2.5
def average(list):
    sum = 0
    for i in list:
        sum += i
    return (sum/len(list))
print(average([1,2,3,4]))

print("Create a function that takes a list and returns the length of the list.")
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(list):
    return len(list)
print(length([37,2,1,-9]))
print(length([]))


print("Create a function that takes a list of numbers and returns the minimum value in the list.If the list is empty, have the function return False ")

# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
# def minFun(array):
#     if len(array)<0:
#         return False
#     minInt = array[0]
#     for val in array:
#         if val<minInt:
#             minInt = val
#     return minInt
# print(minFun([600,80,99,26,3,5]))
def minimum(list):
    if len(list)==0:
        return False
    for i in range(len(list)):
        minInt = list[0]
        if list[i]<minInt:
            minInt = list[i]
    return minInt
print(minimum([37,2,1,-9]))


def Maximum(list):
    if len(list)==0:
        return False
    for x in range(len(list)):
        maxi = list[0]
        if (list[x]>maxi):
            maxi=list[x]
    return maxi
print(Maximum([37,2,1,-9]))
print(Maximum([]))


print("Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.")
# Example: ultimate_analysis([37,2,1,-9]) 
# should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }


def ultimate_analysis(list):
    _dictionary = {'sumTotal':[0] ,
                   'average': [0] ,
                    'minimum': [0] , 
                    'maximun': [0] , 
                    'length': [0] }
    _dictionary.update({"sumTotal" : sum_total(list)})
    _dictionary.update({"average" : average(list)})
    _dictionary.update({"minimum" : minimum(list)})
    _dictionary.update({"maximum" : Maximum(list)})
    _dictionary.update({"length" : length(list)})
    return _dictionary
print(ultimate_analysis([37,2,1,-9]))
print(ultimate_analysis([1,0]))



print("Create a function that takes a list and return that list with values reversed. Do this without creating a second list. ")
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
# def reverse_list(list):
#     for i in range(0, (len(list)-1)//2):
#         temp = list[i]
#         list[i] = list[len(list)-1-i]
#         list[len(list)-1-i] = temp
#     return list
def Reverse_List(list):
    return list[::-1]
print(Reverse_List([37,2,1,-9]))