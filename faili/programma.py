def ierakstit(teksts, faila_nosaukums):
    fails = open(faila_nosaukums, "w", encoding='utf-8')
    fails.write(teksts)
    fails.close()

def pierakstit(teksts, faila_nosaukums):
    fails = open(faila_nosaukums, "a", encoding='utf-8')
    fails.write(teksts)
    fails.close()

def nolasit(faila_nosaukums):
    with open(faila_nosaukums, "r", encoding="utf-8") as fails:
        rindas = fails.readlines()
    return rindas

vardi = ["Anna", "Maija", "Jānis", "Kaspars"]
uzvardi = ["Bērziņa", "Paija", "Ozols", "Kasprets"]
vecums = [23,150,89,11]
dzimums = ["s", "s", "v", "v"]

ierakstit("", "faili/cilveki.txt")

for i in range( len(vardi) ):
    if dzimums[i] == "s":
        rakstamais = "sieviete"
    else:
        rakstamais = "vīrietis"
    teksts = "{} {} - {}, {} \n".format(vardi[i], uzvardi[i], vecums[i], rakstamais)
    pierakstit(teksts, "faili/cilveki.txt" )

# pierakstit("Sveiki, visi!\n \" \n ", "faili/teksts.txt")
    
# Faili, kuru nosaukums ir cilveks0.txt, 
# saturs - Sveiki, Marta! Jūs esat laimējusi vecums*100 (3200) dolārus!
    
def sutit_vestules(vardi, uzvardi, vecums, dzimums):
    for i in range(0, len(vardi)):
        with open("vēstules/vestule{}.txt".format(i), "w", encoding="utf-8") as f:
            if dzimums[i] == "sieviete":
                f.write("Sveika, {} {}! Tu esi laimējusi {}€!".format(vardi[i], uzvardi[i], vecums[i]*10))
            else:
                f.write("Sveiks, {} {}! Tu esi laimējis {}€!".format(vardi[i], uzvardi[i], vecums[i]*10))
        i+=1
               

visi = nolasit("faili/cilveki.txt")
vardi = []
uzvardi = []
vecums = []
dzimums = []
for cilveks in visi:
    info = cilveks.split(" ")
    vardi.append(info[0])
    uzvardi.append(info[1])
    vecums1 = int(info[3].rstrip(","))
    vecums.append(vecums1)
    dzimums.append(info[4])

print(vardi)
print(uzvardi)
print(vecums)
print(dzimums)
sutit_vestules(vardi, uzvardi, vecums, dzimums)




# KM - Pabeigt programmu, lai, izmantojot datus no viena faila, uztaisītos daudzi faili mapītē "vēstules", 
# kur failu nosaukumi ir "vestule1.txt", "vestule2.txt" utt. un failos ierakstīts "Sveika, Marta Britāla! Tu esi laimējusi 320€!" 
# vai "Sveiks, Jānis Bērziņš! Tu esi laimējis 150€!" attiecīgi cilvēkiem ar datiem "Marta Britāla - 32, sieviete" 
# un "Jānis Bēziņš - 15, vīrietis". (naudas summa ir vecums*10 un vēstulē vārdiem mainās galotnes atbilstoši dzimumam).