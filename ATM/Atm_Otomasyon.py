import time
from datetime import datetime
now = datetime.now()
Kartsifresi = "1905"
MevcutBakiye = 3000
girisHakki = 3
print("YapıKredi Bankasına Hoşgeldiniz")
kartİslemi= True
İslemDurumu= True
while İslemDurumu:
    print("------------------------------")
    giris= input("Kart Şifrenizi Giriniz : ")
    if giris != Kartsifresi:
        print("Yanlış Şifre Girdiniz. Lütfen Tekrar Deneyiniz.. ")
        girisHakki -=1
        print(girisHakki,"deneme hakkınız kaldı.")
        if girisHakki == 0:
         print("Kartınız Bloke Olmuştur. En Yakın Bankaya Başvurun.")
         İslemDurumu=False
    else:
        print("Girişiniz Yapıldı.")
        print("""
        Yapmak İstediğiniz İşlemi Seçiniz: 
        ----------------------------------
        1 - Para Çekme
        2 - Para Yatırma 
        3 - Bakiye Öğrenme
        4 - Çıkış
        ----------------------------------
           """)
        while kartİslemi:
            print("-------------------------")
            secilenİslem = input("Yapmak İstediğiniz işlem : ")
            if secilenİslem == "1":
               cekilenPara =int(input("Çekilen Miktarı Giriniz: "))
               if cekilenPara > MevcutBakiye:
                print("Yetersiz Bakiye. 3'e Basarak Bakiyenizi Kontrol Ediniz")
               else:
                MevcutBakiye -= cekilenPara
                print("İşleminiz Gerçekleştiriliyor..")
                time.sleep(1.5)
                tarih = now.strftime("%d/%m/%Y  %H:%M:%S")
                print("İşlem tamamlandı.Güzel Günlerde Kullanın. ")
                print("İşlem Tarihi: ",tarih)
            elif secilenİslem == "2":
               yatırlacakPara = int(input("yatırılacak miktar: "))
               MevcutBakiye += yatırlacakPara
               print("İşleminiz Gerçekleştiriliyor..")
               time.sleep(1.5)
               tarih = now.strftime("%d/%m/%Y  %H:%M:%S")
               print("İşlem tamamlandı.Güzel Günlerde Kullanın. ")
               print("İşlem Tarihi: ",tarih)
              
            elif secilenİslem=="3":
               print("güncel bakiyeniz : ",MevcutBakiye,"₺")
            else:
               print("Çıkış yapılıyor... ")
               time.sleep(1.5)
               print("Çıkış Yapıldı. Bizi tercih ettiğiniz için teşekkür Ederiz.")
               İslemDurumu=False
               kartİslemi =False

           
            
               