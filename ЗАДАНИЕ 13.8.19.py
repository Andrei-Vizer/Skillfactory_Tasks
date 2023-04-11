total = 0
ticket = int(input('Введите количество билетов: '))
if ticket > 3:
    discount = 10
else:
    discount = 0
for i in range(ticket):
    age = int(input('Введите ваш возраст: '))
    if age < 18:
        ticket = 0
    elif 18 <= age < 25:
        ticket = 990
    else:
        ticket = 1390
    total += ticket
print('Общая стоимость билетов = ', total, 'руб')
if discount:
    total *= (100-discount)/100
    print(f"Ваша скидка = {discount} %. Итоговая стоимость ={total}, руб")