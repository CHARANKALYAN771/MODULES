import pandas as p
my_set={
    'car':[1,2,3,4,56,6],
    'bike':[2,3,4,5,4,7],
    'motor':['ck','bmw','ferrari','ford','tata','kia']
}
y=p.DataFrame(my_set ,index=['a','b','c','d','e','f'])
print(y)
print(p.read_csv('app_names.csv') )
z=p.read_csv('app names.csv')
print(z)
x=p.Series(my_set)
print(x)
