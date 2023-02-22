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

keskmine= (sum(sammude_list)/len(sammude_list))
print("keskmine sammude arv oli",round(keskmine),".")#keskmine arvutamine

minimum = min(sammude_list)
päev = sammude_list.index(minimum)
print("kõige väiksem sammude arv oli",minimum,"ja see on ",päev,"päev"".")#prindb vähima arvu

maximum = max(sammude_list)
päev2 = sammude_list.index(maximum)
print("kõige suurem sammude arv oli",maximum,"ja see on ",päev2,"päev"".")#prindib suurima arvu
'''
'''
#ÜL2
f = open('kilpkonn.txt')#teeb .txt faili lahti
from googletrans import *
translator = Translator
k2sud = []
f = open('kilpkonn.txt')#teeb .txt faili lahti
for rida in f:
    k2sud.append(rida.strip())#loob iga failis olevale reale listis indeksi koha

print(k2sud)
det = translator.detect(self,"Tere")
t6lge = translator.translate(det,dest=en)
print(t6lge)
'''

#ÜL2.2
import turtle
kilpkonn=[]
f = open('kilpkonn.txt')#teeb .txt faili lahti
for rida in f:
    kilpkonn.append(rida.strip())#loob iga failis olevale reale listis indeksi koha
f.close()#paneb kinni faili
r=0
arv=input("Sisestage kujundite arv: ")
g=0
t=turtle

while r<=int(arv):
    kilpkonn[0] == t.forward(100)
    kilpkonn[1] == t.right(120)
    kilpkonn[2] == t.forward(100)
    kilpkonn[3] == t.right(120)
    kilpkonn[4] == t.forward(100)
    break
def joonista (self):
    kilpkonn[0]
    kilpkonn[1]
    kilpkonn[2]
    kilpkonn[3]
    kilpkonn[4]

for i in range(int(arv)):
    joonista

t.done()

