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
