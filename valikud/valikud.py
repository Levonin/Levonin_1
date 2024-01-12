from random import *
protsent=randint(-100,500) #0-100 0-60"2", 61-75-"3", 76-89-"4", 90-100-"5"
print(protsent,"% testi tulemus")
if protsent<0 or protsent>100:
    tulemus="valed andmed"
elif 0<protsent<60: #protsent>0 and protsent<60, protsent<60
    tulemus="hinne 2"
elif 60<=protsent<75:
    tulemus="hinne 3"
elif 75<=protsent<90:
    tulemus="hinne 4"
else:   #elif 90<=protsent<=100:
    tulemus="hinne 5"

print(tulemus)
 


arv=randint(0,100)#juhuslik täisarv vahemikust 0...100
if arv%2==0:
    print(arv,"on paaris arv")
else:
    print(arv,"on paaritu arv")
print()





print("tund on alanud")
hilinemine=input("kas õpilane on hilinenud?")
#jah, JAH, Jah,jAH
if hilinemine.upper()=="JAH":
    print("õpilane ootab 30 minutit")
print("Õpilane astub klassi")






