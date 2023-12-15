def min_time_to_capital(n, m, k, roads):
  """
  Calcula el tiempo mínimo requerido para llegar a la capital, sin que se acabe el agua antes de llegar.

  Args:
    n: El número de poblados.
    m: La cantidad de caminos.
    k: Los litros iniciales de agua.
    roads: Una lista de tuples, donde cada tuple representa un camino. Cada tuple tiene la forma (origen, destino, tiempo, agua).

  Returns:
    El tiempo mínimo requerido, o -1 si es imposible llegar a la capital.
  """

  # Creamos un grafo dirigido, donde cada vértice representa un poblado y cada arco representa un camino.

  graph = {}
  for i in range(n):
    graph[i] = {}
  for road in roads:
    graph[road[0]][road[1]] = (road[2], road[3])

  # Inicializamos las distancias.

  distances = [float("inf") for _ in range(n)]
  distances[0] = 0

  # Aplicamos el algoritmo de Bellman-Ford.

  for _ in range(n):
    for i in range(n):
      for j in graph[i]:
        if distances[i] + graph[i][j][0] < distances[j] and distances[i] + graph[i][j][0] <= k:
          distances[j] = distances[i] + graph[i][j][0]

  # Si la distancia a la capital es mayor que la cantidad de agua inicial, entonces es imposible llegar.

  if distances[n - 1] > k:
    return -1

  # De lo contrario, la respuesta es la distancia a la capital.

  return distances[n - 1]


print(min_time_to_capital(5, 5, 20, [(1, 2, 2, 15), (2, 4, 1, 3), (1, 3, 10, 9), (3, 4, 4, 4), (4, 5, 7, 7)]))