import arsa
import daire
devam = "e"
while devam != "h" and devam != "H":
    yer = int(input("Fiyatını hesaplamak istediğiniz yerin numarasını giriniz\n1-Arsa\n2-Daire\nYer = "))
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
        fiyat = daire.daire_fiyat(alan,katsayi)
        print(f"Dairenizin fiyatı {fiyat:.2f}TL'dir.")
        devam = input("\nDevam etmek için e/E çıkmak için h/H giriniz = ")
    else:
        print("Lütfen geçerli bir yer numarası giriniz.")