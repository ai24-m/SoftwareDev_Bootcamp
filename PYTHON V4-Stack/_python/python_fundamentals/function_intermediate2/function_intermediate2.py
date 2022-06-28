
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ]
x[1][0]=15

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
# students[1]['']
print(students)


# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'

# Change the value 20 in z to 30
print("Change the value 20 in z to 30")
z = [{'x': 10, 'y': 20}] # this is a list with on dictonary inside

z[0]['y'] = 30
print(z)



# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops 
# through each dictionary in the list and prints each key and the associated value. 
# For example, given the following list:

students2 = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(students_):
    stringReturn = ''
    for val in students_:
        stringReturn += f"first_name - {val['first_name']}, last_name - {val['last_name']}\n"
    return stringReturn
print(iterateDictionary(students2))


print("Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. ")
# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB

def iterateDictionary2(key_name, students_):
    stringReturn = ''
    for val in students_:
        stringReturn += f"{val[key_name]} \n"
    return stringReturn
print(iterateDictionary2('last_name',students2))


print("Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. ")
# For example:

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(_dict):
    for x in _dict:
        print(len(_dict[x]),x.upper())
        for i in _dict[x]:
            print(i)
        print("")
printInfo(dojo)


