#Lista
list = [1,2,3]
list.append(4)
#List comprehention
[num**2 for num in x]
#in operator
2 in x # True


x = []
for num in x:
  x.append(num**2)


#Tuplas
tupla = ('Definida', 'com', 'parentesis')
#Tuplala unpacking
x = [(1,2),(3,4)]
for a,b in x:
    print(a)
    print(b)

#Set
set = {'nao','tem','elemento','repetido'}
set.add('da pra adicionar elementos')

#Dictionary
dictionary = {'key':'value','key':['valor', 'pode ser', 'lista']}

#For
seq = list(range(10))
for i in seq:
  range(i,10)

#Function
def my_func(name='Default name'):
"""
THIS IS A DOCSTRING
CAN GO MULTIPLE LINES
"""
  print('My name is'+name)

my_func(name='Jose') # Outra forma de chamar
my_func() # usa nome como default name
my_func #retorna o objeto: function__main__.my_func

# map() and lambda
list(map(lambda num : num*3,2))
#lambda num: num*3 =>
def func(num): return num*3

#filter()
list(filter(lambda num : num%2 == 0, seq))
