'''
#Tunniplaani oma
tunniplaan = ["mate", "inka", "vene", "kunst", "arvuti"]

print(tunniplaan)#prindib terver tunniplaane

print(tunniplaan[0])#printib esimese tunni

print(len(tunniplaan))#prindib kui palju tunde on kokku

#prindib kas Kunsti on tunniplaanis
try:#proovi otsida listist kunst
    print(tunniplaan.index("Kunst"))
except ValueError:#kui seda pole siis prindib järgneva
    print("seda pole")
'''
'''
#numbrite oma
a = [1, 12, -3, 4, 0]

#prindib kõik peale esimese
for i in range(0,4,1):
    print(a[i])

#prindib vahemikus 0 kuni 3
for i in range(0,3,1): 
    print(a[i])


print(min(a))

#sorteerib järjendi
#a.sort()
print(a)

#lisab 9 järjendisse
a.append(5)
a[5]= 9
print(a)

a[0]=5
print(a)
'''
'''
#kahe järjendi ülesanne
a = ['A', 'B', 'C']
b = [1, 2, 3]

print(a+b)#liidab järjendid

#b.extend([4])#lisab järjendisse arvu
print(b)#prindib uuendatud järjendi

print(sum(b))#prindib järjendis olevate arvude summa

#Tsükkel mis prindib järjendi a sisemuse üksteise alla
o=0
while o<3:
    print(a[o])
    o +=1
#tsükkel mis muudab kõik väiksemad arvud 0'iks
i=0
while

#tsükkel mis prindib b järjenid
h = 0
while h < 3:
    print(b[h])
    h += 1
'''
'''
g=[]
for i in range(3):
    g.append(i)
    print(i)
print(g)
'''
'''
#prinditakse arvud 2 kuni 5
for i in range(2,5,1):
    print(i)
'''
'''
#prindidakse paarisarvud 2,4,6
for i in range(2,7,2):
    print(i)
'''
'''
#prindib -1 ja -3
for i in range(-1,-4,-2):
    print(i)
'''
'''
korrutis=15
for i in range(1,6,2):
    korrutis=3*i
print(korrutis)
'''