import sqlite3
import time

class Şarkı():
    def __init__(self,isim,sanatçı,süre):
        self.isim=isim
        self.sanatçı=sanatçı
        self.süre=süre

    def __str__(self):
        return "İsim: {}\nSanatçı: {}\nSüre: {}".format(self.isim,self.sanatçı,self.süre)

class Kütüphane():

    def __init__(self):
        self.bağlantı_oluştur()

    def bağlantı_oluştur(self):
        self.bağlantı=sqlite3.connect("Kütüphane.db")
        self.cursor=self.bağlantı.cursor()
        sorgu="Create Table If not exists Şarkılar (İsim TEXT, Sanatçı TEXT, Süre INT)"
        self.cursor.execute(sorgu)
        self.bağlantı.commit()

    def bağlantıyı_kes(self):
        self.bağlantı.close()

    def şarkıları_göster(self):
        sorgu="Select * from Şarkılar"
        self.cursor.execute(sorgu)
        şarkılar=self.cursor.fetchall()
        if (len(şarkılar) == 0):
            print("Kütüphanenizde hiçbir şarkı yok")
        else:
            for i in şarkılar:
                şarkı=Şarkı(i[0],i[1],i[2])
                print(şarkı)

    def şarkı_sorgula(self,isim):
        sorgu="Select * from Şarkılar where İsim = ?"
        self.cursor.execute(sorgu,(isim,))
        şarkılar = self.cursor.fetchall()
        if (len(şarkılar)==0):
            print("Şarkı bulunamadı")
        else:
            şarkı=Şarkı(şarkılar[0][0],şarkılar[0][1],şarkılar[0][2])
            print(şarkı)

    def şarkı_ekle(self,şarkı):
        sorgu="Insert into Şarkılar Values(?,?,?)"
        self.cursor.execute(sorgu,(şarkı.isim,şarkı.sanatçı,şarkı.süre))
        self.bağlantı.commit()

    def şarkı_sil(self,isim):
        sorgu = "Delete from Şarkılar where İsim=?"
        self.cursor.execute(sorgu,(isim,))
        self.bağlantı.commit()