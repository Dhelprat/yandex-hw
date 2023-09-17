name, cost, weight, money = input(), int(input()), int(input()), int(input())

print('================Чек================')
print('Товар:', ' ' * (27 - len(name)), name)
print('Цена:', ' ' * (17 - len(str(weight)) - len(str(cost))), f"{weight}кг * {cost}руб/кг")
print('Итого:', ' ' * (24 - len(str(weight * cost))), f'{weight * cost}руб')
print('Внесено:', ' ' * (22 - len(str(money))), f'{money}руб')
print('Сдача:', ' ' * (24 - len(str(money - weight * cost))),f'{money - weight * cost}руб')
print('===================================')