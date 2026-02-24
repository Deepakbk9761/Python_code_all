#2. Non primitive data types

'''1. list '''
# collection of elements or items which is changeable or replaceable
# data=["Deepak",20,"Arghakhanchi"] ### it is start form zero index 
# print(data[0])  ### answer will be Deepak because inverted comma get the index one so
# data[0]="Laxmi" ##it is changeable or replaceable whose value can be changed
# print(data[0])

# print 300 from given number
# number=[200,300,600],
# [600,67,78]
# print(number[0][2])  #index always start from zero 


# print the data 600 from the given data
# data=[
#     [
#         [500, 600, 600,700]
#     ]
# ]
# print(data[0][0][3])


# add 90 to the given data
'''data=[67,66,97]
data.append(90)  #append the data to the end of this list only one value add at a time
print(data)'''

#remove the data
'''data=[67,66,97]
data.remove(97)
print(data)'''

# count the data
'''data=[67,66,97,97]
print(data.count(97))'''

#  insert the data
#data=[67,66,97,97]
#data.insert(2,300) #index le first argument index and second is value(insert object before index )
#data+=[6] #we use the assignment operator replaced by insert 
#print(data)
'''2.tuples'''
#collection of elements or items which is unchangable but allows duplicate values
# like sunday monday tuesday like ek paxi ek aauxa vane we uese tuples

#yadi change garnai paryo vane change into list and make 
'''week=("sunday","Monday", "Tuesday","Wednesday", "Thursday","Friday","Saturday")
print(dir(week))
print(week.count("sunday"))
print(week.index("sunday"))
print(week)'''


'''dictionary'''
# for values insert and remove we use list in every case 
#key values pairs form ma aauxa dictionary always used in single quotes and comma,
'''data = {
    'name': 'Deepak', 'name'=keys, 'deepak'=values ,=pairs
    'age': 20,
    'Address': 'Arghakhanchi', # Added missing comma here
    'contact': {
        'phone': 9856231523,
        'gmail NO': 'deepakbk@gmail.com'
    }
}

print(data['name'])
print(data['age'])
print(data['Address'])

# Changed 'email' to 'gmail NO' to match your dictionary
print(data['contact']['gmail NO'])'''



'''students=[
    {'name':'ram','age':20},
    {'name':'shyam','age':21},
    {'name':'hari','age':23}
]
print(f"my name is {students[0]['name']}")
print(students[2]['name'])'''
'''set'''

# student={
#     'name':'deepak',
#     'age':20,
#     'Address':"kathmandu"
# }
# print(student.get('age','key not found'))
# print(student.pop('name'))
# print(student.values())
# print(student.keys())
# print(student.items())
'''my_bike={
    'name':'Honda',
    'model':2002,
    'age':9

}
my_bike['id']=my_bike['age'] * my_bike['model']  #New featrues add
my_bike['pursing in']=2020  #ADD SOME FEATRUES
print(my_bike)'''

#new key add in user
user={
    'name':'sagar',
    'id':50,
    'age':60,
}
'''print(f"User name is {user['name']}")
print(user.values())
print(user.keys())
print(user['age'],['name'])'''
user['dept']='It'
print(user)


'''set'''
# Note:set and dictionary are also same but some differnt in both simple form ie set and key values and pair form is dictionary
# unique values, unordered , changable collection of items and duplicate value automativ remove it
# to make the set when we use the phone number and gmail etc

# set={34,45,67, 34,78}
# print(set)

