

#Список банков и процентных ставок
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_values_list=list(per_cent.values()) #Список процентных ставок
print(per_cent_values_list)

money = float(input("Введите сумму вклада:"))

for i in range(len(per_cent_values_list)):
    per_cent_values_list[i]=per_cent_values_list[i]*money/100
    
deposit=per_cent_values_list
print(deposit)   #накопленные средства за год вклада в каждом из банков

max_deposit=max(deposit)
print("Максимальная сумма, которую вы можете заработать - ", max_deposit)

