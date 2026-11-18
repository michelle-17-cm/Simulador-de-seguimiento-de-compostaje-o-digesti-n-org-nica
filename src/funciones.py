def calcular_promedio(datos):
    if len(datos) == 0:
        return 0
    return sum(datos) / len(datos)


def calcular_humedad(datos):
    if len(datos) == 0:
        return 0
    return sum(datos) / len(datos)


def calcular_variacion(datos):
    if len(datos) < 2:
        return 0
    return datos[-1] - datos[0]


def resumen_compostaje(temperaturas, humedades):
    promedio_temp = calcular_promedio(temperaturas)
    promedio_humedad = calcular_humedad(humedades)
    variacion_temp = calcular_variacion(temperaturas)

    print("===== RESUMEN DEL COMPOSTAJE =====")
    print("Temperatura promedio:", promedio_temp, "°C")
    print("Humedad promedio:", promedio_humedad, "%")
    print("Variación de temperatura:", variacion_temp, "°C")