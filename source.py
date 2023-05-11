import math
import matplotlib.pyplot as plt
import numpy as np


# заполнялка отсутупов
def filler():
    print()
    print()
    print()
    print()
    print()


def calculate_trajectory(q, m, E, B, v0, t):

    x0, y0 = 0.0, 0.0  # начальные координаты
    vx0, vy0 = v0  # начальные скорости по осям

    # Расчет ускорений
    ax = (q / m) * (E[0] + v0[0] * B[0])
    ay = (q / m) * (E[1] + v0[1] * B[1])

    # Расчет координат в зависимости от времени
    x = x0 + vx0 * t + 0.5 * ax * t**2
    y = y0 + vy0 * t + 0.5 * ay * t**2

    return x, y


# предупреждение
print("Не рекомендуется вводить очень маленькие (<0.001) и очень большие (>1000) данные, из-за проблем с "
      "производительностью python в вычислениях больших значений")
filler()
_ = input("С предупреждением ознакомлен, несу ответственность за своё железо (ввести любой символ): ")
filler()

# параметры на ввод
q = float(input("Заряд частицы (с учётом знака, Кулонах): "))
m = float(input("Масса частицы (в Килограммах): "))
v = float(input("Скорость частицы (в Метрах в Секунду): "))
v_angle = float(input("Угол вхождения частицы в поле: "))
B = float(input("Индукция магнитного поля (в Теслах): "))
B_angle = float(input("Угол вектора магнитной индукции (в Градусах): "))
E = float(input("Сила электрического поля (в Ньютонах на Кулон): "))
E_angle = float(input("Угол силы электрического поля (в Градусах): "))
time_lim = float(input("Лимит времени симуляции (в Секундах): "))

# пересчёт значений в векторные, для удобства хранения
E = np.array([E*math.cos(math.radians(E_angle)), E*math.sin(math.radians(E_angle))])  #[Ex, Ey]
B = np.array([B*math.cos(math.radians(B_angle)), B*math.sin(math.radians(B_angle))])  # [Bx, By]
v0 = np.array([v*math.cos(math.radians(v_angle)), v*math.sin(math.radians(v_angle))])  # начальная скорость [v0x, v0y]
filler()

t = np.linspace(0, time_lim, 100)  # шаги времени, как массив

x, y = calculate_trajectory(q, m, E, B, v0, t)

# построение графика
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Траектория движения заряженной частицы')
plt.grid(True)
plt.show()
