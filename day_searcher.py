def dienas_mekletajs (sis_gads, sis_menesis, sis_datums, si_diena, dz_gads, dz_menesis, dz_datums):
    menesu_dienu_skaits = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    #Skaitām, cik dienas ir pagājušas
    #Pārbaude, vai šogad jau ir bijusi dzimšanas diena
    

    pagajusas_dienas = 0
    pagajusie_gadi = sis_gads-dz_gads

    if vai_datums_pagajis(sis_menesis, sis_datums, dz_menesis, dz_datums) == False:
        pagajusie_gadi -=1

    pagajusas_dienas += 365*pagajusie_gadi

    garie_gadi = 0
    sakuma_gads = dz_gads
    if vai_datums_pagajis(dz_menesis, dz_datums, 2, 29):
        sakuma_gads +=1

    beigu_gads = sis_gads
    if vai_datums_pagajis(sis_menesis, sis_datums, 2, 29) == False:
        beigu_gads -=1


    for gads in range (sakuma_gads, beigu_gads+1):
        if gads % 4 == 0:
            garie_gadi +=1
        if gads % 100 == 0 and gads % 400 != 0:
            garie_gadi -=1

    pagajusas_dienas += garie_gadi

    # cik pilni mēneši ir pagājuši?
    # cik dienas ir kopā pa tiem mēnešiem?
    # cik dienas ir pagājušas nepilnajā mēnesī?

    return "OK"


def vai_datums_pagajis(tagad_menesis, tagad_datums, salidzinamais_menesis, salidzinamais_datums):
    if tagad_menesis>salidzinamais_menesis:
        return True
    if tagad_menesis<salidzinamais_menesis:
        return False
    if tagad_datums>salidzinamais_datums:
        return True
    return False
    