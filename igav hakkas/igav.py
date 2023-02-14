#sorteerib 2 erinevat faili
n1 = []
n2 = []
#võtab teise faili lahti ning loeb selle ja lisab selle n1 järjendisse
f = open('nimed 1')#teeb .txt faili lahti
for rida in f:
    n1.append(rida.strip())  #hakatakse faili lugema iga rida
f.close()#suleb faili
#võtab teise faili lahti ning loeb selle ja lisab selle n2 järjendisse
fe = open('nimed 2')  #teeb .txt faili lahti
for rida in fe:
    n2.append(rida.strip())  #hakatakse faili lugema iga rida
fe.close()#suleb faili
print(sorted(n1+n2))#sorteerib need(tähestiku järjekorda) ning väljastab sorteeritud andmed

print(sorted(n1+n2, key=len))#sorteerib need pikkuse järjekorda