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
'''
#ÜL5
nimi1="Paide"
nimi2="Türi"
print("Tere,"[0],nimi1[-5],nimi2,"!")
#võtab tere'st 0 indeksi alt tähe ning väljastab selle
#Siis võtab nimi1'st indeks -5 alt tähe ning väljastab selle
#siis võtab nime2 ja väljastab selle
'''
'''
#ÜL6
a = "A"
b = 1
while b < 3:#tsükkel mis kestab niikaua kui b on võiksem kui kolm
    print(a,end=" ")#prindib a("A") ning teeb nii et see prindiks selle kõevale
    b += 1#liidab b'le 1 juurde
'''
'''
#ÜL7
a = 10
b = 2
print(a>b)#põhimõtteliselt küsib kas see on õige või vale
'''
'''
#ÜL8
a = 10
b = 2
print(a != b and b > 10)#prindib esimese
print(b == a or a >= 0)#prindib ainult true
'''
'''
#ÜL9
from tkinter import *#impordib terve tkinter 
#akna loomine
raam = Tk()
raam.title("Tühi tahvel")
tahvel = Canvas(raam,width=600)

#Teksti, ristküliku ning kolmnurga* joonitamine
tahvel.create_rectangle(50,70,100,100, width=2, outline="blue")
#tahvel(aknale antud nimi).create_rectange(loob ristküliku)(määrab nurkade asukohad ning outline paksuse ja värvi)
tahvel.create_text(50,50, text="Tere!")
tahvel.create_polygon(100,100,150,150,200,100, fill="red",outline="black")

#akna säilitamine
tahvel.pack()#organiseerib eelnevalt tehtud koodid enne kui paneb need tööle
raam.mainloop()#loopib selle koodi et see aken kinni ei läheks
'''