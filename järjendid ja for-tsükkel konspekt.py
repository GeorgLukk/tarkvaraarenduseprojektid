'''
number = [ 0, 'üks', 2, 'kolm']#järjendid võivad olla erinevat tüüpi
print(number[1])
tühi_järjend = []#võib olla ka tühi järjend
numbrid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]#numbritega näide järjendist
#pythonis algab indekseerimine 0'st
list = ["Tere", "headaega"]
print (list[0])
nädalapäevad = ["esmaspäev", "teisipäev", "kolmapäev", "neljapäev", "reede", "laupäev", "pühapäev"]
#nädalapäevad = ["esmaspäev"#0, "teisipäev"#1, "kolmapäev"#2, "neljapäev"#3, "reede"#4, "laupäev"#5, "pühapäev"#6]
nimi = ['Malle', 'Volli', 'Salme', 'Kustav']#tekitatakse loend nimedest
print (nimi[0])#tahetakse väljastada nime mille indeks on 0 ehk Malle
#SPLIT JA JOIN meetodid
#split poolitab lause kaheks sealt kus on vahe sees(võib ka defineerida sulgudes millest poolitada)
'Tere hommikust'.split()
['Tere', 'hommikust']
#Join alguses defineeritakse kust neid liidetakse ja siis antakse sulgudesse sõnad mida liita
' '.join(['Tere', 'hommikust'])
'Tere hommikust'
#FOR
#Näide 1
for linn in ["Tartu", "Tallinn", "Põltsamaa"]:
    print("Muutuja linn väärtus: " + linn)
#prindidakse esimene "" + esimene , teine , kolmas
#Näide 2
a = [12, 23, 34, 45, 56]
i = 0
for el in a:
    if el > 30:
        i += 1
print(i)
#prinditakse 12 siis 23 jne kuna seal koodis on i+= 1 siis liidedakse i'le antud indeksile 1 juurde

#FOR RANGE
#For range varjandid
list(range(5))
[0, 1, 2, 3, 4]
print(list(range(5)))
print(list(range(0,5)))
list(range(0, 15, 2))
[0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(0,15,2)))#annab sellest range funktsioonist ainult paarisarvud
list(range(5, 0, -1))
[5, 4, 3, 2, 1]
print(list(range(5, 0, -1)))
for i1 in range(5):#teeb endale range funktsiooni nimega i
    print(i1)#prindib funksiooni range i 0,1,2,3,4
for i2 in range(1,5,1):#teeb range funktsiooni 1st 4ni
    print(i2)#prindib selle range funktsiooni 1,2,3,4
'''

arvud = [2,4,6,7,2]#tehakse järjend nimega arvud
for i in range(0,5,1):#for range indeksitega 0-5 ning vahe nende indeksitel on 1
    print(arvud[i])#prindib arvud järjendist
#roberti test
arvud = [2,4,6,7,2,99]#tehakse järjend nimega arvud
for i in range(0,6,5):#for range indeksitega 0-6 ning vahe nende indeksitel on 6
    print(arvud[i])#prindib arvud järjendist

#saab ka lisada elemendi järjendi lõppu
a = []
a.append(2)
a = [2,3,4,2,6,]#loob järjendi nimega a
a[2] = 90
a.append(5)#loob indeksile uue sisendi
a[5] = 99#täidab indeksi 5 sisendi
a.remove(2)#removib ära selle arvu järjendist mitte indeksi
a.append(6)#loob indeksile uue sisendi
a[5] = 1#täidab indeksi 6 sisendi
#a.sort()
print (a)#prindib a järjendi

'''
#Sellisel moel saab ka .txt failidest võtta ridu ning väljastada neid python failis
#1
f = open('andmed.txt')#teeb .txt faili lahti
for rida in f:
    print('Lugesin järgneva rea: ' + rida)
f.close()#paneb kinni faili

#2
f = open('nimed.txt')#avab faili
while True:
    nimi = f.readline() #loeb failist antud rea
    if nimi == "":#kui pole seal midagi anda annab see tühja vastuse
        break
f.close()#paneb kinni faili

#näide failist lugemisel
import random#impordib randon funsiooni
nimekiri = []#teeb tühja järjendi
f = open('nimekiri_10it.txt',encoding='utf-8')#lisatakse fail ning selle nimi ja kooding
for rida in f:
    nimekiri.append(rida.strip())#hakatakse faili lugema iga rida
f.close()#suleb faili
suvaline = random.randint(0,len(nimekiri)- 1)#loob suvalise'le enda range'le
print('suvaline asi on: '+nimekiri[suvaline])#prindib suvalise'le antud rantgest midagi
'''