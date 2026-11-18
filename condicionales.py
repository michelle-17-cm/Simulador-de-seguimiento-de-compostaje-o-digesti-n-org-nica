def evaluar_compostaje(temperatura, humedad, relacion_cn, oxigeno, ph):
    alertas = []

    if temperatura < 35:
        alertas.append("ALERTA: Temperatura baja (< 35 °C).")
    elif temperatura > 65:
        alertas.append("ALERTA CRITICA: Sobrecalentamiento (> 65 °C).")

    if humedad < 45:
        alertas.append("ALERTA: Humedad baja (< 45%). Regar.")
        
  elif humedad > 65:
          alertas.append("ALERTA: Humedad alta (> 65%). Agregar material seco.")

    if oxigeno < 10:
        alertas.append("ALERTA: Oxigeno bajo (< 10%). Airear o voltear.")

    if relacion_cn < 20 or relacion_cn > 35:
        alertas.append("ALERTA: Relacion C/N fuera de rango (20 - 35).")

    if ph < 6.0 or ph > 8.5:
        alertas.append("ALERTA: pH fuera de rango (6.0 - 8.5).")

    if not alertas:
        return ["OK: El compostaje esta en condiciones adecuadas."]
    return alertas


if __name__ == "__main__":
    for msg in evaluar_compostaje(60.2, 42.0, 26.4, 9.2, 7.8):
        print(msg)
        