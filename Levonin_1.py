
#print("Tere maailm!")
#1
#nimi = input("Mis on sinu nimi?")
#vanus=int(input("kui vana sa oled?"))
#print("Tere tulemast!"+ nimi + "Sa oled"+str(vanus)+" aastat vana")
#print("Tere tulemast!"  ,nimi, "Sa oled",vanus,"aastat vana")
#print("Tere tulemast! {0} sa oled {1} aastat vana".format(nimi,vanus))
#print("Muutuja vanus=",vanus,"tüüp on",type(vanus))
#2
#vanus = 18
#eesnimi = "Jaak"
#pikkus = 16.5
#kas_käib_koolis = True
#print(type(vanus))
#print(type(eesnimi))
#print(type(pikkus))
#print(type(kas_käib_koolis))

from random import * 
kokku=randint(10,100)
print("kokku: ",kokku)
mitu = int(input("mitu kommi  tahad ära võtta?"))
kokku-=mitu
print("nüüd laua peal on",kokku,"kommid")


from random import *

p=randint(1,5)
hind=12.90
hind*=1.1 #hind koos jatatega
osa=round(hind/p,2)
print("iga sõber maksab: ",osa)


try:
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    kiirus = aeg / teepikkus
    print("Sinu kiirus oli " + str(kiirus) + "km/h")
except:
    print("viga andmetüübiga")