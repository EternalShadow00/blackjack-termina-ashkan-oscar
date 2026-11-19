"""
baraja.py - La baraja francesa de 52 cartas para el blackjack.

Una carta es una tupla (valor, palo), por ejemplo ("A", "♠") o ("10", "♥").
"""

import random

# Los 13 valores posibles de una carta
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Los 4 palos: picas, corazones, diamantes y tréboles
PALOS = ["♠", "♥", "♦", "♣"]


def crear_baraja():
    """Devuelve una lista con las 52 cartas, sin barajar."""
    baraja = []
    # Por cada palo, añadimos una carta de cada valor: 4 x 13 = 52 cartas
    for palo in PALOS:
        for valor in VALORES:
            baraja.append((valor, palo))
    return baraja


def barajar(baraja):
    """Mezcla las cartas de la baraja al azar (cambia la propia lista)."""
    random.shuffle(baraja)


def repartir(baraja):
    """Saca la última carta de la baraja y la devuelve."""
    # pop() quita la carta de la lista, así no puede volver a salir
    return baraja.pop()


# Prueba rápida: solo se ejecuta con "python baraja.py", no al importarlo
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")  # para que se vean ♠ ♥ ♦ ♣ en Windows

    mi_baraja = crear_baraja()
    print("Cartas en la baraja:", len(mi_baraja))
    barajar(mi_baraja)
    print("Reparto 3 cartas:", repartir(mi_baraja), repartir(mi_baraja), repartir(mi_baraja))
    print("Quedan:", len(mi_baraja))
