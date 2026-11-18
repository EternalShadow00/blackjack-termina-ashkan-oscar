"""
baraja.py - La baraja francesa de 52 cartas para el blackjack.

Una carta es una tupla (valor, palo), por ejemplo ("A", "♠") o ("10", "♥").
"""

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
