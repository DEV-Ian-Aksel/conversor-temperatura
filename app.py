
def convertir(temperatura, origen, destino):
    escalas = ["C", "F", "K"]

    origen = origen.upper()
    destino = destino.upper()

    if origen not in escalas or destino not in escalas:
        raise ValueError("Escala no válida")

    # Convertir primero a Celsius
    if origen == "C":
        celsius = temperatura
    elif origen == "F":
        celsius = (temperatura - 32) * 5 / 9
    else:
        celsius = temperatura - 273.15

    if celsius < -273.15:
        raise ValueError("Temperatura inferior al cero absoluto")

    # Convertir de Celsius a la escala destino
    if destino == "C":
        return celsius
    elif destino == "F":
        return (celsius * 9 / 5) + 32
    else:
        return celsius + 273.15
