class cal():#teeb kalkulaatori klassi
    def __init__(self,a,b):#küsib selle funksiooni käest a'd ja b'd
        self.a=a
        self.b=b
    def liida(self):#Teeb funksiooni liitmine
            return self.a + self.b #teeb a+b
    def lahuta(self):#Teeb funksiooni lahutamine
            return self.a - self.b #teeb a-b
    def korruta(self):#Teeb funksiooni korrutamine
            return self.a * self.b #teeb a*b
    def jaga(self):#Teeb funksiooni jagamine
            return self.a / self.b #teeb a / b
    def astendamine(self):#Teeb funksiooni astendamine
            return self.a ** self.b #teeb a**b
    def jaak(self):#Teeb funksiooni jäägi leidmine
            return self.a // self.b #teeb a//b
a = int(input("Sisesta esimene arv: "))#küsib esimest arvu
b = int(input("Sisesta teine arv: "))#küsib teist arvu
obj=cal(a,b)#

while True:
    def menu():#teem menüü funksiooni
        x=('1. Liida \n2. Lahuta \n3. Korruta \n4. Jaga \n5. Ruutjuur\n6. jääk')#annab valikud
        print (x)#prindib eelneva rea
    menu()
    choice=int(input('vali millist tehet tahad teha: '))#saad valida eelnevalt prinditud realt millist arvutamist tahad teha
    if choice == 1:#kui valisid 1 siis annan se selle funksiooni
        print("Result: ",obj.liida())
    elif choice == 2:#kui valisid 2 siis annan see selle funksiooni
        print("Vastus: ",obj.lahuta())
    elif choice == 3:#kui valisid 3 siis annan see selle funksiooni
        print("Vastus: ",obj.korruta())
    elif choice == 4:#kui valisid 4 siis annan see selle funksiooni
        print("Vastus: ",obj.jaga())
    elif choice == 5:#kui valisid 5 siis annan see selle funksiooni
        print("Vastus: ", obj.astendamine())
    elif choice == 6:#kui valisid 6 siis annan see selle funksiooni
        print("Vastus: ", obj.jaak())
    elif choice == 0:#kui valisid 0 siis annan see selle funksiooni
        print("Vali üks neist")
        break
    else:#kui ei valinud ühtegi neist siis annab see "vale valik"
        print("Vale valik")
        break
quit()#lõpetab funksiooni
