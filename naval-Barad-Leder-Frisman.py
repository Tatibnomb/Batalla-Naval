import random


# Constantes
N = 10  # Tamaño del tablero (10x10)
CANTIDAD_DISPAROS = 15
CANTIDAD_BARCOS = 3
LONGITUDES_BARCOS = [1, 2, 3]  # Barcos de hasta 3 casillas


# Funciones
def crear_tablero(n):
    return [["⬜" for _ in range(n)] for _ in range(n)] # De CHAT GPT


def mostrar_tablero(tablero, ocultar_barcos=True):
    for fila in tablero:
        for celda in fila:
            if ocultar_barcos and celda == "🚢":
                print("⬜", end=" ")
            else:
                print(celda, end=" ")
        print()
    print()


def colocar_barco(tablero, fila, col, longitud, orientacion):
    for i in range(longitud):
        f = fila + i if orientacion == "V" else fila
        c = col + i if orientacion == "H" else col
        tablero[f][c] = "🚢"


def es_valido(tablero, fila, col, longitud, orientacion):
    for i in range(longitud):
        f = fila + i if orientacion == "V" else fila
        c = col + i if orientacion == "H" else col
        if f >= N or c >= N or tablero[f][c] == "🚢":
            return False
    return True


def ubicar_barcos_manual(nombre_jugador):
    tablero = crear_tablero(N)
    print(f"\n🔧 {nombre_jugador}, ubicá tus barcos:") #Inserta emoji (De CHAT GPT)
    for longitud in LONGITUDES_BARCOS:
        while True:
            try:
                print(f"📦 Barco de longitud {longitud}")
                fila = int(input("Fila (0 a N-1): "))
                col = int(input("Columna (0 a N-1): "))
                orientacion = input("Orientación (H o V): ").upper()
                if orientacion not in ["H", "V"]:
                    print("⚠️ Orientación inválida.")
                    continue
                if es_valido(tablero, fila, col, longitud, orientacion):
                    colocar_barco(tablero, fila, col, longitud, orientacion)
                    mostrar_tablero(tablero, ocultar_barcos=False)
                    break
                else:
                    print("⚠️ No se puede colocar ahí. Intentalo de nuevo.")
            except ValueError:
                print("⚠️ Entrada inválida.")
    return tablero


def realizar_disparo(tablero_rival, tablero_disparos, fila, col):
    if tablero_disparos[fila][col] != "⬜":
        return "repetido"
    if tablero_rival[fila][col] == "🚢":
        tablero_disparos[fila][col] = "💥"
        tablero_rival[fila][col] = "💥"
        return "acierto"
    else:
        tablero_disparos[fila][col] = "🌊"
        return "fallo"


def contar_barcos_restantes(tablero):
    return sum(fila.count("🚢") for fila in tablero)


# Juego principal
def jugar():
    print("⚓ Bienvenido a Batalla Naval 2 Jugadores ⚓")


    # Crear tableros
    tablero_j1 = ubicar_barcos_manual("Jugador 1")
    tablero_j2 = ubicar_barcos_manual("Jugador 2")
    disparos_j1 = crear_tablero(N)
    disparos_j2 = crear_tablero(N)


    turno = 1
    disparos_realizados = {1: 0, 2: 0}
    aciertos = {1: 0, 2: 0}
    fallos = {1: 0, 2: 0}


    while disparos_realizados[1] < CANTIDAD_DISPAROS or disparos_realizados[2] < CANTIDAD_DISPAROS:
        jugador = 1 if turno % 2 == 1 else 2
        tablero_rival = tablero_j2 if jugador == 1 else tablero_j1
        tablero_disparos = disparos_j1 if jugador == 1 else disparos_j2


        if disparos_realizados[jugador] >= CANTIDAD_DISPAROS:
            print(f"🚫 Jugador {jugador} ya usó todos sus disparos.")
            turno += 1
            continue


        print(f"\n🎯 Turno del Jugador {jugador}")
        mostrar_tablero(tablero_disparos, ocultar_barcos=False)
        try:
            fila = int(input("Fila: "))
            col = int(input("Columna: "))
            if not (0 <= fila < N and 0 <= col < N):
                print("⚠️ Coordenadas fuera de rango.")
                continue
            resultado = realizar_disparo(tablero_rival, tablero_disparos, fila, col)
            if resultado == "repetido":
                print("⚠️ Ya disparaste ahí.")
                continue
            elif resultado == "acierto":
                print("💥 ¡Barco enemigo impactado!")
                aciertos[jugador] += 1
            else:
                print("🌊 Agua...")


            disparos_realizados[jugador] += 1
            if contar_barcos_restantes(tablero_rival) == 0:
                print(f"🎉 Jugador {jugador} ha hundido todos los barcos enemigos. ¡Gana!")
                break


        except ValueError:
            print("⚠️ Entrada inválida. Usá números enteros.")


        turno += 1


    print("\n🏁 Fin del juego")
    print(f"Jugador 1: {aciertos[1]} aciertos, {disparos_realizados[1] - aciertos[1]} fallos")
    print(f"Jugador 2: {aciertos[2]} aciertos, {disparos_realizados[2] - aciertos[2]} fallos")


    print("\nTablero final Jugador 1 (barcos propios):")
    mostrar_tablero(tablero_j1, ocultar_barcos=False)
    print("Tablero final Jugador 2 (barcos propios):")
    mostrar_tablero(tablero_j2, ocultar_barcos=False)


# Ejecutar juego (de CHAT GPT)
if __name__ == "__main__":
    jugar()