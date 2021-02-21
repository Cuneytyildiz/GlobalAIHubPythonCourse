"""
Recipe Application
Enter 3 recipes. Create a separate class for each recipe.
Identify the products used in this recipe using the init () method.
Write a function about how long these products should be used later.
Do not forget to use inheritance here. Here to use inheritance;
For example;
Write a cooking function. Since this method will be common to all
classes, you need to use inheritance here.

"""

class Yemek():

    def __init__(self,yemekAdi,yag,tuz,pSure):
        self.yemekAdi = yemekAdi
        self.yag = yag
        self.tuz = tuz
        self.pSure = pSure
    
    def ekle(self,malzeme):
        print(f"{malzeme} eklenir.")
    
    def pisir(self):
        print(f"{self.yemekAdi} {self.pSure} dakika pişirilir.")
    
    def karistir(self):
        print(f"{self.yemekAdi} karıştırılır")
    
    def kaynat(self,malzeme):
        print(f"{malzeme} kaynatılır.")
    
    def dilimle(self,malzeme):
        print(f"{malzeme} dilimlenir.")
    
    def kizart(self,malzeme):
        print(f"{malzeme} {self.pSure} dakika kızartılır.")
    
class Makarna(Yemek):

    def __init__(self,yemekAdi,yag,tuz,pSure,makarna,su):
        super().__init__(yemekAdi,yag,tuz,pSure)
        self.makarna = makarna
        self.su = su

class PatatesKızartmasi(Yemek):

    def __init__(self,yemekAdi,yag,tuz,pSure,patates):
        super().__init__(yemekAdi,yag,tuz,pSure)
        self.patates = patates
    def soy(self):
        print(f"{self.patates} kabuğu soyulur.")

class Menemen(Yemek):

    def __init__(self,yemekAdi,yag,tuz,pSure,yumurta,domates,biber):
        super().__init__(yemekAdi,yag,tuz,pSure)
        self.yumurta = yumurta
        self.domates = domates
        self.biber = biber   

while True:
    print("-------Yemek Tarifleri-----:")
    print("1-Makarna")
    print("2-Patates Kızartması")
    print("3-Menemen")
    while True:
        secim=int(input("Hangi Tarifi Öğrenmek İstiyorsunuz: "))
        if(secim<=0 or secim>3):
            print("Hatalı Seçim !!!\n")
        else:
            break
    
    if(secim==1):
        print("-----Makarna Tarifi-----")
        yemek = Makarna("Makarna","1 tatlı kaşığı yağ","1 tatlı kaşığı tuz","10-15","1 paket makarna","1 litre su")
        yemek.ekle(yemek.su)
        yemek.kaynat(yemek.su)
        yemek.ekle(yemek.tuz)
        yemek.ekle(yemek.yag)
        yemek.ekle(yemek.makarna)
        yemek.pisir()
        print("Afiyet Olsun...\n")
        break
    
    elif(secim == 2):
        print("-----Patates Kızartması Tarifi-----")
        yemek = PatatesKızartmasi("Patates Kızartması","2 bardak yağ","1/2 çay kaşığı tuz","10","4 adet patates")
        yemek.ekle(yemek.patates)
        yemek.soy()
        yemek.dilimle(yemek.patates)
        yemek.ekle(yemek.yag)
        yemek.kizart(yemek.patates)
        yemek.ekle(yemek.tuz)
        print("Afiyet Olsun...\n")
        break
    
    elif(secim == 3):
        print("-----Menemen Tarifi-----\n")
        yemek = Menemen("Menemen","2 yemek kaşığı yağ","1/2 çay kaşığı tuz","10","3 adet yumurta","3 adet domates","3 adet biber")
        yemek.ekle(yemek.yag)
        yemek.ekle(yemek.biber)
        yemek.kizart(yemek.biber)
        yemek.dilimle(yemek.domates)
        yemek.ekle(yemek.domates)
        yemek.ekle(yemek.tuz)
        yemek.pisir()
        yemek.ekle(yemek.yumurta)
        print("Afiyet Olsun...\n")
        break


        





      


