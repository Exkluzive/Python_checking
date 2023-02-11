# Путевой вычислитель(компютер)  v.0.0.2


stars = 50        # Кол-во звездочек перед подсчетом прогамы (оформление)
tabs = 10           # кол-во отступов
programm = "Путевой расчет  v. 0. 0. 2"

dist = 0            # Расстояние каторе нужно проехать
speed = 0           # Средняя скорость транспорта , км\ч
time = 0            # Время в движение (за рулем)
total_time = 0      # Общее время в пути
drive_hours = 0     # Часов в движении (полных)
drive_mins = 0      # Минут (остаток)
total_hours = 0     # Часов всего (Поных)
total_mins = 0

fuel_tank = 0       # Объем топливного бака
consum_100km = 0    # средний расход топлива на 100 км\л
dist = 0            # Расстояние в км.
refuels = 0         # Кол-во дозаправок
refuel_time = 20    # Время дозаправки
fuel = 0            # Сколько затрачено топлива
price = 0           # Цена топлива за литр

breaks = 0  # Кол-во плановых остановок
break_time = 0  # Время каждой плановой остановки



# Выводим заголовок программы
print("\t" * tabs, programm)
print("🚗" * stars)


# Ввод данных от пользователя данной проги

dist = int(input("Введите расстояние, КМ: "))
speed = int(input("Планируемая средняя скорость, Км/Ч :"))
fuel_tank = float(input("Объем топливного бака Л. : "))
consum_100km = float(input("Введите средний расход топлива на л./100км :"))
price = int(input("Введите стоймость 1 л. топлива, Руб : "))
breaks = int(input("Количество плановых остановок: "))
break_time = float(input("Время каждой плановой остановки, минут: "))

# Производим вечисления

time = dist * 60 / speed  # Время за рулем
fuel = consum_100km * dist / 100  # Всего затрачено топлива

refuels = fuel // fuel_tank # Дозаправка
total_time = time + refuels * refuel_time + breaks * break_time
drive_hours = time // 60
drive_mins =  time - drive_hours * 60
total_hours = total_time // 60
total_mins = total_time - total_hours * 60

print("*" * stars)
print("\t" * tabs, "Результат вычисления вашего маршрута!!!")


print("Время за рулем :", int(drive_hours), "ч", int(drive_mins), "м.")
print("Общее время в пути Ч:", int(total_hours), "ч", int(total_mins), "м.")
print("Потрачено времени на дозаправку:", refuels * refuel_time, "минут")
print("Количество дозаправок в пути:", refuels)
print("Израсходовано топлива, Л.:", fuel)
print("Количество дозаправок в пути:", refuels)
print(" Общая стоймость топлива на всю поездку с учетом дозаправок :", price * fuel,  "Рублей")

