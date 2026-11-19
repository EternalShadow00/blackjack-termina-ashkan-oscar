"""
main.py - Blackjack en terminal.

- Turno del jugador y bucle de partidas: Ashkan (issue #3)
- Turno del crupier y quién gana: Óscar (issue #4)

Se ejecuta con:  python main.py
"""

import sys

from baraja import crear_baraja, barajar, repartir
from mano import calcular_puntos, mostrar_mano

# Para que se vean ♠ ♥ ♦ ♣ en la terminal de Windows
sys.stdout.reconfigure(encoding="utf-8")


def turno_jugador(baraja, jugador):
    """El jugador pide carta (p) o se planta (s). Devuelve sus puntos finales."""
    while True:
        print("Tu mano:", mostrar_mano(jugador))

        # Si se pasa de 21, su turno termina
        if calcular_puntos(jugador) > 21:
            print("¡Te has pasado de 21!")
            break

        opcion = input("¿Pides carta (p) o te plantas (s)? ").strip().lower()
        if opcion == "p":
            carta = repartir(baraja)
            jugador.append(carta)
            print("Te sale:", carta[0] + carta[1])
        elif opcion == "s":
            print("Te plantas.")
            break
        else:
            print("No te entiendo: escribe p o s.")

    return calcular_puntos(jugador)

def turno_crupier(baraja, crupier):
    """El crupier enseña su mano y pide carta mientras tenga menos de 17."""
    print("Mano del crupier:", mostrar_mano(crupier))
    while calcular_puntos(crupier) < 17:
        carta = repartir(baraja)
        crupier.append(carta)
        print("El crupier pide y le sale:", carta[0] + carta[1])
        print("Mano del crupier:", mostrar_mano(crupier))
    return calcular_puntos(crupier)


def decidir_ganador(puntos_jugador, puntos_crupier):
    """Compara los puntos y dice quién gana."""
    if puntos_crupier > 21:
        print("El crupier se ha pasado de 21. ¡Ganas!")
    elif puntos_jugador > puntos_crupier:
        print("¡Ganas!", puntos_jugador, "a", puntos_crupier)
    elif puntos_jugador < puntos_crupier:
        print("Pierdes.", puntos_jugador, "a", puntos_crupier)
    else:
        print("Empate a", puntos_jugador)


def jugar_partida():
    """Juega una partida completa."""
    # Preparamos una baraja nueva y la mezclamos
    baraja = crear_baraja()
    barajar(baraja)

    # Dos cartas para cada uno
    jugador = [repartir(baraja), repartir(baraja)]
    crupier = [repartir(baraja), repartir(baraja)]

    # Del crupier solo se ve la primera carta; la segunda está boca abajo
    print("\nCarta visible del crupier:", crupier[0][0] + crupier[0][1])

    puntos_jugador = turno_jugador(baraja, jugador)
    if puntos_jugador > 21:
        print("Pierdes. Gana el crupier.")
        return

      # --- Turno del crupier y resultado: Óscar (issue #4) ---
    puntos_crupier = turno_crupier(baraja, crupier)
    decidir_ganador(puntos_jugador, puntos_crupier)



def main():
    print("=== BLACKJACK ===")
    while True:
        jugar_partida()
        otra = input("\n¿Otra partida? (s/n) ").strip().lower()
        if otra != "s":
            print("¡Hasta la próxima!")
            break


# Solo arranca el juego si se ejecuta este archivo directamente
if __name__ == "__main__":
    main()
