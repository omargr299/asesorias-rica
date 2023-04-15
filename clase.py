# ---ciclos---
# num = 0
""" while( num!=10 ):
    num+=1
    if num==5: 
        print("hola")
        continue
    print(num) """

""" while( num!=10 ):
    num+=1
    if num==5: 
        print("hola")
        break
    print(num) """

""" print(list(range(10)))
for i in range(10):
    print(i) """

""" for i in [1,3.14,"hola",True,[1,2,3]]:
    print(i) """

# ---arreglos---

# arr = [1,2,3]
# indexacion
# print(arr[2])

#sublistas
""" arr = list(range(10))
print(arr[0:4])
print(arr[4:10])
print(arr[:])
print(arr[4:9:2])
arrmew = arr[4:8]
print(arrmew,arr) """

# funcion len
""" print(len(arr))
print(len("hola")) """

# ---string---
""" string = "ballena"
# print(string[0])
for i in string:
    if i=="a": print(i) """

# operaciones con areglos
""" arr = [1,2,3,4,5]
print(arr+[5,6,7])
print(arr*3)
s = "hola"
print(s+" rica")
print(s*3) """

# copia vs referencia
""" v1 = 3
v2 = v1
v1+=1
v2+=2
print(v1,v2)
a = [1,2,3]
b = a
c = b.copy()
b.append(5)
print(a,b,c)
a = "str"
b = a
b+="aaa"
print(a,b) """

# ---Tuplas, Diccionarios y Uniones---
# () Tuplas
# {} Diccionarios
# [] Listas

""" lis = [1,2,3,4,5]
print(type(lis))
tupla = (1,2,3,4,5) # la tupla no se puede alterar
print(type(tupla))
print(tupla) """
#tupla[1] = 5 ERROR

# clave: valor
""" dic = {"a": 1, "b": 2} #la clave siempre es unica para cada elemento
print(type(dic))
print(dic)
print(dic["a"]) # se indexa por claves
dic[6] = "hola"
print(dic) """

#indexa claves
""" for clave in dic:
    print(clave) """

#para obtener los valores

#indexar con la clave
""" for clave in dic.keys():
    print(dic[clave]) """

#obtinenes los valores con una funcion
""" for valor in dic.items():
    print(valor)
    print(valor[1]) """


""" a = [1,2,3]
b = [4,5,6,8]
print(list(zip(a,b))) """

# funciones

""" def saludo():
    print("Hola")
saludo()
saludo()
saludo()
saludo() """

""" def suma():
    a = 1
    b= 2
suma()
def imprimir(x):
    print(x)
def resta(a,b):
    res = a-b
    return res
    
    print("a")
print(resta(1,2))
print("as","asf","asdasf") """

# valores por defecto
""" def division(a,b=1):
    return a/b
print(division(2))
print(division(2,3)) """

# desempaqutamiento

""" arr = [1,2,3]
a,b,c = arr
print(a,b,c)
#errores
arr = [1,2,3,4]
a,b,c = arr
print(a,b,c) 
arr = [1,2,3]
a,b,c,d = arr
print(a,b,c)
arr = [1,2,3,4]
a, b, *c = arr
print(a,b,c)
arr = [1,2,3,4]
*a, b, c = arr
print(a,b,c)
arr = [1,2,3,4]
a, *b, c = arr
print(a,b,c)"""

""" def suma(a,*b):
    for i in b:
     a+=i
    print(a)
suma(1,2,3)
nums = [1,2,3,4,5]
suma(*nums)

def algo():
    return "hola"

def suma(a,b):
    sum = a+b

def lista():
    return [1,2,3]

# None != True False "" [] 0
print( algo() )
print( suma(1,2) )
var = algo()
print(var)

var = lista()
print(var)
print(*var)
a,b,c = lista()
print(a)

a = 0
_a = 0
a123 = 0

# funciones de orden superior
def funcion():
    print("hola")

funcion()
var = funcion()
print(var)
var = funcion
var()
num = 1
num = [3]
num[0]

def funcion2(func):
    print('soy una funcion de orden superior y hago esto:')
    func()

funcion2(funcion)"""


class EmpleadoAccenture:
    empresa = "Accenture"

    def __init__(self,_id):
        print('se creo un empleado')
        self.id = _id

    def __del__(self):
        print('adios')

    def __add__(self,other):
        return self.id + other.id

    def saludar(self):
        print('hola')

    def cambiar_id(self,new_id):
        self.id = new_id


print(EmpleadoAccenture.empresa)
# assert 1==2

empleado1 = EmpleadoAccenture(1)
empleado2 = EmpleadoAccenture(2)
print(empleado1.empresa)
print(empleado2.empresa)
# print(EmpleadoAccenture.id)
print(empleado1.id)
print(empleado2.id)
# EmpleadoAccenture.saludar()
# del empleado2
empleado1.saludar()
empleado1.cambiar_id(3)
print(empleado1.id)

empleado3 = empleado1
print(empleado3.id)

empleado4 = EmpleadoAccenture(4)
print(empleado1+empleado2)
print(empleado1+empleado2+empleado4)
