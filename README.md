# Sensorsuz-Konum-Hesaplama (Vision-Based Localization)
Bu proje, **harici konum sensörleri (GPS, LiDAR vb.) kullanılmadan**, yalnızca **kamera görüntüsü** üzerinden bir **hedef alanın konum ve mesafe bilgilerinin hesaplanmasını** amaçlamaktadır.
Çalışma, Teknofest sürecinde geliştirilmiş olup özellikle **İHA, otonom sistemler ve savunma/havacılık** uygulamaları için referans niteliği taşımaktadır.

## Projenin Amacı
- Kameranın **Field of View (FOV)** değerleri ve aracın mevcut **irtifa bilgisi** kullanılarak:
- Hedef alanın araçtan olan **yatay ve dikey mesafesinin** hesaplanması
- Hedef nesnenin **göreceli konumunun** tespit edilmesi
- Sensör bağımlılığını azaltarak **daha sade ve maliyeti düşük** bir konum çözümü sunulması hedeflenmiştir.

## Kullanılan Yöntem
- Tek kamera görüntüsü üzerinden görüntü işleme
- Kamera FOV geometrisi kullanılarak piksel–metre dönüşümü
- Bilinen irtifa bilgisi ile trigonometrik konum hesaplama
- Deneme–yanılma ve iteratif iyileştirme yaklaşımı

## Test Senaryosu
Geliştirilen algoritma, **26 metre irtifadan, 2.5 metre çapında** tanımlı bir hedef alan üzerinde test edilmiştir.
Her testte yatay ve dikey mesafe hesaplamaları ayrı ayrı analiz edilmiş ve hata oranları ölçülmüştür.

### Deneme -1-
<img width="500" height="700" alt="deneme1_1" src="https://github.com/user-attachments/assets/6c63f7a0-4dfc-4c1b-a29d-95ab76426040" />
<img width="500" height="700" alt="deneme1_2" src="https://github.com/user-attachments/assets/3a4cf0e5-5d5d-4720-a410-68247e5e54a6" />

### Sonuçlar -1-
<img width="1500" height="100" alt="sonuc1" src="https://github.com/user-attachments/assets/2526853f-a6d0-45d4-91c9-07a61db910d7" />
İlk test çalışmasında, **toplam hata payı 0.5 metrenin altında** elde edilmiştir.
Bu sonuç, sistemin temel geometrik yaklaşımının doğru çalıştığını göstermiş ve proje için güçlü bir başlangıç oluşturmuştur.

### Deneme -2-
<img width="500" height="700" alt="deneme2_1" src="https://github.com/user-attachments/assets/658155a2-d7fb-4f44-b0af-df961ec04694" />
<img width="500" height="700" alt="deneme2_2" src="https://github.com/user-attachments/assets/26479765-ebc7-47db-ae6d-e39f3a1b8427" />

### Sonuçlar -2-
<img width="1500" height="100" alt="sonuc2" src="https://github.com/user-attachments/assets/f1441b04-1d52-4b4e-9694-04160397fcec" />
İkinci denemede **dikey mesafe hesaplaması önemli ölçüde iyileştirilmiştir**.
Ancak yatay mesafe hesaplamasında yapılan varsayımlar nedeniyle önceki teste kıyasla yaklaşık %50 daha fazla hata oluşmuştur. Buna rağmen toplam hata oranında genel bir düşüş sağlanmıştır


### Deneme -3-
<img width="500" height="700" alt="deneme3_1" src="https://github.com/user-attachments/assets/ad4bb7bb-b758-423c-ba9e-78048e0a6914" />
<img width="500" height="700" alt="deneme3_2" src="https://github.com/user-attachments/assets/9f9ce436-4395-4ec4-bdc4-295d2b75ab12" />

### Sonuçlar -3-
<img width="1500" height="100" alt="sonuc3" src="https://github.com/user-attachments/assets/4acc1cc2-6b96-4a54-aac9-837edc8f61ef" />
Üçüncü iterasyonda yatay mesafe hesaplamasında önceki hata büyük ölçüde telafi edilmiş ve hata oranı yaklaşık %80 azaltılmıştır.
Bu iyileştirme yapılırken dikey mesafe hata oranında artış gözlemlenmiş olsa da, **maksimum hata 1 metrenin altında tutulmuştur**.

### Deneme -4-
<img width="500" height="700" alt="deneme4_1" src="https://github.com/user-attachments/assets/ffa8d623-d409-4c9b-8755-ea3dcd7649f5" />
<img width="500" height="700" alt="deneme4_2" src="https://github.com/user-attachments/assets/3b734ead-7e15-4801-abb4-f3415df6e08a" />


### Sonuçlar -4-
<img width="1500" height="100" alt="sonuc4" src="https://github.com/user-attachments/assets/4ca5c665-cd5b-4ca1-8481-5490492d12cd" /> 
Dördüncü ve son denemede yapılan optimizasyonlar sayesinde hem yatay hem dikey mesafe hesaplamalarında **toplam hata  0.5 metrenin altına** indirilmiştir.
Bu sonuç, algoritmanın sahaya uygulanabilirliğini ve kararlılığını göstermektedir.


## Projenin Öne Çıkan Kazanımları
- Sensörsüz (camera-only) konum hesaplama
- İteratif geliştirme ve hata analizi
- Gerçek saha testleriyle doğrulama
- İHA ve otonom sistemlere uyarlanabilir yapı
- **< 0.5 m hata payına** ulaşan konum doğruluğu

## Gelecek Çalışmalar

- Kamera kalibrasyonu ve lens distorsiyon düzeltmeleri
- Farklı irtifa ve FOV senaryolarında testler
- Gerçek zamanlı (real-time) entegrasyon
- Çoklu hedef tespiti desteği
