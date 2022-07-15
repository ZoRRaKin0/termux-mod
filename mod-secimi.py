#coded by ZoRRaKin

import os
import time
os.system ('figlet ACHERON MOD SECİMİ')
print("""
1.)HACKER MOD
2.)CODER MOD
3.)FUNNY MOD
4.)CIKIŞ
""")
mod_secimi = str(input("HANGİ MODU KULLANACAKSINIZ : "))
os.system('clear')
if mod_secimi=="1":
    print("HACKER MOD DEVREYE GİRİYOR")
    time.sleep(1.2)
    os.system('clear')
    print ("""
    1.)OTO SQLMAP
    2.)OSİNT
    3.)SİTE BİLGİ TOPLAMA
    4.)DDOS
    5.)İP BİLGİ TOPLAMA
    """)
    hacker_mod_secimi = str(input("HANGİ PAKETİ KULLANACAKSINIZ :"))
    if hacker_mod_secimi=="1":
        print("İSTEGİNİZ DEVREDE")
        os.system('cd oto-sqlmapp')
        os.system('ls')
        os.system('python oto-sqlmap.py')
    else:
        if hacker_mod_secimi=="2":
            print("İSTEGİNİZ DEVREDE")
            os.system('cd osi.ig')
            os.system('ls')
            os.system('pip install -r requirements.txt')
            username=str(input("ARANACAK KULLANICI ADINI GIRINIZ : "))
            print("python main.py -u",username)
            print("KOMUTUNU YAZINCA CALISACAKTIR")
        else:
            if hacker_mod_secim =="3":
                print("İSTEGİNİZ DEVREDE")
                os.system('cd RED_HAWK')
                os.system('cd nikto ')
                os.system('cd wpbf')
            else:
                if hacker_mod_secim =="4":
                    print("İSTEGİNİZ DEVREDE")
                    os.system('cd hammer')
                    site_ip_bilgisi=str(input("SİTE İP GİRİNİZ :"))
                    print("python hammer.py -s "site_ip_bilgisi "-t 135")
                    print("KOMUTUNU YAZINCA CALISACAKTIR")
                else:
                    if hacker_mod_secim=="5":
                        print("İSTEGİNİZ DEVREDE")
                        os.system('cd İPGeoLocation')
                        os.system('pip install colorama')
                        os.system('pip install termcolor')
                        ip_bilgisi=str(input("İP ADRESİNİ GİRİNİZ"))
                        print("pip install termcolor",ip_bilgisi)
                        print("KOMUTUNU YAZINCA CALISACAKTIR")   
else:
    if mod_secimi=="2":
        print("CODER MOD DEVREYE GİRİYOR")
        os.system('nano')
    else:
        if mod_secimi=="3"
            print("FUNNY MOD DEVREYE GİRİYOR")
            time.sleep(1.2)
            os.system('clear')
            print("""
            1.)TERMUX'U YAKARIM
            2.)TREN YOLCULUGUNA CIKARIRIM
            3.)DAGLARA İSTEDİGİNİ YAZARIM
            4.)MATRİX YAPARIM BURALARI
                    """)
            funny_mod_secimi = str(input("HANGİ PAKET DEVREYE SOKULSUN : "))
            if funny_mod_secimi=="1":
                print("İSTEGİNİZ DEVREDE...")
                os.system('cacafire')
            else:
                if funny_mod_secimi=="2":
                    print('İSTEGİNİZ DEVREDE...')
                    os.system('sl')
                else:
                    if funny_mod_secimi=="3":
                        print("İSTEGİNİZ DEVREDE")
                        istek=str(input("NE YAZIYIM DAYI"))
                        print("figlet",istek)
                        print("bu komutu yazınız calısacakır")
                    else:
                        if funny_mod_secimi=="4":
                            print("İSTEGİNİZ DEVREDE")
                            os.system('cmatrix')
                        else:
                            print("HATALI SECIM YAPTINIZ")
                        
        else:
            if mod_secimi=="4":
                print ("CIKIS YAPILIYOR. İYİ GÜNLER")
                os.system('exit')
            else:
                prinnt("HATALI SECIM YAPTINIZ PROGRAM KAPANIYOR İYİ GÜNLER :)")
                os.system('exit')
