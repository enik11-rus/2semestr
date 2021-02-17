import matplotlib.pyplot as plt
import numpy as np


def my_func(x, a, b, c):
    '''
    y = a*x**2 + b*x + c
    '''
    return a*x**5 + b*x + c


styles = plt.style.available
plt.style.use(styles[6])

a = -5; b = 20; c = 10

left = -10; right = 0; step = .01
data_x = np.arange(left, right, step)
data_y = [my_func(x, a, b, c) for x in data_x]
plt.plot(data_x, data_y, linewidth=3, color='#FF0000')

a = 5; b = 20; c = 10
left = 0; right = 10; step = .01
data_x = np.arange(left, right, step)
data_y = [my_func(x, a, b, c) for x in data_x]
plt.plot(data_x, data_y, linewidth=3, color='#FF0000')


plt.title("График функции")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.grid(True)
plt.axhline(linewidth=2, color='#000000')
plt.axvline(linewidth=2, color='#000000')


plt.show()
