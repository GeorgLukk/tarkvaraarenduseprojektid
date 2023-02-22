#name = input("Sisesta nimi: ")
#clr = input("Sisesta värv: ")
class fruit:
    def __init__(self):#antud funktsioon küsib nime ja värvi
        self.name = name #self.name = name
        self.colour = clr #self.color = clr
    def details(self) -> apple: #teeb funksiooni õunale mis väljastab
        print ("my " + self.name +
               " is " + self.colour)#väljastab selle funksioooni
apple = fruit ("apple", "red")#annab õunale vajalikud detailid
apple.details()#prindib objektile antud detailid
'''
class fruit:
    def __init__(self, clr):
        self.colour = clr
apple = fruit("red")
banana = fruit("yellow")

class fruit:
    def __init__(self, name, clr):
        self.name = name
        self.colour = clr
    def details(self):
        exp_date = " 07.02.2022"
        print("expires on" + exp_date)
apple = fruit("apple", "red")
apple.details()
'''
