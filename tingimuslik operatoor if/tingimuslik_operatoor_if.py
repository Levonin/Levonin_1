nimi=input("mis sul nimi on?").capitalize()
print("Tere,",nimi)
if nimi=="Juku":
    print("Lahme kinno")
    vanus=int(input("Kui vana sa oled?"))
    if vanus<0 or vanus>100:
        pilet="vale vanus"
    elif vanus<6:
        pilet="tasuta pilet"
    elif vanus<=14:
        pilet="lastepilet"
    elif vanus<=65:
        pilet="täispilet"
    elif vanus<=100:
        pilet="sooduspilet"
    print(pilet)    ### ilus vastu

else:
    print("Ma ootan Jukut")


