# Cantidad total de segundos
cant_segundos = 288325

# Calcular el número de días
dias = cant_segundos // (24 * 3600)
cant_segundos = cant_segundos % (24 * 3600)

# Calcular el número de horas
horas = cant_segundos // 3600
cant_segundos %= 3600

# Calcular el número de minutos
minutos = cant_segundos // 60

# Calcular el número de segundos restantes
segundos = cant_segundos % 60

# Imprimir el resultado
print("Días:", dias)
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)