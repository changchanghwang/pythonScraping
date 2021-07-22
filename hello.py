print('hello world')
print('------------------------------------------------------')

a = 2
b = 3
print (a+b)

first_name = 'Changhwan'
last_name = 'Hwang'
print (first_name + last_name)

num = '2'
print(first_name+num)
print('------------------------------------------------------')

a_list = ['사과', '배', '감']
print(a_list)

a_list.append('귤')
print(a_list)
print('------------------------------------------------------')

a_dict = {'name':'bob', 'age':27}
print(a_dict['age'])
a_dict['height'] = 178
print(a_dict)
print('------------------------------------------------------')

def sum(num1, num2):
    return num1+num2
result = sum(2,3)
print(result)
print('------------------------------------------------------')

age = 15
if age > 20:
    print('성인입니다')
else:
    print('청소년입니다.')
print('------------------------------------------------------')

def is_adult(age):
    if age > 20:
        print('성인입니다')
    else:
        print('청소년입니다')

is_adult(30)
is_adult(15)
print('------------------------------------------------------')

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
count = 0
for ff in fruits:
    if ff == '배':
        count += 1
print(count)
print('------------------------------------------------------')

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    print(person['name'], person['age'])
