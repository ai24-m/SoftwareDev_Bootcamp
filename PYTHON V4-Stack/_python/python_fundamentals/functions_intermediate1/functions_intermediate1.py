import random
def randInt(min = 0,max = 100):
        if max>0 and min<max: 
          if max != 100 and min != 0:
            return round(random.random()*(max-min)+min)
        if min != 0:
            return round(random.random()*(100-min)+min)
        if max != 100:
            return round(random.random()*max)
        else:
          print("Try again, The numbers should be min > max and  max < 0")
        return round(random.random()*100)

print(randInt())
print(randInt(max = 50))
print(randInt(min = 50))
print(randInt(min = 50, max = 500))



