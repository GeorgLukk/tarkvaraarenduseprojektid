#Georg Lukk IS22
'''
#ÜL1
sammude_list=[]
f = open('sammud.txt')#teeb .txt faili lahti
for rida in f:
    sammude_list.append(rida.strip())#loob iga failis olevale reale listis indeksi koha
f.close()#paneb kinni faili
print(sammude_list)
#listi int failitüübiks tegemine
with open('sammud.txt') as f:
    sammude_list = [ int(i) for i in f ]
sammud_kokku = sum(sammude_list)
print(sammud_kokku)
print(sum(sammude_list)/len(sammude_list))#keskmine arvutamine
print(min(sammude_list))
print(max(sammude_list))
'''
#ÜL2f = open('sammud.txt')#teeb .txt faili lahti
from googletrans import *
trans = Translator
k2sud = []
f = open('sammud.txt')#teeb .txt faili lahti
for rida in f:
    k2sud.append(rida.strip())#loob iga failis olevale reale listis indeksi koha
f.close()#paneb kinni faili
det = trans.detect(k2sud)
t6lge = trans.translate(k2sud,dest=en)
print(t6lge)
