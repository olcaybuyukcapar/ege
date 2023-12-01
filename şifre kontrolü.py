gizli_sifre = input("...")

girilen_deger = str(input("şifreyi giriniz... : "))
if girilen_deger == gizli_sifre:
    print("şifre doğru, giriş yapablirsiniz")
else:
    print("hatalı şifre girdiniz")
    print("şunu girdiniz: " + girilen_deger)