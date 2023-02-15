#Georg Lukk IS22
'''
#ÜL1
sammude_list=[]
f = open('sammud.txt')#teeb .txt faili lahti
for rida in f:
    sammude_list.append(rida.strip())#loob iga failis olevale reale listis indeksi koha
f.close()#paneb kinni faili

print("erinevatel päevadel tehtud sammude arv", sammude_list,".")

#listi int failitüübiks tegemine
with open('sammud.txt') as f:
    sammude_list = [ int(i) for i in f ]

sammud_kokku = sum(sammude_list)
print("sammude arv kokku",sammud_kokku,".")

print("keskmine sammude arv oli",sum(sammude_list)/len(sammude_list),".")#keskmine arvutamine

print("kõige väiksem sammude arv oli",min(sammude_list),".")#prindb vähima arvu

print("kõige suurem sammude arv oli",max(sammude_list),".")#prindib suurima arvu
'''
'''
#ÜL2f = open('sammud.txt')#teeb .txt faili lahti
from googletrans import *
trans = Translator
k2sud = []
f = open('kilpkonn.txt')#teeb .txt faili lahti
for rida in f:
    k2sud.append(rida.strip())#loob iga failis olevale reale listis indeksi koha

print(k2sud)
det = trans.detect(k2sud)
t6lge = trans.translate(k2sud,dest=en)
print(t6lge)
'''
#ÜL2.2
import turtle
kilpkonn=[]
f = open('kilpkonn.txt')#teeb .txt faili lahti
for rida in f:
    kilpkonn.append(rida.strip())#loob iga failis olevale reale listis indeksi koha
f.close()#paneb kinni faili
print(kilpkonn)
r=0
arv=input("Sisestage kujundite arv: ")
g=0
t=turtle
while r<=(len(kilpkonn)):
    kilpkonn[0]==t.forward(100)
    kilpkonn[1] == t.right(120)
    kilpkonn[2] == t.forward(100)
    kilpkonn[3] == t.right(120)
    kilpkonn[4] == t.forward(100)
    r+=1
    g+=1

while g==arv:
    print(kilpkonn)
    g += 1
    if g==arv:
        t.done()
