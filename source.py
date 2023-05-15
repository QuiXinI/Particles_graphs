import math
import matplotlib.pyplot as plt
import numpy as np


# заполнялка отступов
def filler():
    print()
    print()
    print()
    print()
    print()


def check(vx, vy):
    if vy == 0:
        return 1
    else:
        return math.degrees(math.atan2(vy, vx))


def calculate_trajectory(q, m, e, e_angle, b, b_angle, v, v_angle, time_step, x, y):
    # Вычисление компонент электрического и магнитного полей
    e_x = e * math.cos(math.radians(e_angle))
    e_y = e * math.sin(math.radians(e_angle))
    b_x = b * math.cos(math.radians(b_angle))
    b_y = b * math.sin(math.radians(b_angle))

    # Вычисление компонент ускорения
    a_x = (q * (e_x + v * b_y - v * e_y)) / m
    a_y = (q * (e_y - v * b_x + v * e_x)) / m

    # Вычисление новых компонент скорости
    v_x = v * math.cos(math.radians(v_angle)) + a_x * time_step
    v_y = v * math.sin(math.radians(v_angle)) + a_y * time_step

    # Вычисление новых компонент позиции
    x += v_x * time_step
    y += v_y * time_step

    # Вычисление нового угла
    v_angle = check(v_x, v_y)

    return [x, y, v_angle]


# предупреждение
print("Не рекомендуется вводить очень маленькие (<0.001) и очень большие (>1000) данные, из-за проблем с "
      "производительностью python в вычислениях больших значений")
filler()
_ = input("С предупреждением ознакомлен, несу ответственность за своё железо (ввести любой символ): ")
filler()

# параметры на ввод
q = float(input("Заряд частицы (с учётом знака, в элементарных зарядах): ")) / 6.242e+18
m = float(input("Масса частицы (в Атомарных Единицах Массы): ")) / 6.022e+26
v = float(input("Скорость частицы (в Метрах в Секунду): "))
v_angle = float(input("Угол вхождения частицы в поле: "))
b = float(input("Индукция магнитного поля (в Теслах): "))
b_angle = float(input("Угол вектора магнитной индукции (в Градусах): "))
e = float(input("Сила электрического поля (в Ньютонах на Метр): "))
e_angle = float(input("Угол силы электрического поля (в Градусах): "))
time_lim = float(input("Лимит времени симуляции (в Секундах): "))
time_step = float(input("Шаг времени симуляции (в Миллисекундах): ")) / 1000

# заполнение массивов симуляции
x = [0] * int(time_lim // time_step + 1)
y = x
for i in range(1, len(x)):
    x[i] = calculate_trajectory(q, m, e, e_angle, b, b_angle, v, v_angle, time_step, x[i - 1], y[i - 1],)[0]
    y[i] = calculate_trajectory(q, m, e, e_angle, b, b_angle, v, v_angle, time_step, x[i - 1], y[i - 1],)[1]
    v_angle = calculate_trajectory(q, m, e, e_angle, b, b_angle, v, v_angle, time_step, x[i - 1], y[i - 1],)[2]

# перевод массивов в необходимый для библиотеки тип данных
x = np.asarray(x)
y = np.asarray(y)

# построение графика
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Траектория движения заряженной частицы')
plt.grid(True)
plt.show()
