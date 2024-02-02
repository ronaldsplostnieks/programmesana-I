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

# print(nolasit("faili/teksts.txt"))

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


# Izveidojas fails, kur katrā rindiņā ir vārds, uzvārds - vecums
# Marta Britāla - 32, sieviete

# pierakstit("Sveiki, visi!\n \" \n ", "faili/teksts.txt")
    
# Faili, kuru nosaukums ir cilveks0.txt, 
# saturs - Sveiki, Marta! Jūs esat laimējusi vecums*100 (3200) dolārus!

visi = nolasit("faili/cilveki.txt")
vardi = []
vecums = []
for cilveks in visi:
    info = cilveks.split(" ")
    vardi.append(info[0])
    vecums1 = int(info[3].rstrip(","))
    vecums.append(vecums1)

print(vecums)