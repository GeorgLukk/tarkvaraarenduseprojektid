#1
a = 1
b = "a\n"
while a<3:#tsükkel mis käib niikaua kui aon väiksem kui 3
    print (b)
    a+=1 #lisab a'le 1
#2
b= "'Tere!'"
c= '"Head aega!"'
print (b)#väljastab b
print("\n") #loob vahe
print(c)#väljastab c
#3
a= "Tere"
b= "Tore"
lause = a*3+"\\" + b #korrutab a'd 3 korda lisab 2 \ märki millelt üks kaob ning b
#\\ see jagab \ \'ga ning sellepärast jääbgi näha 1 \ märk
print(lause) #väljastab eelnevalt loodud lause
#4
nimi="loomariik"
print(nimi[0]+nimi[-1])#prindib esimese ja viimase tähe kuna 0 on esimene indeks ja -1 hakatakse tagand poolt lugema
#5
nimi1="Paide"
nimi2="Türi"
print("Tere,"[0],nimi1[-5],nimi2,"!")#väljastab T P türi kuna Tere 0 indeks + Paide -5 indeks ning nimi2
#6
a="A"
b=1
while b<3:#tsükkel mis kestab niikaua kui b on väiksem kui b
    print(a,end=" ")#tühik tuleb lõppu mitte vahele ehk end mis viib tühiku Lõppu
    b+=1
#7
a=10
b=2
print(a>b)#kui küsitakse <,>,= siis antakse vastuseks kas True või False
#8
a=10
b=2
print(a!= b and b>10)#prindib viimase kui on and
print(b== a or a>=0)#prindib True
#9
from tkinter import *
#loob raami
raam = Tk()
#annab raamile nime
raam.title("Tühi tahvel")
#loob tahvli raami sisse
tahvel = Canvas(raam, width=600)
#loob ristküliku tahvli piiridesse
tahvel.create_rectangle(50,70,100,100, width=2, outline="blue")#50 alguspunkt 70 on 2 punkt 100 3 punkt
#kirjutab Tere 50,50 koordinaatidele
tahvel.create_text(50,50, text="Tere!")
#teeb hylknurga mille külgede pikkused on need numbrid
tahvel.create_polygon(100,100,150,150,200,100, fill="red" ,outline="black")
#fill ehk täidab antud värviga
#outline on välimine joon
tahvel.pack()
#organiseerib need eelnevad kujuneid enne kui lisab need canvasele
raam.mainloop()
#loob tsükli et need kujundid ilmuksid