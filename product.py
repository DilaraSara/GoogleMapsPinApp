import folium
import numpy as np
import csv

def cember_koordinatlari(merkez, yaricap_km, nokta_sayisi):
    koordinatlar = []
    acilar = np.linspace(0, 2 * np.pi, nokta_sayisi)  # Eşit aralıklı açılar oluştur
    enlem_mesafe = yaricap_km / 111.32  # Enlem için mesafe
    boylam_mesafe = yaricap_km / (111.32 * np.cos(np.radians(merkez[0])))  # Boylam için mesafeyi düzelt

    for aci in acilar:
        enlem = merkez[0] + enlem_mesafe * np.cos(aci)  # Enlem hesapla
        boylam = merkez[1] + boylam_mesafe * np.sin(aci)  # Boylam hesapla
        koordinatlar.append((enlem, boylam))  # Koordinatı ekle
    
    return koordinatlar

center_coordinate = (38.67323964025944, 39.23889697792604) # Rastgele koordinatlar
r_km = 2  # Yarıçap
num_points = 500  # Nokta sayısı

points = cember_koordinatlari(center_coordinate, r_km, num_points)

baslik = "Atakum Belediyesi"

icerik = '''Tırnak Mantar Tedavisi: Tırnak mantarı, tırnağın kalınlaşmasına ve renk değişimine neden olan bir enfeksiyondur. Tedavisinde mantar önleyici kremler, ojeler ve oral ilaçlar kullanılır. Tedavi süresi uzundur ve tam iyileşme aylar alabilir.

Tırnak Batık Tedavisi: Tırnak batması, tırnağın deriye doğru büyüyerek ağrı ve enfeksiyona yol açtığı bir durumdur. Tedavi, tırnağın düzgün kesilmesi, antibiyotik kremler ve bazen cerrahi müdahaleyi içerir.

Nasır Tedavisi: Nasır, cildin basınç veya sürtünme nedeniyle kalınlaşması sonucu oluşur. Tedavisinde nasır bandı, nasır taşı veya ponza taşı kullanımı ve rahat ayakkabılar tercih edilmesi önerilir.

Harita: https://maps.app.goo.gl/X2aMszd8B1nEtwSv9

Web Sitesi: https://ayaksagligimerkezi.com/

Anahtar kelimeler;

Ayak mantar tedavisi
Tırnak mantar tedavisi
Tırnak Batık tedavisi
Batık tedavisi
Nasır tedavisi
'''

# CSV çıktısı oluştur
with open('coordinates.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['WKT', 'ad', 'açıklama'])  # Başlık satırını yaz

    for i, point in enumerate(points, start=1):
        wkt = f"POINT ({point[1]} {point[0]})"
        writer.writerow([wkt, f"{baslik}", f"{icerik}"])  # Koordinatları ve açıklamaları yaz

print("CSV dosyası başarıyla oluşturuldu.")