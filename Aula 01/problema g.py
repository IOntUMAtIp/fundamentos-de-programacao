import math

a, b = map(float, input().split())
c, d = map(float, input().split())
resultado = (a - b) ** 2 + (c - d) ** 2
print(math.sqrt(resultado))