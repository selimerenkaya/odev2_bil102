def arsa_katsayi(secim):
    global katsayi
    if secim == 1:
        katsayi = 1.6  # deniz_kenar
    elif secim == 2:
        katsayi = 1.2  # sehir_merkez
    elif secim == 3:
        katsayi = 0.8  # kirsal


def arsa_cevre(sekil):
    if sekil == 1:  # dikdörtgen
        uzun_kenar = float(input("\nArsanızın uzun kenarının uzunluğunu giriniz = "))
        kisa_kenar = float(input("Arsanızın kısa kenarının uzunluğunu giriniz = "))
        return (kisa_kenar+uzun_kenar)*2
    elif sekil == 2:  # çember
        pi = 3.14
        yaricap = float(input("\nArsanızın yarıçapını giriniz = "))
        return pi*yaricap*2


def arsa_fiyat(arsa_cevresi):
    return katsayi*arsa_cevresi*1000