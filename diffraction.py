from asyncio import wait
from math import *

#    A = float(input("Entrez la valeur (A): "))
#    D = float(input("Entrez la valeur (D): "))
#    Lambda0 = float(input("Entrez la valeur (Lambda0): "))
#    L= float(input("Entrez la valeur (L): "))
#    Téta = float(input("Entrez la valeur (Téta): "))


print("A est la largeur de l'ouverture (en m)")
print("D est la distance entre l'ouverture et la surface de contact (en m)")
print("Lambda0 est la longeur d'onde du lazer (en m)")
print("L est la largeur de la tache centrale (en m)")
print("Téta est l'angle de diffraction (en rad)")

recherche = input("que recherchez vous ?")

if recherche == "A":
    D = float(input("Entrez la valeur (D): "))
    Lambda0 = float(input("Entrez la valeur (Lambda0): "))
    L= float(input("Entrez la valeur (L): "))
    A = (2*D*Lambda0)/L
    print("La valeur de A est donc: {} m.".format(A))
elif recherche == "D":
    A = float(input("Entrez la valeur (A): "))
    Lambda0 = float(input("Entrez la valeur (Lambda0): "))
    L= float(input("Entrez la valeur (L): "))
    D = (A*L)/2*Lambda0
    print("La valeur de A est donc: {} m.".format(D))
elif recherche == "Lambda0":
    A = float(input("Entrez la valeur (A): "))
    D = float(input("Entrez la valeur (D): "))
    L= float(input("Entrez la valeur (L): "))
    Lambda0 = (A*L)/2*D
    print("La valeur de A est donc: {} m.".format(Lambda0))
elif recherche == "L":
    A = float(input("Entrez la valeur (A): "))
    D = float(input("Entrez la valeur (D): "))
    Lambda0 = float(input("Entrez la valeur (Lambda0): "))
    L = (2*Lambda0*D)/A
    print("La valeur de A est donc: {} m.".format(L))
else:
    print("cette lettre ne fait pas partie du calcul de diffraction !")
