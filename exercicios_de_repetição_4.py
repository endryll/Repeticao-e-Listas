a = 80000
b = 200000
ano = 0

while a <= b:
    a += a * 0.03
    b += b * 0.015
    ano += 1

print(f"Em {ano} anos, a população de A ({a:.0f}) ultrapassará ou igualará a população de B ({b:.0f}).")