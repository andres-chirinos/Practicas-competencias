n = int(input()) 
coordenadas = [tuple(map(int, input().split())) for _ in range(n)]

# Almacenamos las capitales ordenadas por su pendiente.
pendientes = sorted(coordenadas, key=lambda x: x[1] / x[0])
print(*pendientes)
# Consideramos las capitales una a una.
reinos_con_territorio_infinito = []
for pendiente in pendientes:
  # Calculamos el punto más lejano en el eje x que se encuentra en el territorio de la capital actual.
  x_mas_lejano = float("inf")
  for x, y in coordenadas:
    if x > x_mas_lejano and y <= x * pendiente:
      x_mas_lejano = x
  # Si este punto se encuentra en el territorio de otra capital, entonces la capital actual no tiene territorio infinito.
  for x, y in coordenadas:
    if x == x_mas_lejano and y > x * pendiente:
      break
    else:
      # La capital actual tiene territorio infinito.
      reinos_con_territorio_infinito.append(pendiente + 1)


print(*reinos_con_territorio_infinito)
