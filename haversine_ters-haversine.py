from math import radians, sin, cos, sqrt, atan2,asin,tan,degrees

def ters_haversine(lat1,lon1,lon_u,lat_u):
    R = 6378.0
    c = lon_u/(R*1000)
    a = tan(c/2)**2 / (1 + tan(c/2)**2)
    dlon = 2*asin(sqrt(a/((cos(radians(lat1))**2))))
    R = 6378.0
    c = lat_u/(R*1000)
    a = tan(c/2)**2 / (1 + tan(c/2)**2)
    dlat = 2*asin(sqrt(a))
    #dlat = asin(sqrt(a))*2
    #print("dlon=",dlon,"dlat=",dlat)
    
    dlon = dlon*-1 if lon_u < 0 else dlon
    dlat = dlat*-1 if lat_u < 0 else dlat
    lon2 = radians(lon1)+dlon
    lat2 = radians(lat1)+dlat
    return degrees(lat2),degrees(lon2)
    
    


def haversine(lat1, lon1, lat2, lon2):
    # Radyan cinsinden koordinatları al
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    # Haversine formülü
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    # Dünya yarıçapı km (ortalama)
    R = 6378.0
    # Gerçek uzaklık hesaplama
    distance = R * c * 1000  # Metre cinsinden
    return distance
    
# Örnek kullanım
lat1, lon1 = 40.1876005 , 29.12816450  # New York'un koordinatları
lat2, lon2 = 40.1878083,  29.12820295  # Los Angeles'in koordinatları

mesafe_metre = haversine(lat1, lon1, lat2, lon2)
yatay_metre = haversine(lat1, lon1, lat2, lon1)
dikey_metre = haversine(lat1, lon1, lat1, lon2)
print(f"1-2 Iki konum arasi gercek uzaklik: {mesafe_metre:.2f} metre")
print(f"Iki konum dikey gercek uzaklik: {dikey_metre:.2f} metre")
print(f"Iki konum yatay gercek uzaklik: {yatay_metre:.2f} metre")

lat3,lon3 = ters_haversine(lat1,lon1,dikey_metre,yatay_metre)
mesafe_metre = haversine(lat1, lon1, lat3, lon3)
yatay_metre = haversine(lat1, lon1, lat3, lon1)
dikey_metre = haversine(lat1, lon1, lat1, lon3)
print(f"1-3 Iki konum arasi gercek uzaklik: {mesafe_metre:.2f} metre")
print(f"Iki konum dikey gercek uzaklik: {dikey_metre:.2f} metre")
print(f"Iki konum yatay gercek uzaklik: {yatay_metre:.2f} metre")

mesafe_metre = haversine(lat3, lon3, lat2, lon2)
yatay_metre = haversine(lat3, lon3, lat2, lon3)
dikey_metre = haversine(lat3, lon3, lat3, lon2)
#ters_haversine(lat1,lon1,yatay_metre,dikey_metre)
print(f"2-3 Iki konum arasi gercek uzaklik: {mesafe_metre:.2f} metre")
print(f"Iki konum dikey gercek uzaklik: {dikey_metre:.2f} metre")
print(f"Iki konum yatay gercek uzaklik: {yatay_metre:.2f} metre")

print("-----------------------"*5)
print(lat2,lon2)
print(lat3,lon3)
#print("sonuc=",sonuc)
#print("konum=",lat2,lon2)
#sonuc = sqrt(pow(dikey_metre,2)+pow(yatay_metre,2))

