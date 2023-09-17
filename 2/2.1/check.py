name, cost, weight, num = input(), int(input()), int(input()), int(input())

print('Чек')
print(f"{name} - {weight}кг - {cost}руб/кг")
print(f"Итого: {cost * weight}руб")
print(f"Внесено: {num}руб")
print(f"Сдача: {num - cost * weight}руб")