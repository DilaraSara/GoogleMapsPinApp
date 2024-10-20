import folium
import numpy as np

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


def harita_olustur(merkez, noktalar):  # Haritayı başlat
    harita = folium.Map(location=merkez, zoom_start=15)

    # Her bir nokta için pin ekle
    for nokta in noktalar:
        folium.CircleMarker(location=nokta, radius=2, color='red').add_to(harita)

    return harita


center_coordinate = (38.67323964025944, 39.23889697792604) # Rastgele koordinatlar
r_km = 1  # Yarıçap
num_points = 500  # Nokta sayısı

points = cember_koordinatlari(center_coordinate, r_km, num_points)
map_object = harita_olustur(center_coordinate, points)

# Haritayı kaydet
map_object.save("/Users/dilarasara/Desktop/python_ödev/harita_duzeltilmis.html")

def list_coordinates_yedek(points):
    for point in points:
        print(f" ({point[0]}, {point[1]})")  # Noktaları doğru şekilde listele

def list_coordinates(points):
    for point in points:
        print(f"\"POINT ({point[1]} {point[0]})\",Nokta 1,")  # Noktaları doğru şekilde listele

list_coordinates(points)

# Developer Maaşları Python, Php, Java -> Yurtiçinde ve Yurtdışında Ayrıca Çalışma Şartları
# İnternet Nasıl Çalışır Videosu
## Domain Hosting Nasıl Çalışır, Django Nasıl Deploy Edilir.
# Parola İle Şifre Arasındaki Fark
# Yapay Zekayı Yazılımda Nasıl Kullanabilirsin

# Github Developer Student Pack ***



'''Bu sorunun temel nedeni, coğrafi koordinat sisteminde enlemin ve boylamın farklı ölçeklerde olmasıdır. 
Dünya küre şeklinde olduğundan, 1 derece enlem her zaman yaklaşık 111.32 km’ye karşılık gelir, ancak boylam için bu mesafe enleme bağlı olarak değişir.

Ekvatora yakın yerlerde 1 derece boylam yaklaşık 111.32 km'ye eşittir.
Ancak, kutuplara yaklaştıkça, 1 derece boylamın karşılık geldiği mesafe küçülür ve enleminiz arttıkça bu mesafe azalır.
Bu yüzden, merkez koordinatlarınız (örneğin, enlem 41.32) ile hesap yaptığınızda, 
boylam doğrultusundaki mesafe enlem doğrultusundaki mesafeden farklı olacaktır ve bu da bir daire yerine elips benzeri bir şekil oluşmasına neden olur.

Bu durumu düzeltmek için boylam doğrultusundaki mesafeyi enlem konumunuza göre düzeltebilirsiniz.
boylam doğrultusundaki mesafe enlem ile düzeltildiği için artık bir daire şekli oluşturmanız mümkün olacak. 
Bu düzeltme, boylamların enleme göre farklı mesafelere karşılık gelmesinden kaynaklanan elips etkisini ortadan kaldıracaktır.

'''