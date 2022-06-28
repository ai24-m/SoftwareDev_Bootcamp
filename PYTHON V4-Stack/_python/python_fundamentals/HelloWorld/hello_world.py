# 1. TASK: print "Hello World"
print("Hello World!")
# 2. print "Hello Noelle!" with the name in a variable
name = "Aziza"
print("Hello ", name , "!")	# with a comma
print("Hello " + name + "!")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello ", name , "!" )	# with a comma
# print("Hello " + name + "!" ) # with a +	-- this one should give us an error!
#Python doesn't know how to add a string and a number, but it can add two strings together, 
#  //so if we can cast the number as a string,  then we will be able to "add" the two values togethe
print("Hello",str(name)) 

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "Ilove to eat {} and {} ".format(fave_food1,fave_food2 )) # with .format()
print(f"I Love to eat  {fave_food1}  {fave_food2}" ) # with an f string
