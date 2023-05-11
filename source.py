import matplotlib.pyplot as plt
import numpy as np


# заполнялка отступов
def filler():
    print()
    print()
    print()
    print()
    print()


def calculate_trajectory(q_ct, m_ct, e_ct, b_ct, v0_ct, t_ct):
    x0, y0 = 0.0, 0.0  # начальные координаты
    vx0, vy0 = v0_ct  # начальные скорости по осям

    # Расчет ускорений
    ax = (q_ct / m_ct) * (e_ct[0] + v0_ct[0] * b_ct[0])
    ay = (q_ct / m_ct) * (e_ct[1] + v0_ct[1] * b_ct[1])

    # Расчет координат в зависимости от времени
    x_ct = x0 + vx0 * t_ct + 0.5 * ax * t_ct ** 2
    y_ct = y0 + vy0 * t_ct + 0.5 * ay * t_ct ** 2

    return x_ct, y_ct


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
b = float(input("Индукция магнитного поля (в Теслах): "))
B_angle = float(input("Угол вектора магнитной индукции (в Градусах): "))
e = float(input("Сила электрического поля (в Ньютонах на Кулон): "))
E_angle = float(input("Угол силы электрического поля (в Градусах): "))
time_lim = float(input("Лимит времени симуляции (в Секундах): "))

# пересчёт значений в векторные, для удобства хранения
e = np.array([e * np.cos(np.deg2rad(E_angle)), e * np.sin(np.deg2rad(E_angle))])  # [Ex, Ey]
b = np.array([b * np.cos(np.deg2rad(B_angle)), b * np.sin(np.deg2rad(B_angle))])  # [Bx, By]
v0 = np.array([v * np.cos(np.deg2rad(v_angle)), v * np.sin(np.deg2rad(v_angle))])  # начальная скорость [v0x, v0y]
filler()

t = np.linspace(0, time_lim, 100)  # шаги времени, как массив

x, y = calculate_trajectory(q, m, e, b, v0, t)

# построение графика
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Траектория движения заряженной частицы')
plt.grid(True)
plt.show()
