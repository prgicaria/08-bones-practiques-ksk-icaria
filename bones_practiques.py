#!/usr/bin/env python3
"""
Divisió entre dos enters
Institut Icària
Programació - 1r Batxillerat - Curs 2023-24

Descripció: Aquest programa demana dos nombres
enters a l'usuari (dividend i divisor),
calcula la divisió, el quocient i el residu,
i mostra els resultats per pantalla
amb el format esperat.
'''
__author__ = "Koa Salazar"
__email__= "koasalazar@instituticaia.cat"
__date__ = "2024/10/16"
"""


def main():
    """
    Funció principal que demana dos enters a l'usuari, realitza els càlculs
    corresponents i mostra la divisió, el quocient i el residu.
    """
    # Demana a l'usuari que introdueixi el dividend i el divisor
    dividend = int(input("Introdueix el dividend: "))
    divisor = int(input("Introdueix el divisor: "))

    # Calcula el quocient i el residu
    quocient = dividend // divisor
    residu = dividend % divisor

    # Mostra els resultats segons el format esperat
    print(f"Divisió: {dividend}/{divisor}")
    print(f"Quocient: {quocient}")
    print(f"Residu: {residu}")


if __name__ == "__main__":
    main()
