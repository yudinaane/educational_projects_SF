quantity_ticket = int(input('Введите количество билетов\n'))
print('Введите для каждого билета возраст посетителя')
age_visitor = [int(input()) for i in range(1, quantity_ticket+1)]

quantity_age = [0, 0, 0]
for age in age_visitor:
    if age < 18:
        quantity_age[0] = quantity_age[0]+1
    if 18 <= age <= 25:
        quantity_age[1] = quantity_age[1]+1
    if age > 25:
        quantity_age[2] = quantity_age[2]+1
print(quantity_age)

quantity_price = [0, 990, 1390]
N = []
for i in range(3):
    N.append(quantity_age[i]*quantity_price[i])
print(str(N))
price = sum(N)


if quantity_ticket > 3:
    print('Сумма к оплате без скидки = ', price)
    print('Вы зарегистрировали более 3-х билетов, поэтому у вас есть скидка 10%.')
    new_price = price*0.9
    print('Сумма к оплате с учетом скидки = ', int(new_price))
else:
    print('Сумма к оплате = ', price)
