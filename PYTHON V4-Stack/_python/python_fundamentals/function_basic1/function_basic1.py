#1
print("---------                 1st output ")
def a():
    return 5
print(a()) # the output is : 5




#2
print("---------                 2nd output ")
def a():
    return 5
print(a()+a()) # the output is : 10





#3
print("---------                 3rd output ")
def a():
    return 5
    return 10
print(a()) # the output is : 5




#4
print("---------                 4th output ")
def a():
    return 5
    print(10)
print(a()) # the output is :  5
pass



#5
print("---------                 5th output ")
def a():
    print(5)
x = a()
print(x) # the output is : 5, None

pass



#6
# print("---------                 6th output")
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'


#7
print("---------                 7th output")
def a(b,c):
    return str(b)+str(c)
print(a(2,5))# the output is 25



# #8
# print("---------                 8th output")
# def a():
#     b = 100
#     print(b)

#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())

# SyntaxError: invalid non-printable character U+00A0 # line 75






#9
print("---------                 9th output")
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))# the output is 7
print(a(5,3))# the output is 14
print(a(2,3) + a(5,3))# the output is 21





#10
print("---------                 10th output")
def a(b,c):
    return b+c
    return 10
print(a(3,5))# the output is 8


#11
print("---------                 11th output")
b = 500
print(b)# the output is : 500
def a():
    b = 300
    print(b) 
print(b)# the output is : 500
a()# the output is : 300
print(b) # the output is : 500



#12
print("---------                 12th output")
b = 500
print(b)  # the output is : 500
def a():
    b = 300
    print(b)
    return b
print(b) # the output is : 500
a()  # the output is : 300
print(b) # the output is : 500




#13
print("---------                  13th output")
b = 500
print(b) # the output is : 500
def a():
    b = 300
    print(b)
    return b
print(b) # the output is : 500
b=a() # the output is : 300
print(b) # the output is : 300



#14
print("---------                 14th output")
def a():
    print(1) 
    b()
    print(2)
def b():
    print(3)
a()# the output is : 1,3,2




#15
print("---------                 15th output")
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)# the output is : 1,3,5,10


