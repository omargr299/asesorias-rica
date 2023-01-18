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



