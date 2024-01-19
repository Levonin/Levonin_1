# nimi=input("mis sul nimi on?").capitalize()
# print("Tere,",nimi)
# if nimi=="Juku":
#     print("Lahme kinno")
#     vanus=int(input("Kui vana sa oled?"))
#     if vanus<0 or vanus>100:
#         pilet="vale vanus"
#     elif vanus<6:
#         pilet="tasuta pilet"
#     elif vanus<=14:
#         pilet="lastepilet"
#     elif vanus<=65:
#         pilet="täispilet"
#     elif vanus<=100:
#         pilet="sooduspilet"
#     print(pilet)    ### ilus vastu

# else:
# print("Ma ootan Jukut")

# 2
# nimi1 = input("Sisestage esimese inimese nimi: ")
# nimi2 = input("Sisestage teise inimese nimi: ")
# print(nimi1, "ja", nimi2, "on täna pinginaabrid!")

#3
# pikkus = float(input("Sisestage ruumi seina pikkus meetrites: "))
# laius = float(input("Sisestage ruumi seina laius meetrites: "))
# pindala = pikkus * laius
# print("Ruumi pindala on", pindala, "ruutmeetrit")
# remont_soov = input("Kas soovite remonti teha? (jah/ei): ")
# if remont_soov == "jah":
#     ruutmeetri_hind = float(input("Kui palju maksab ruutmeeter? "))
#     remondi_maksumus = pindala * ruutmeetri_hind
#     print("Põranda vahetamine maksab", remondi_maksumus, "eurot")

#4
# alghind = float(input("Sisestage toote alghind: "))
# if alghind > 700:
#     soodustusega_hind = alghind * 0.7
#     print("30% soodustusega hind on", soodustusega_hind)
# else:
#     print("Alghind ei ületa 700, soodustust ei rakendata.")

#5
# temperatuur = float(input("Sisestage temperatuur kraadides järgi: "))
# if temperatuur > 18:
#     print("Temperatuur on üle 18 kraadi, see on soovitav toasoojus talvel.")
# else:
#     print("Temperatuur on 18 kraadi või madalam, see võib olla pisut jahe talvel.")

#6

# pikkus = float(input("Sisestage oma pikkus meetrites: "))
# if pikkus < 1.6:
#     print("Teie pikkus on lühike.")
# elif pikkus < 1.8:
#     print("Teie pikkus on keskmine.")
# else:
#     print("Teie pikkus on pikk.")


#7
# pikkus = float(input("Sisestage oma pikkus meetrites: "))
# sugu = input("Sisestage oma sugu (mees/naine): ")
#
# if sugu == "mees":
#     if pikkus < 1.6:
#         print("Teie pikkus on lühike.")
#     elif pikkus < 1.8:
#         print("Teie pikkus on keskmine.")
#     else:
#         print("Teie pikkus on pikk.")
# else:
#     if pikkus < 1.5:
#         print("Teie pikkus on lühike.")
#     elif pikkus < 1.7:
#         print("Teie pikkus on keskmine.")
#     else:
#         print("Teie pikkus on pikk.")
# #11
# sünni_aasta = int(input("Sisestage oma sünniaasta: "))
# praegu_aasta = 2023
# aastat_vana= praegu_aasta - sünni_aasta
#
# if aastat_vana % 5 == 0:
#     print("Palju õnne, sul on juubeliaasta!")
# else:
#     print("See ei ole juubeliaasta.")

#12

# toode_hind = float(input("Sisestage toote hind: "))
# if toode_hind < 10:
#     soodustus_hind = toode_hind * 0.9
# else:
#     soodustus_hind = toode_hind * 0.8
# print("Lõplik hind:", soodustus_hind, "€")

#13
# sugu = input("Kas te olete mees või naine? (mees/naine): ")
#
# if sugu == 'mees':
#     a_vana = int(input("Palun sisestage oma vanus: "))
#     if a_vana > 15 and a_vana < 19:
#         print("Olete meeskonna jaoks sobiv kandidaat.")
#     else:
#         print("Vabandust, te ei sobi meeskonda vanuse tõttu.")
# elif sugu == "naine":
#     print("Olete meeskonna jaoks sobiv kandidaat.")
# else:
#     print("Kahjuks meeskonda kandideerimiseks peab olema mees või naine.")

