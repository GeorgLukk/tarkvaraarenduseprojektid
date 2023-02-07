
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

#ÜL4
import turtle
i=0
for i in range (4):
    turtle.fd(50)
    turtle.lt(90)
    i+1
turtle.exitonclick()

#ÜL5
from functools import reduce#impordib recude funktsiooni
d = [3,4,5,2,6]
def add(a,b):#loob funktsiooni
	return a + b #liidab a ja b ning läheb algusesse 3+4 ja läheb tagasi 7 ning nii edasi
the_sum = reduce(add, d)#reduce liidab iga arvu järjest üksteise otsa
print(the_sum)#väljastab lõpptulemuse

#ÜL6
e=[2,4,5,6,12,18]
for paaris in e:#alustab for tsükli mis vaatab e järjendit
    if paaris % 2 == 0:#kui järjendis number jagub 2'ga siis see prindib selle
        print(paaris,end=',')#väljastab paaris numbri ning paneb koma nenede vahele
#end on funksioon mis paneb midagi iga tsükli lõppu (praegusel juhul ,)

#ÜL7
