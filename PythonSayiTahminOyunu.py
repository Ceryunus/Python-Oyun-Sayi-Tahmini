import random


class Oyun():

    def __init__(self, arasinda):
        self.arasinda = arasinda

    def sayiuretici(self):
        self.cevap = random.randrange(1, self.arasinda)  # 1iel 100 arası random bir sayı ürettim
        # print(random.randrange(1, 101))

    def kucukBuyuk(self):
        if self.a < self.cevap:
            print(f"Cevap {self.a}'sayısından daha büyüktür. ")
        else:
            print(f"Cevap {self.a}'sayısından daha küçüktür. ")

    def tamBolunme(self):
        if self.cevap % self.a == 0:
            print(f"{self.a} sayısına cevap tam bölünür")
        else:
            print(f"{self.a} sayısına cevap tam bölümez")

    def nekadarUzaklik(self):
        if self.cevap - self.a < 30 or self.cevap - self.a > 30:
            print(f"{self.a} sayısı ,cevaba 30 birimden daha yakındır")
        else:
            print(f"{self.a} sayısı ,cevaba 30 birim uzaklığından daha uzaktır")

    def randomFunctionSelection(self):
        self.mylist = [self.nekadarUzaklik, self.tamBolunme, self.kucukBuyuk]
        return random.choice(self.mylist)

    def puanlama(self):

        if self.hatasayisi == 0:
            self.hatasayisi += 1
            toplamhatasayisi = 0
            self.toplamhatasayisi = toplamhatasayisi
            self.puan = 100
            return self.puan
        elif self.hatasayisi < 10:
            self.puan -= 10
            self.toplamhatasayisi += 1
            return self.puan

    def resault(self):
        if self.puan > 90:
            print("Helal len , sen bu işi başarmışsın")
        elif self.puan > 70:
            print("Fena sayılmazsın hee")
        elif self.puan > 50:
            print("Gelişmen lazım ehe")
        elif self.puan > 30:
            print("Baya kötüsün :/")
        elif self.puan > 10:
            print("Kötünün kötüsü olurmu yavvv ")
            print(self.cevap)
        else:
            print("BAŞARAMADIN")
            print(self.cevap)

    def cevapver(self):
        s1.sayiuretici()
        self.hatasayisi = 0
        while True:
            a = int(input("Tahmininizi giriniz"))
            self.a = a

            if self.a != self.cevap:
                print(f"Kalan Puanınız {self.puanlama()}")
                self.randomFunctionSelection()()
                print(f"Kalan haklar : {10 - self.toplamhatasayisi}")

            elif self.a == self.cevap:
                self.puanlama()
                self.resault()
                print(f"dogru. Cevap {self.cevap}")
                break

            if self.toplamhatasayisi >= 10:
                self.resault()
                print(f"Cevap {self.cevap}")
                break


s = int(input("Oyun 1 ila kaç arasında olsun"))
s1 = Oyun(s)
s1.cevapver()
