print("Tere! olen sinu uus sõber - Python")
nimi=input("Kirjuta sinu nimi:")
print(nimi)
print("Oi kui ilus nimi!")
Vastus= int(input(nimi + ",Kas leian sinu keha indeksi? 0-ei,1-jah => "))
if Vastus == 1:
    pikkus=int(input("Kirjuta sinu pikkus: "))
    mass = int(input("Kirjuta sinu mass: "))
    indeks = mass /(0.01*pikkus)**2
    print(nimi + "!Sinu keha indeks on: ",round(indeks))

