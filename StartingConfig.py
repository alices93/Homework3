import random
import math
import numpy as np

def calcolaL(numeroMolecole):
	L = (numeroMolecole/0.6)**(1.0/3.0) #L = L/sigma
	return L

def generaCubo(numeroMolecole, L):
    rho = math.sqrt(2*numeroMolecole)
    insiemeCoordinate = set()
    listaVelocita= []
    while len(insiemeCoordinate)<numeroMolecole:
        x= random.random() * L
        y= random.random() * L
        z = random.random() * L
        insiemeCoordinate.add((x,y,z))
        theta = 2 * math.pi * random.random()
        phi = math.acos(1 - 2 * random.random())
        vx = rho * math.cos(theta) * math.sin(phi)
        vy = rho * math.sin(theta) * math.sin(phi)
        vz = rho * math.cos(phi)
        listaVelocita.append((vx, vy, vz))
    with open('startingConfig\\insiemeCoordinate.txt', 'w') as the_file:
        the_file.write(str(insiemeCoordinate))
    with open('startingConfig\\listaVelocita.txt', 'w') as the_file:
        the_file.write(str(listaVelocita))
    return (list(insiemeCoordinate), listaVelocita)

def main():
    numeroMolecole = 60
    L = calcolaL(numeroMolecole)
    generaCubo(numeroMolecole, L)

main()
