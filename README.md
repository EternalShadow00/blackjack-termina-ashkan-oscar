# Blackjack en terminal

Mini-proyecto en parejas del **Módulo Optativo** de 2º DAW (IES María Moliner).
Es un blackjack para jugar en la terminal contra el crupier, escrito en Python.

El objetivo principal del proyecto es trabajar en equipo con **Git y GitHub**: cada tarea es una Issue, se desarrolla en su propia rama y entra en `main` mediante una Pull Request revisada por el compañero.

## Cómo ejecutarlo

Necesitas **Python 3** (no hace falta instalar nada más: solo usa la librería estándar).

```bash
git clone https://github.com/EternalShadow00/blackjack-termina-ashkan-oscar.git
cd blackjack-termina-ashkan-oscar
python main.py
```

## Reglas del juego

- Se juega con una baraja francesa de 52 cartas, que se baraja en cada partida.
- El jugador y el crupier reciben 2 cartas. Del crupier solo se ve la primera.
- Puntos de las cartas:
  - del 2 al 10, lo que indica la carta;
  - J, Q y K valen 10;
  - el As vale 11, o 1 si con 11 la mano se pasa de 21.
- El jugador pide carta (`p`) o se planta (`s`). Si pasa de 21, pierde.
- Después juega el crupier: pide carta mientras tenga menos de 17.
- Si el crupier se pasa de 21, gana el jugador. Si no, gana quien tenga más puntos. Con los mismos puntos hay empate.
- Al terminar, el juego pregunta si quieres jugar otra partida.

## Estructura

```
├── baraja.py      # crear, barajar y repartir las cartas
├── mano.py        # calcular los puntos y mostrar una mano
├── main.py        # el juego: turno del jugador, turno del crupier y resultado
├── README.md
└── docs/
    ├── proceso-git.md   # documentación del proceso con Git y GitHub
    └── img/             # capturas
```

Una carta es una tupla `(valor, palo)`, por ejemplo `("A", "♠")`, y una mano es una lista de cartas.

## Flujo de trabajo con Git

1. Cada tarea tiene su **Issue**.
2. Se trabaja en una rama `feature/...` creada desde `main`.
3. Se sube la rama y se abre una **Pull Request** con `Closes #n`.
4. El compañero la revisa y la fusiona. La rama `main` está protegida: no se puede subir nada directamente y cada PR necesita 1 aprobación.

## Autores

- Ashkan Sevinov ([@EternalShadow00](https://github.com/EternalShadow00)): `baraja.py`, turno del jugador y README.
- Óscar ([@Oscarblan4](https://github.com/Oscarblan4)): `mano.py`, turno del crupier y `docs/proceso-git.md`.
