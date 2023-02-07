
#Ülesanne 1. Seitse linna I (kohustuslik)
#Koosta järjend, milles on vähemalt seitse Eesti linna ning järjesta need tähestikulisse järjekorda, kasutades selleks vastavat funktsiooni.
#Lisaks väljasta kasutajale lause, kus öeldakse mitu linna on järjendis, kasutades järjendi elementi lugemiseks vastavat funktsiooni.
linnad = ['Tallinn','Tartu','Viljandi','Pärnu','Rakvere','Valga','Haapsalu']#lood linnadele järjendi
linnad.sort()#sorteerid linnad järjekorda
for ik in range (0,7,1):#teeb range linnade järjendile
    print (linnad[ik])#prindib linnad
print ('linnu on kokku: ',len(linnad))#loeb linnad kokku ning völjastab selle

#ÜL 2
#loob järjendid
a = [2, 3, 1, 5]
b = [6, 4]
#liidab järjendid
c= a+b
#sorteerib järjendi
c.sort()
print(c)#väljastab järjendi

#ÜL3
for ik in range (0,7,1):#teeb range linnade järjendile
    print (linnad[ik])#prindib linnad