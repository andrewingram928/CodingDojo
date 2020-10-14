x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0].update(last_name = 'Bryant')
print(students[0])

sports_directory["soccer"] = ['Andres', 'Ronaldo', 'Rooney']
print(sports_directory)

z[0] = {"x" : 10, "y": 30}
print(z)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(some_list):
  for curr_dict in some_list:
    display_str = ''
    for curr_key in curr_dict.keys():
      display_str += (f"{curr_key} - {curr_dict[curr_key]}, ")
    print(display_str)

iterate_dictionary(students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict.keys():
        print(f"{len(some_dict[key])} {key}")
        for item in some_dict[key]:
            print(item)
        

printInfo(dojo)

