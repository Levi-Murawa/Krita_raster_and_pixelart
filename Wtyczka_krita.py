from krita import *
from random import random

def rasteryzacja(szer, wys, bity, ile_krok):
    krok = int(round(255 / ile_krok))
    progi = range(0, 256, krok)
    progi = list(progi)
    progi[-1] = 255
    progi[0] = 0
    for x in range(szer):
        for y in range(wys):
            ran = round(random() * 255)
            sam_pixe = int.from_bytes(bity[4 * (y * szer + x)], 'big')
            pixel_zmiana(x, y, szer, bity, 255, 255, 255, 255)
            for pro in progi:
                if(sam_pixe <= pro <= ran):
                    pixel_zmiana(x, y, szer, bity, 0, 0, 0, 255)
                    break

def losowanie(width, height, data, ile_krok):
    krok = int(round(255 / ile_krok))
    progi = range(0, 256, krok)
    progi = list(progi)
    progi[-1] = 255
    for x in range(width):
        for y in range(height):
            ran = round(random() * 255)

            for pro in progi:
                if(ran <= pro):
                    pixel_zmiana(x, y, width, data, pro, pro, pro, 255)
                    print(pro, ran)
                    break

def pixel_zmiana(x, y, szer, data, red, green, blue, alpha):
    adress = 4 * (y * szer + x) + 0
    do_wstawienia = blue.to_bytes(1, 'big')
    #print(do_wstawienia)
    data.replace(adress, 1, do_wstawienia)
    ##Blue
    adress = 4 * (y * szer + x) + 1
    do_wstawienia = green.to_bytes(1, 'big')
    data.replace(adress, 1, do_wstawienia)
    ##Grean
    adress = 4 * (y * szer + x) + 2
    do_wstawienia = red.to_bytes(1, 'big')
    data.replace(adress, 1, do_wstawienia)
    ##Red
    adress = 4 * (y * szer + x) + 3
    do_wstawienia = alpha.to_bytes(1, 'big')
    data.replace(adress, 1, do_wstawienia)
    ##Alpha



def pixel_zmiana_stara(x, y, data, red, green, blue, alpha):
    for c in range(4):
        if (c == 0):
            adress = 4 * (y * width + x) + c
            do_wstawienia = blue.to_bytes(1, 'big')
            #print(do_wstawienia)
            data.replace(adress, 1, do_wstawienia)
            ##Blue
        elif (c == 1):
            adress = 4 * (y * width + x) + c
            do_wstawienia = green.to_bytes(1, 'big')
            data.replace(adress, 1, do_wstawienia)
            ##Grean
        elif (c == 2):
            adress = 4 * (y * width + x) + c
            do_wstawienia = red.to_bytes(1, 'big')
            data.replace(adress, 1, do_wstawienia)
            ##Red
        elif (c == 3):
            adress = 4 * (y * width + x) + c
            do_wstawienia = alpha.to_bytes(1, 'big')
            data.replace(adress, 1, do_wstawienia)
            ##Alpha
        else:
            print('Cos nie dziala')

def szachownica(width, height, data, red, green, blue, alpha):
    for x in range(width):
        for y in range(height):
            if ((x + y) % 2 == 0):
                pixel_zmiana(x, y, width, data, red, green, blue, alpha)

# newDocument = Krita.instance().createDocument(4, 4, "Document name", "RGBA", "U8", "", 300.0)
# activeView = Krita.instance().activeWindow().activeView()

width = Krita.instance().activeDocument().width()
height = Krita.instance().activeDocument().height()

l = Krita.instance().activeDocument().activeNode()  # get current layer
data = l.pixelData(0, 0, width, height)  # get pixels as QByteArray

#szachownica(width, height, data, 0, 0, 0, 255)
#losowanie(width, height, data, 6)
rasteryzacja(width, height, data, 6)

l.setPixelData(data, 0, 0, width, height)  # copy back to image
Krita.instance().activeDocument().refreshProjection()  # refresh