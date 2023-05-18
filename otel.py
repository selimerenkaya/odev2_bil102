def otel_katsayi(secim):
    global katsayi
    if secim == 1:
        katsayi = 2.4  # antalya
    elif secim == 2:
        katsayi = 1.6  # bodrum
    elif secim == 3:
        katsayi = 1.2  # çeşme


def oda_fiyat(turu):
    if turu == 1:  # kral dairesi
        kisi = input("Kaç kişi kalacağınızı girin = ")
        return 10000*kisi
    elif turu == 2:  # aile odası
        kisi = input("Kaç kişilik aile odası istediğinizi girin = ")
        if kisi <= 4:
            return 5000*kisi
        elif kisi > 4:
            return 8000*kisi
    elif turu == 3:  # tek kişilik oda
        return 3500


def otel_fiyat(oda_fiyati):
    return katsayi*oda_fiyati