print("Print all integers from 0 to 150.")
print()
for i in range(0, 151):
    print(i)


print(" --- ")

print("Multiples of Five - Print all the multiples of 5 from 5 to 1,000  : ") 
print()
for i in range(1,1000):
  print(i*5)

print(" --- ")

print("Print integers 1 to 100. If divisible by 5,print Coding instead. If divisible by 10, print Coding Dojo")
print()

for i in range (1,101,1):
        if i % 5== 0:
            print ("Coding")
        if i % 10== 0:
            print ("Dojo")


print(" --- ")

print("Add odd integers from 0 to 500,000, and print the final sum")
print()

for _total in range(500000):
    if(_total % 2 != 0):
       _total = _total + _total
print(_total)

print(" --- ")

print("Print positive numbers starting at 2018, counting down by fours")
print()

def countDown():
    num = 2018
    while num > 0:
        print (num)
        num = num - 4
        
countDown()   

print(" --- ")

print("Set three variables: lowNum, highNum, mult. Starting at lowNum going through highNum only the integers that are a multiple of mult")
print()

lowNum=2
highNum=9
mult=3
for flexible in range (lowNum, highNum +1):
        if flexible % mult == 0:
            print (flexible)
            

