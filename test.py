import time

from ÇalmaListesi import *

print("""Çalma listesi programına hoşgeldiniz.

İşlemler:
1-)Şarkıları göster
2-)Şarkı sorgula
3-)Şarkı ekle
4-)Şarkı sil

Çıkmak için 'q' tuşuna basınız 

""")
Liste=Kütüphane()
while True:
    a=input("Bir işlem giriniz:")
    if a=="q":
        print("programdan çıkılıyor")
        break

    elif a == "1":
        Liste.şarkıları_göster()

    elif a=="2":
        isim=input("Sorgulamak istediğiniz şarkıyı girin:")
        print("Şarkı sorgulanıyor...")
        time.sleep(1)
        Liste.şarkı_sorgula(isim)

    elif a=="3":
        print("Eklemek istediğiniz şarkıyı giriniz:")
        yeni_şarkı=Şarkı(isim=input("İsim:"),sanatçı=input("Sanatçı"),süre=input("Süre:"))
        print("Şarkı ekleniyor")
        time.sleep(1)
        Liste.şarkı_ekle(yeni_şarkı)

    elif a=="4":
        isim=input("Silmek istediğiniz şarkının ismini giriniz:")
        a=input("Emin misiniz?(E/H)")
        if a=="E":
            print("şarkı siliniyor...")
            time.sleep(1)
            Liste.şarkı_sil(isim)
        else:
            continue
    else:
        print("Geçersiz işlem")