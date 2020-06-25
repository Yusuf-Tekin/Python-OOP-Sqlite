import sqlite3

class girisExam:


    connection = sqlite3.connect('database.db')
    if(connection):
        print('Bağlandı')

    else:
        print('Bağlanamadı')
    cursor = connection.cursor()

    def tablo_yarat(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username,password)")# IF NOT EXISTS DEMEK EĞER TABLO YOKSA OLUŞTUR DEMEK TERMİNALDE Kİ HATAYI YOK ETMEK MAKSAT

    def kullaniciEkle(self,username,password):
        adddata = self.cursor.execute("INSERT INTO users VALUES ('" + username + "','" +password + "')")
        if(adddata):
            print('Kayıt Başarılı')
            self.connection.commit()
        else:
            print('Kayıt Başarısız')

    def dataInput(self):
        Username = input('Username => ')
        Password = input('Password => ')
        self.kullaniciEkle(Username,Password)

    def girisKontrol(self,Username,Password):
        self.cursor.execute("SELECT * FROM users")
        data = self.cursor.fetchall()
        for i in data:
            if(i[0] == Username and i[1] ==Password):
                print('Hoşgeldin ' + i[0])
                newpass = input('Yeni Şifre Belirtin -> ')
                self.sifre_guncelle(i[0],newpass)
                break
            else:
                print('Hesap Bulunamadı')
    def sifre_guncelle(self,Username,newPassword):
        update = self.cursor.execute("UPDATE users SET password = '" +newPassword+ "' WHERE username = '" +Username+ "'")#ogranciler tablosunda nu'su 10090 olanlar 10000 olacak şekilde günceller
        if(update):
            self.connection.commit()
            print('Şifre Güncellendi')
        else:
            print('Şifre Güncelleme Hatası')

    def giris_yap(self):
        getUsername = input('Kullanıcı Adı: ')
        getPassword = input('Parola:')
        self.girisKontrol(getUsername,getPassword)

    def kullaniciSil(self):
        print('Hesabı Silebilmek için kullanıcı adı ve parola girin')
        username = input('Kullanıcı Adı : ')
        password = input('Şifre:')
        self.cursor.execute("SELECT * FROM users")
        data = self.cursor.fetchall()
        for i in data:
            if (i[0] == username and i[1] == password):
                self.hesapSil(i[0],i[1])
                break
            else:
                print('Hesap Bulunamadı')


    def hesapSil(self,Username,Password):
        print('Silinen Hesap Adı : ' + Username)
        print('Silinen Hesap Şifre : ' + Password)
        delete = self.cursor.execute('DELETE FROM users WHERE username =  "' +Username+ '"')
        self.connection.commit()
        if(delete):
            print('Hesabınız kalıcı olarak silindi. Tekrar Görüşmek Dileğiyle -> ' + Username)
        else:
            print('Hesabınız Silinemedi')

yeni = girisExam()
"""Kullanmak istediğin fonksiyon kodları..."""