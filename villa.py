def villa_katsayi(secim):
    global katsayi
    if secim == 1:
        katsayi = 3.2  # istanbul
    elif secim == 2:
        katsayi = 2.6  # muğla
    elif secim == 3:
        katsayi = 1.8  # izmir


def kisi_fiyat(kisi):
    if kisi > 5:
        return kisi*4500
    elif kisi <= 4:
        return kisi*3500


def villa_fiyat(kisi_fiyati):
    return katsayi*kisi_fiyati
