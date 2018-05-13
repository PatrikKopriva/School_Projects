from PIL import Image
import random

#1. slouží k vykreslování kruhů do obrázku a následující práci s nimi
def create():
    im=Image.new("RGB", (840,640), (255,255,255))
    im.save("circles.bmp")
#slouží k vykreslování jednoho kruhu se zadaným středem a poloměrem
#před používáním funkcí s kružnicemi je potřeba použít funkci "create"
def circle(x0,y0,radius):
    im = Image.open("circles.bmp")
    im = im.convert("RGB")
    x = radius-1
    y = 0
    dx = 1
    dy = 1
    err = dx - (radius << 1)
    while (x >= y):
        im.putpixel((x0 + x, y0 + y),(0,0,0))
        im.putpixel((x0 + y, y0 + x),(0,0,0))
        im.putpixel((x0 - y, y0 + x),(0,0,0))
        im.putpixel((x0 - x, y0 + y),(0,0,0))
        im.putpixel((x0 - x, y0 - y),(0,0,0))
        im.putpixel((x0 - y, y0 - x),(0,0,0))
        im.putpixel((x0 + y, y0 - x),(0,0,0))
        im.putpixel((x0 + x, y0 - y),(0,0,0))
        if err <= 0:
            y+=1
            err += dy
            dy += 2
        if err > 0:
            x-=1
            dx += 2
            err += dx - (radius << 1)
    im.save("circles.bmp")
    
#slouží k vytváření náhodných souřadnic středu a poloměru
def randomCircles(n):
    for i in range(n):
        x0=random.randint(20,820)
        y0=random.randint(20,620)
        rngx=x0
        rngy=y0
        limit=1
        if rngx<420:
            rngx=x0-1
        else:
            rngx=x0-419
            rngx=420-rngx
        if rngy<320:
            rngy=y0-1
        else:
            rngy=y0-319
            rngy=320-rngy
        if rngy<rngx:
            limit=rngy
        else:
            limit=rngx
        radius=random.randint(0,limit)
        circle(x0,y0,radius)
        
#slouží k vybarvování průsečíků
def crossing():
    im= Image.open("circles.bmp")
    im= im.convert("RGB")
    for i in range (2,638):
        for j in range (2,838):
            black=0
            for l in range (3):
                if im.getpixel((j+l,i))==(0,0,0) or im.getpixel((j+l,i))==(255,0,0):
                    black+=1
                if im.getpixel((j+l,i-1))==(0,0,0) or im.getpixel((j+l,i-1))==(255,0,0):
                    black+=1
                if im.getpixel((j+l,i+1))==(0,0,0) or im.getpixel((j+l,i+1))==(255,0,0):
                    black+=1
            if black>4:
                for l in range (3):
                    if im.getpixel((j+l,i))==(0,0,0):
                        im.putpixel((j+l,i),(255,0,0))
                    if im.getpixel((j+l,i-1))==(0,0,0):
                        im.putpixel((j+l,i-1),(255,0,0))
                    if im.getpixel((j+l,i+1))==(0,0,0):
                        im.putpixel((j+l,i+1),(255,0,0))
    im.save("circles.bmp")
    
#rozmaže obrázek
def blur():
    im= Image.open("circles.bmp")
    im= im.convert("RGB")
    for i in range (2,638):
        for j in range (2,838):
            R=[]
            G=[]
            B=[]
            avgR=0
            avgG=0
            avgB=0
            for l in range (3):
                R.append(im.getpixel((j+l,i))[0])
                G.append(im.getpixel((j+l,i))[1])
                B.append(im.getpixel((j+l,i))[2])
                R.append(im.getpixel((j+l,i-1))[0])
                G.append(im.getpixel((j+l,i-1))[1])
                B.append(im.getpixel((j+l,i-1))[2])
                R.append(im.getpixel((j+l,i+1))[0])
                G.append(im.getpixel((j+l,i+1))[1])
                B.append(im.getpixel((j+l,i+1))[2])
            for l in R:
                avgR+=l
            avgR=avgR/9
            avgR=round(avgR)
            for l in G:
                avgG+=l
            avgG=avgG/9
            avgG=round(avgG)
            for l in B:
                avgB+=l
            avgB=avgB/9
            avgB=round(avgB)
            for l in range (3):
                im.putpixel((j+l,i),(avgR,avgG,avgB))
                im.putpixel((j+l,i-1),(avgR,avgG,avgB))
                im.putpixel((j+l,i+1),(avgR,avgG,avgB))
        im.save("circles.bmp")        
