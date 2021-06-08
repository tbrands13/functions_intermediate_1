# 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ]
x [1][0] = 15
print(x)
#
#  2. Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students [0]['last_name'] = 'Bryant'
print(students)

# 3. In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory ['soccer'] [0] = 'Andres'
print(sports_directory)

# 4. Change the value 20 in z to 30
z = [{'x': 10, 'y': 20}]
z [0]['y'] = 30
print (z)


# 2. Iterate Through a List of Dictionaries
heroes = [
    {'first_name': 'Izuku', 'last_name': 'Midoriya'},
    {'first_name': 'Katsuki', 'last_name': 'Bakugou'},
    {'first_name': 'Shoto', 'last_name': 'Todoroki'},
]
def iterateDictionary(lst):
    for x in range (0,len(lst), 1):
        for key, val in lst[x].items():
            print (key, '-', val)

iterateDictionary(heroes)



# 3. Get Values From a List of Dictionaries
def iterateDictionary2(lst):
    for x in range (len(lst)):
        print(lst[x]['first_name'])

iterateDictionary2(heroes)

def iterateDictionary2(lst):
    for x in range (len(lst)):
        print(lst[x]['last_name'])

iterateDictionary2(heroes)


# 4. Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(coding):
    for x,y in coding.items():
        print(f'{x} {len(y)}')
        for value in y:
            print(value)
printInfo(dojo)
