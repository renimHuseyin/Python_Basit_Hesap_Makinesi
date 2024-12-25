def toplama():
    sayi_1 = int(input("Birinci Sayiyi Gir:"))
    sayi_2 = int(input("İkinci Sayiyi Gir: "))

    Toplam = sayi_1 + sayi_2
    print(f"Toplam: {Toplam}")

def cikarma():
    sayi_1 = int(input("Birinci Sayiyi Gir:"))
    sayi_2 = int(input("İkinci Sayiyi Gir: "))

    Toplam = sayi_1 - sayi_2
    print(f"Toplam: {Toplam}")

def carpmma():
    sayi_1 = int(input("Birinci Sayiyi Gir:"))
    sayi_2 = int(input("İkinci Sayiyi Gir: "))

    Toplam = sayi_1 * sayi_2
    print(f"Toplam: {Toplam}")

def bolme():
    sayi_1 = int(input("Birinci Sayiyi Gir:"))
    sayi_2 = int(input("İkinci Sayiyi Gir: "))

    Toplam = sayi_1 / sayi_2
    print(f"Toplam: {Toplam}")

print("HESAP MAKİNESİ\n")

islem = input("Yapmak İstediğiniz İşlemi Giriniz (toplam): (toplam, cikarma, bolme, carpma)\n")
if islem == "toplam":
    toplama()

if islem == "cikarma":
    cikarma()

if islem == "carpma":
    carpmma()

if islem == "bolme":
    bolme()