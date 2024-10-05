orbits = {}

planets = ('Меркурій', 'Венера', 'Земля', 'Марс', 'Юпітер', 'Сатурн', 'Уран', 'Нептун')

for planet in planets:
    radius = float(input(f"Введіть радіус орбіти для {planet}: "))
    orbits[planet] = radius

name = input("Введіть назву нової планети, щоб додати до словника: ")
radius = float(input(f"Введіть радіус орбіти для {name}: "))
orbits[name] = radius
print(f"Планету {name} додано до словника.")

name = input("Введіть назву планети для пошуку по словнику: ")
radius = orbits.get(name)
if radius is not None:
    print(f"Радіус орбіти планети {name}: {radius}")
else:
    print(f"Планету {name} не знайдено в словнику.")