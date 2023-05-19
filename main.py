import arsa
import daire
import otel
import villa
devam = "e"
while devam != "h" and devam != "H":
    yer = int(input("Fiyatını hesaplamak istediğiniz yerin numarasını giriniz\n1-Arsa\n2-Daire"
                    "\n3-Otel\n4-Villa\nYer = "))
    if yer == 1:
        secim = int(input("\nArsanızın bölgesinin numarasını giriniz"
                          "\n1-Deniz Kenarı\n2-Şehir Merkezi\n3-Kırsal\nBölge = "))
        while secim not in range(1, 4):  # geçerli aralıkta bir bölge girilmiş mi diye kontrol eden kısım
            secim = int(input("\nLütfen geçerli bir bölge numarası giriniz"
                              "\n1-Deniz Kenarı\n2-Şehir Merkezi\n3-Kırsal\nBölge = "))

        sekil = int(input("\nArsanızın şekil numarasını giriniz\n1-Dikdörtgen\n2-Çember\nŞekil = "))
        while sekil not in range(1, 3):  # geçerli aralıkta bir şekil girilmiş mi diye kontrol eden kısım
            sekil = int(input("\nLütfen geçerli bir şekil numarası giriniz"
                              "\n1-Dikdörtgen\n2-Çember\nŞekil = "))

        arsa.arsa_katsayi(secim)
        cevre = arsa.arsa_cevre(sekil)
        fiyat = arsa.arsa_fiyat(cevre)
        print(f"Arsanızın fiyatı {fiyat:.2f}TL'dir.")
        devam = input("\nDevam etmek için e/E çıkmak için h/H giriniz = ")
    elif yer == 2:
        secim = int(input("\nLütfen dairenizin kat yeri numarasını giriniz"
                          "\n1-Ara Kat\n2-Üst Kat\n3-Zemin Kat\nKat= "))
        while secim not in range(1, 4):  # geçerli aralıkta bir kat yeri girilmiş mi diye kontrol eden kısım
            secim = int(input("\nLütfen geçerli bir kat yeri numarasını giriniz"
                              "\n1-Ara Kat\n2-Üst Kat\n3-Zemin Kat\nKat= "))

        katsayi = daire.daire_katsayi(secim)
        alan = daire.daire_alan()
        fiyat = daire.daire_fiyat(alan, katsayi)
        print(f"Dairenizin fiyatı {fiyat:.2f}TL'dir.")
        devam = input("\nDevam etmek için e/E çıkmak için h/H giriniz = ")
    elif yer == 3:
        secim = int(input("\nLütfen otelinizin bulunduğu şehri seçiniz"
                          "\n1-Antalya\n2-Bodrum\n3-Çeşme\nŞehir= "))
        while secim not in range(1, 4):  # geçerli aralıkta bir şehir numarası girilmiş mi diye kontrol eden kısım
            secim = int(input("\nLütfen geçerli bir şehir numarası giriniz"
                              "\n1-Antalya\n2-Bodrum\n3-Çeşme\nŞehir= "))

        tur = int(input("\nOda türü numaranızı giriniz\n1-Kral dairesi\n2-Aile odası\n3-Tek kişilik oda\nTür = "))
        while tur not in range(1, 4):  # geçerli aralıkta bir tür numarası girilmiş mi diye kontrol eden kısım
            tur = int(input("\nLütfen geçerli bir tür numarası giriniz"
                            "\n1-Kral dairesi\n2-Aile odası\n3-Tek kişilik oda\nTür = "))

        otel.otel_katsayi(secim)
        oda_fiyati = otel.oda_fiyat(tur)
        otel_fiyati = otel.otel_fiyat(oda_fiyati)
        print(f"Otel Tatilinizin fiyatı {otel_fiyati:.2f}TL'dir.")
        devam = input("\nDevam etmek için e/E çıkmak için h/H giriniz = ")
    elif yer == 4:
        secim = int(input("\nLütfen villanızın bulunduğu şehri seçiniz"
                          "\n1-İstanbul\n2-Muğla\n3-İzmir\nŞehir= "))
        while secim not in range(1, 4):  # geçerli aralıkta bir şehir numarası girilmiş mi diye kontrol eden kısım
            secim = int(input("\nLütfen geçerli bir şehir numarası giriniz"
                              "\n1-İstanbul\n2-Muğla\n3-İzmir\nŞehir= "))

        kisi = int(input("\nVillada kaç kişi kalmayı planladığınızı girin = "))

        villa.villa_katsayi(secim)
        kisi_fiyati = villa.kisi_fiyat(kisi)
        villa_fiyati = villa.villa_fiyat(kisi_fiyati)
        print(f"Villa Tatilinizin fiyatı {villa_fiyati:.2f}TL'dir.")
        devam = input("\nDevam etmek için e/E çıkmak için h/H giriniz = ")
    else:
        print("Lütfen geçerli bir yer numarası giriniz.")
