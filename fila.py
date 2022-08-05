# o primeiro que entra é o primeiro que sai

from collections import deque
fila = deque(["A","B","C"])
print(fila)
fila.append("D")
print(fila)
fila.append("E")
print(fila)
fila.append("F")
print(fila)
fila.popleft()
print(fila)
fila.popleft()
print(fila)