#14
# inimesed = int(input("Sisestage inimeste arv: "))
# kohad = int(input("Sisestage bussi kohtade arv: "))
# bussi_vaja = inimesed // kohad
# last_bus = inimesed % kohad
# if last_bus > 0:
#     bussi_vaja += 1
# print("Vajalike busside arv:", bussi_vaja)
# print("Viimases bussis on inimesi:", last_bus)

#8

#from datetime import*
#from random import * 

#arve_nr = date.today()
#print(arve_nr)
#tsekk="arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
#summa=0

#toode="Piim"
#hind=randint(50,150)/100
#v=input("Toode:"+toode+" Hind: "+str(hind)+"\nkas tahad osta?").lower()
#if v=="jah":
#    mitu=int(input("mitu?"))
#    tsekk+=toode+"  "+str(hind)+"  "+str(mitu*hind)+"\n"
#    summa+=mitu*hind

#toode="Leib"
#hind=randint(90,300)/100
#v=input("Toode:"+toode+" Hind: "+str(hind)+"\nkas tahad osta?").lower()
#if v=="jah":
#    mitu=int(input("mitu?"))
#    tsekk+=toode+"  "+str(hind)+"  "+str(mitu*hind)+"\n"
#    summa+=mitu*hind

#    toode="Kommid"
#hind=randint(600,1500)/100
#v=input("Toode:"+toode+" Hind: "+str(hind)+"\nkas tahad osta?").lower()
#if v=="jah":
#    mitu=int(input("mitu?"))
#    tsekk+=toode+"  "+str(hind)+"  "+str(mitu*hind)+"\n"
#    summa+=mitu*hind
#    tsekk+="Kokku maksta: "+str(summa)
#    print(tsekk)
#    raha=float(input("maksa"+str(summa)))
#    if raha==summa:
#        print("tänan ostu eest")
#    elif raha >summa:
#        print("Tänan ostu eest! Tagasi "+str(raha-summa))
#    else:
#        print("Maksa veel"+str(summa-raha))
#8 uus
#from datetime import *
#from random import * 

#arve_nr = date.today()
#print(arve_nr)
#tsekk="arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
#summa=0
#for toode in ["Piim","leib","Komm"]:
#    hind=randint(50,150)/100
#    v=input("Toode:"+toode+" Hind: "+str(hind)+"\nkas tahad osta?").lower()
#    if v=="jah":
#        mitu=int(input("mitu?"))
#        tsekk+=toode+"  "+str(hind)+"  "+str(mitu*hind)+"\n"
#        summa+=mitu*hind
#tsekk+="Kokku maksta: "+str(summa)
#print(tsekk)
#while True:
#    raha=float(input("maksa "+str(summa)+"\n"))
#    if raha==summa:
#        print("tänan ostu eest")
#        break
#    elif raha >summa:
#        print("Tänan ostu eest! Tagasi "+str(raha-summa))
#        break
#    else:
#        summa-=raha
#        print("Maksa veel"+str(summa))

#11
#sünni_aasta = int(input("Sisestage oma sünniaasta: "))
#praegu_aasta = 2023
#aastat_vana= praegu_aasta - sünni_aasta

#if aastat_vana % 5 == 0:
#        print("Palju õnne, sul on juubeliaasta!")
#else:
#        print("See ei ole juubeliaasta.")

#11.2
#from datetime import *
#from random import *

#ta=date.today().year
#sp=date(int(input("Sünniaasta: ")),int(input("Sünnikuu: ")),int(input("sünnipäev: "))).year
#if (ta-sp)%5==0:
#    print("Sul on Juubell")
#else:
#        print("Tavaline sünnipäev")

#14
#inimesed = int(input("Sisestage inimeste arv: "))
#kohad = int(input("Sisestage bussi kohtade arv: "))
#bussi_vaja = inimesed // kohad
#last_bus = inimesed % kohad
#if last_bus > 0:
#    bussi_vaja += 1
#print("Vajalike busside arv:", bussi_vaja)
#print("Viimases bussis on inimesi:", last_bus)

#14.1

#maht=int(input("Bussi maht: "))
#i=int(input("Inimeste arv: "))
#ba=round(i/maht)
#if i%maht!=0:
#    ba+=1
#vb=i%maht
#print("Kokku on vaja {0} bussil ja viimasel sõidavad {1} inimest".format(ba,vb))



