def fonction_cadre_ligne(Liste, l, h, ph, pb ):
    for i in range(h):
        for j in range(l):
            if(not(ph[0]<i and pb[0]>i and ph[1]< j and pb[1] >j )):
                Liste.append(((j, i), 180, 0, 0.008, 0.008))
    return Liste

def fonction_cadre_cran(Liste, l, h, ph, pb ):
    for i in range(h):
        for j in range(l):
            if(not(ph[0]<i and pb[0]>i and ph[1]< j and pb[1] >j )):
                Liste.append(((j, i), 45, 135, 0.008, 0.008))
    return Liste