from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


url = "https://www.instagram.com/"

def verileri_al(kullanici_adi):
    son_url = url + kullanici_adi

    request = Request(son_url, headers={'User-Agent':'Mozilla/5.0'})
    html_verisi = urlopen(request).read()


    soup = BeautifulSoup(html_verisi, 'html.parser')

    veri = soup.find("meta",property="og:description").attrs['content']
    veri = veri.split("-")[0]
    veri = veri.split(" ")
    
    print("Takipçi Sayısı: " +veri[0])
    print("Takip Edilen Sayısı: " +veri[2])
    print("Gönderi Sayısı: " +veri[4])



kullanici_adi = input("Mevcut Bir Kullanıcı Adı Giriniz: ")
verileri_al(kullanici_adi)


