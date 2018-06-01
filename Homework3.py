import random
import math
import numpy as np
import ast

def calcolaL(numeroMolecole):
	L = (2 * numeroMolecole)**(1.0/3.0) #L = L/sigma
	return L

def raggioCritico(L):
	rc = L / 2.0
	return rc

def distanza(molecola1, molecola2, L):
	distanzaXYZ=[]
	for indice in range(0,3):
		di= molecola2[indice]-molecola1[indice]
		di-= L*round(di/L)
		distanzaXYZ.append(di)
	sommaQuadrati = 0.0
	for coordinata in distanzaXYZ:
		sommaQuadrati+= coordinata**2
	distanza12 = math.sqrt(sommaQuadrati)
	return distanza12

def calcolaRx(molecola1, molecola2, L, coordinata):
	di = molecola1[coordinata] - molecola2[coordinata]
	di -= L * round(di/L)
	return di

def calcolaK(velocitaPrim, numeroMolecole): #energia cinetica
	k = 0.0
	for v in velocitaPrim:
		k += v[0]**2 + v[1]**2 + v[2]**2
	k *= 0.5
	return k

def calcolaF(posizioni, rc, L):
	forza = []
	for molecola in posizioni:
		fx = 0.0
		fy = 0.0
		fz = 0.0
		for molecola2 in posizioni:
			if molecola == molecola2:
				continue
			r = distanza(molecola, molecola2, L)
			if r > rc:
				continue
			rx = calcolaRx(molecola, molecola2, L, 0)
			ry = calcolaRx(molecola, molecola2, L, 1)
			rz = calcolaRx(molecola, molecola2, L, 2)
			fx += (rx / (r ** 3)) * (1 + r) * math.exp(-r)
			fy += (ry / (r ** 3)) * (1 + r) * math.exp(-r)
			fz += (rz / (r ** 3)) * (1 + r) * math.exp(-r)
		forza.append((fx, fy, fz))
	return forza

def calcolaU(posizioni, numeroMolecole, L, rc):
    u = 0.0
    for indice, molecola in enumerate(posizioni):
        for molecola2 in posizioni[indice+1:]:
            if molecola == molecola2:
                continue
            r = distanza(molecola, molecola2, L)
            if r > rc:
                continue
            u += (1 / r) * math.exp(-r)
    return u

def calcolaP(posizioni, numeroMolecole, L, rc, temperatura):
    pId =  numeroMolecole * temperatura / (L ** 3)
    pEx = 0.0
    for indice, molecola in enumerate(posizioni):
        for molecola2 in posizioni[indice+1:]:
            if molecola == molecola2:
                continue
            r = distanza(molecola, molecola2, L)
            if r > rc:
                continue
            pEx += (1/(3 * L ** 3)) * (1 / r + 1) * math.exp(-r)
    p = pId + pEx
    return p

def calcolaT(energia): #prende in ingresso energia per molecola
    temperatura =  2.0 / 3.0 * energia
    return temperatura

def energiaTotale(energia, potenziale):
    eTot = energia + potenziale
    return eTot

def MDloop(rc, posizioni, velocitaStart, deltat, forze, tArrivo, L, numeroMolecole):
    t = 0.0
    listaK = []
    listaU = []
    listaeTot = []
    listaTemp = []
    listaP = []
    listaF = []
    while(t < tArrivo):
        t += deltat
        posizNuove = []
        for posizione, velocita, forza in zip(posizioni, velocitaStart, forze):
			nuovaPosizX = posizione[0] + velocita[0] * deltat + 0.5 * forza[0] * (deltat ** 2)
			nuovaPosizY = posizione[1] + velocita[1] * deltat + 0.5 * forza[1] * (deltat ** 2)
			nuovaPosizZ = posizione[2] + velocita[2] * deltat + 0.5 * forza[2] * (deltat ** 2)
			posizNuove.append((nuovaPosizX, nuovaPosizY, nuovaPosizZ))
        posizioni = posizNuove
        forzeNuove = calcolaF(posizioni, rc, L)
        velocitaNuove = []
        for velocita, forza, forzaNuova in zip(velocitaStart, forze, forzeNuove):
            velocitaNuovaX = velocita[0] + 0.5 * forza[0] * deltat + 0.5 * forzaNuova[0] * deltat
            velocitaNuovaY = velocita[1] + 0.5 * forza[1] * deltat + 0.5 * forzaNuova[1] * deltat
            velocitaNuovaZ = velocita[2] + 0.5 * forza[2] * deltat + 0.5 * forzaNuova[2] * deltat
            velocitaNuove.append((velocitaNuovaX, velocitaNuovaY, velocitaNuovaZ))
        velocitaStart = velocitaNuove
        k = calcolaK(velocitaStart, numeroMolecole) / numeroMolecole
        u = calcolaU(posizioni, numeroMolecole, L, rc) / numeroMolecole
        eTot = energiaTotale(k, u)
        temp = calcolaT(k)
        p = calcolaP(posizioni, numeroMolecole, L, rc, temp)
        listaU.append(u)
        listaK.append(k)
        listaeTot.append(eTot)
        listaTemp.append(temp)
        listaP.append(p)
    with open('MDloop\\posizioni_' + str(deltat) + '.txt', 'w') as the_file:
        the_file.write(str(posizioni))
    with open('MDloop\\velocita_' + str(deltat) + '.txt', 'w') as the_file:
        the_file.write(str(velocitaStart))
    with open('MDloop\\forze_' + str(deltat) + '.txt', 'w') as the_file:
        the_file.write(str(forze))
    with open('MDloop\\k_' + str(deltat) + '.txt', 'w') as the_file:
        the_file.write(str(listaK))
    with open('MDloop\\u_' + str(deltat) + '.txt', 'w') as the_file:
        the_file.write(str(listaU))
    with open('MDloop\\eTot_' + str(deltat) + '.txt', 'w') as the_file:
        the_file.write(str(listaeTot))
    with open('MDloop\\temperatura_' + str(deltat) + '.txt', 'w') as the_file:
        the_file.write(str(listaTemp))
    with open('MDloop\\p_' + str(deltat) + '.txt', 'w') as the_file:
        the_file.write(str(listaP))



def main():
    posizioni = []
    vstart = []
    with open('startingConfig\\posizioni.txt', 'U') as f: #apre file
    	data=f.read()
    	posizioni = ast.literal_eval(data)
    with open('startingConfig\\listaVelScal.txt', 'U') as f: #apre file
    	data=f.read()
    	vstart = ast.literal_eval(data)
    numeroMolecole = 60
    L = calcolaL(numeroMolecole)
    rc = raggioCritico(L)
    forze = calcolaF(posizioni, rc, L)
    MDloop(rc, posizioni, vstart, 0.009, forze, 25.0, L, numeroMolecole)

main()
