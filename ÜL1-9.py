'''
#ÜL1
a=1#defineerib a oleks 1
b="a\n"#ütleb et kui pridnidtakse b siis tuleb a ning valib järgmise rea
while a<3:#alustab while tsükli mis vaatab kas a<3
    print(b)#prindib b
    a+=1#liidab a'le 1 juurde
'''
'''
#ÜL2
b="'Tere!'"#annab b'le "'Tere!'" ning kui prinditakse see siis '' jäävad sinna kuna see oli defeineeritud juba stingina
c='"head aega!"'
#printimine
print(b)
print("\n")#teeb 2 vahet kuna alustab juba 2 realt ning järab 3nda rea vahele
print(c)#alustab 4 realt
'''
'''
#ÜL3
#defineerib a ja b
a="Tere"
b="Tore"
lause = a * 3 + "\\" + b#Korrutab a 3ga ehk väljastab seda 3 korda
print(lause)#väljastab lause
'''
'''
#ÜL4
#defineerib nime
nimi="loomariik"
print(nimi[0]+nimi[-1])#väljastab esimese indeksi all oleva täha ja -1 indeksiall oleva tähe ning liidab need
'''
#ÜL5
nimi1="Paide"
nimi2="Türi"
print("Tere,"[0],nimi1[-5],nimi2,"!")
#võtab tere'st 0 indeksi alt tähe ning väljastab selle
#