import math
import numpy as np
import cv2
import  time

def ters_haversine(lon_u,lat_u,yön):
    heading  = 1
    lat1 = 40.1876005 #yan
    lon1 = 29.1281645 #dikey
    R = 6371.0
    c = lon_u/(R*1000)
    a = math.tan(c/2)**2 / (1 + math.tan(c/2)**2)
    dlon = math.asin(2*math.sqrt(a/((math.cos(math.radians(lat1))**2))))
    dlat = math.asin(math.sqrt(a))*2
    
    dlon = dlon*-1 if lon_u < 0 else dlon
    dlat = dlat*-1 if lat_u < 0 else dlat
    if 0 < heading < 90:
        lon2 = math.radians(lon1)+dlon
        lat2 = math.radians(lat1)+dlat
    elif 90 < heading < 180:
        lon2 = math.radians(lon1)+dlon
        lat2 = math.radians(lat1)+dlat
    elif 180 < heading < 270:
        lon2 = math.radians(lon1)+dlon
        lat2 = math.radians(lat1)-dlat
    elif 270 < heading :
        lon2 = math.radians(lon1)-dlon
        lat2 = math.radians(lat1)-dlat
    elif heading == 0 :
        if yön > 0:
            lon2 = math.radians(lon1)-dlon
            lat2 = math.radians(lat1)+dlat
        else:
            lon2 = math.radians(lon1)-dlon
            lat2 = math.radians(lat1)-dlat
    elif heading == 90 :
        if yön > 0:
            lon2 = math.radians(lon1)+dlon
            lat2 = math.radians(lat1)+dlat
        else:
            lon2 = math.radians(lon1)-dlon
            lat2 = math.radians(lat1)+dlat
    elif heading == 180 :
        if yön > 0:
            lon2 = math.radians(lon1)+dlon
            lat2 = math.radians(lat1)-dlat
        else:
            lon2 = math.radians(lon1)+dlon
            lat2 = math.radians(lat1)+dlat
    elif heading == 270 :
        if yön > 0:
            lon2 = math.radians(lon1)+dlon
            lat2 = math.radians(lat1)-dlat
        else:
            lon2 = math.radians(lon1)-dlon
            lat2 = math.radians(lat1)-dlat    
        
    print(math.degrees(lat2),math.degrees(lon2))
    return math.degrees(lat2),math.degrees(lon2)

def hesapla(yukseklik,alan3,orta_nokta):
    dikey_aci_ileri = 25
    dikey_aci_geri = 25
    yatay_aci_sol = 40
    yatay_aci_sağ = 40
    
    yatay_pixsel = (1920*math.tan(math.radians(yatay_aci_sağ)))/(math.tan(math.radians(yatay_aci_sol))+math.tan(math.radians(yatay_aci_sağ)))
    dikey_pixsel = (1080*math.tan(math.radians(dikey_aci_geri)))/(math.tan(math.radians(dikey_aci_ileri))+math.tan(math.radians(dikey_aci_geri)))
    tan_y = (1080-dikey_pixsel-alan3[1])*math.tan(math.radians(dikey_aci_ileri))/(1080-dikey_pixsel)
    tan_x = -1*(1920-yatay_pixsel-alan3[0])*math.tan(math.radians(yatay_aci_sol))/(1920-yatay_pixsel)
    gercek_uzaklik_yatay = tan_x*(math.sqrt(pow((yukseklik*math.tan(math.radians(dikey_aci_ileri))*(1080-dikey_pixsel-alan3[1])/(1080-dikey_pixsel)),2)+pow((yukseklik),2)))
    gercek_uzaklik_dikey = tan_y*(math.sqrt(pow((yukseklik*math.tan(math.radians(yatay_aci_sol))*(1920-yatay_pixsel-alan3[0])/(1920-yatay_pixsel)),2)+pow((yukseklik),2)))  
    
    if orta_nokta[0]>=alan3[0]:
        yön=1
    else:
        yön=-1
    return (gercek_uzaklik_yatay,gercek_uzaklik_dikey),(ters_haversine(gercek_uzaklik_dikey,gercek_uzaklik_yatay,yön))
def camera():
    cap = cv2.VideoCapture(0)#"rtsp://192.168.144.25:8554/main.264"
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)#3
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)#4
    yatay_pixsel2,dikey_pixsel2 = 960,540
    red_lower = np.array([167, 145, 201])
    red_upper= np.array([179, 238, 255])
    cv2.namedWindow('tam ekran',cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('tam ekran',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    while True:
        _,image = cap.read()
        oran = (1080/image.shape[0])
        nokta_x , nokta_y = int(yatay_pixsel2/oran),int(dikey_pixsel2/oran)

        dikey_çizgi_baslangic= (int(yatay_pixsel2/oran),0)
        dikey_çizgi_bitis= (int(yatay_pixsel2/oran),int(1080/oran))
        yatay_çizgi_baslangic = (0,int(dikey_pixsel2/oran))
        yatay_çizgi_bitis = (int(1920/oran),int(dikey_pixsel2/oran))
        renk = (255,0,0)
        renk2 = (0,0,255)
        image = cv2.line(image,dikey_çizgi_baslangic,dikey_çizgi_bitis,renk,2)
        image = cv2.line(image,yatay_çizgi_baslangic,yatay_çizgi_bitis,renk,2)
        hsvFrame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
        contours, _ = cv2.findContours(red_mask,1,2)
        objectCounterRed = 1
        
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 300:
                if objectCounterRed == 1:
                    x, y, w, h = cv2.boundingRect(contour)
                    image = cv2.rectangle(image, (x, y),
                                               (x + w, y + h),
                                               (0, 0, 255), 2)
                    a=int(x+w/2)
                    b=int(y+h/2)
                    cv2.circle(image,(a,b),2,(255,0,0),-1)
                    gercek_uzaklik,gercek_konum = hesapla(26,(a*oran,b*oran),(yatay_pixsel2,dikey_pixsel2))
                    image = cv2.line(image,(nokta_x , nokta_y),(nokta_x,int(b)),renk2,2)
                    image = cv2.line(image,(nokta_x , nokta_y),(int(a),nokta_y),renk2,2)
                    cv2.putText(image, str(gercek_uzaklik[1])+"metre", (nokta_x,int((b+nokta_y)/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
                    cv2.putText(image, str(gercek_uzaklik[0])+"metre", (int((a+nokta_x)/2),nokta_y+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        
                    #print((str(gercek_konum[0])+" "+str(gercek_konum[1])))
                objectCounterRed += 1
        cv2.imshow("tam ekran", image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
camera()