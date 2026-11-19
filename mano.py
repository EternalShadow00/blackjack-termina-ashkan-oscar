"""
mano.py - Calcula los puntos de una mano de blackjack y la muestra como texto.

Una mano es una lista de cartas, y cada carta es una tupla (valor, palo),
por ejemplo [("A", "♠"), ("10", "♥")].
"""


def calcular_puntos(mano):
    """Devuelve los puntos de la mano. El As vale 11, o 1 si con 11 te pasas."""
    puntos = 0
    ases = 0

    for valor, palo in mano:
        if valor in ("J", "Q", "K"):
            puntos += 10          # las figuras valen 10
        elif valor == "A":
            puntos += 11          # el As cuenta primero como 11
            ases += 1
        else:
            puntos += int(valor)  # el resto vale su número

    # Si nos pasamos de 21 y hay ases contados como 11, los bajamos a 1
    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1

    return puntos