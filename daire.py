def daire_katsayi(secim):
    ara_kat = 2
    ust_kat = 1.6
    zemin_kat = 0.9
    if secim == 1:
        katsayi = ara_kat
    elif secim == 2:
        katsayi = ust_kat
    elif secim == 3:
        katsayi = zemin_kat
    return katsayi


def daire_alan():
    uzun_kenar = float(input("\nDairenizin uzun kenarının uzunluğunu giriniz = "))
    kisa_kenar = float(input("Dairenizin kısa kenarının uzunluğunu giriniz = "))
    return kisa_kenar*uzun_kenar


def daire_fiyat(alan, katsayi):
    return katsayi*alan*5000