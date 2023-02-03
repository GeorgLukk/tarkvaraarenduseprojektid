number = [ 0, 'üks', 2, 'kolm']#järjendid võivad olla erinevat tüüpi
tühi_järjend = []#võib olla ka tühi järjend
numbrid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]#numbritega näide järjendist
#pythonis algab indekseerimine 0'st
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
#prindidakse esimene "" + esimene linn jne
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
list(range(0, 15, 2))
[0, 2, 4, 6, 8, 10, 12, 14]
#saab ka lisada elemendi järjendi lõppü
a = []
a.append(2)
#Sellisel moel saab ka .txt failidest võtta ridu ning väljastada neid python failis
#1
f = open('andmed.txt')#teeb .txt faili lahti
for rida in f:
    print('Lugesin järgneva rea: ' + rida)
f.close()#paneb kinni faili
#2
f = open('nimed.txt')#avab faili
while True:
    nimi = f.readline() #loeb failist antude rea
    if nimi == "":#kui pole seal midagi anda annab see tühja vastuse
        break
f.close()#paneb kinni faili
#näide failist lugemisel
nimekiri = []
f = open('nimekiri_10it.txt',encoding='utf-8')#lisatakse fail ning selle nimi ja kooding
for rida in f:
    nimekiri.append(rida.strip())#hakatakse faili lugema
f.close()#suleb faili
suvaline = random.randint(0,len(nimekiri)- 1)#loob suvalise'le enda range
print(nimekiri[suvaline])#prindib suvalise'le antud rantgest midagi
