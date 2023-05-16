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
        return math.degrees(math.atan(vx / vy))


# предупреждение
print("Не рекомендуется вводить очень маленькие (<0.001) и очень большие (>1000) данные, из-за проблем с "
      "производительностью python в вычислениях больших значений")
filler()
_ = input("С предупреждением ознакомлен, несу ответственность за своё железо (ввести любой символ): ")
filler()

# параметры на ввод
q = float(input("Заряд частицы (с учётом знака, в элементарных зарядах): ")) / 6.242e+18
m = float(input("Масса частицы (в КилоДальтонах): ")) / 6.022e+26
v = float(input("Скорость частицы (в Метрах в Секунду): "))
v_angle = float(input("Угол вхождения частицы в поле: "))
b = float(input("Индукция магнитного поля (в Теслах): "))
b_direct = float(input("Направление вектора магнитной индукции (1 на наблюдателя, 0 от наблюдателя): "))
e = float(input("Сила электрического поля (в Ньютонах на Метр): "))
e_angle = float(input("Угол силы электрического поля (в Градусах): "))
time_lim = float(input("Лимит времени симуляции (в Секундах): "))
time_step = float(input("Шаг времени симуляции (в Секундах): "))

# заполнение массивов симуляции
x = [0] * int(time_lim // time_step + 1)
y = x

# расчёт симуляции
for i in range(1, len(x)):
    # Вычисление векторных единиц
    e_x = e * math.cos(math.radians(e_angle))
    e_y = e * math.sin(math.radians(e_angle))
    v_x = v * math.cos(math.radians(v_angle))
    v_y = v * math.sin(math.radians(v_angle))

    # Вычисление сил
    if b_direct == 0:  # от нас
        f_x = q * e_x + q * v_y * b
    else:  # к нам
        f_x = q * e_x - q * v_y * b
    f_y = q * e_y + q * v_x * b

    # Вычисление ускорений
    a_x = f_x / m
    a_y = f_y / m

    # Вычисление новых координат
    x[i] = x[i - 1] + v_x * time_step + a_x * (time_step ** 2) / 2
    y[i] = y[i - 1] + v_y * time_step + a_y * (time_step ** 2) / 2

    # Вычисление новых скоростей
    v_x = v_x + a_x * time_step
    v_y = v_y + a_y * time_step

    # Вычисление нового угла
    v_angle = check(v_x, v_y)

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
