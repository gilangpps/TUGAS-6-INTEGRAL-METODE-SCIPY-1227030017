# -*- coding: utf-8 -*-
"""TUGAS 6 -Metode Integrasi Scipy_1227030017.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Md4oO6V1x1SpUj483wbmz4T0gKa8t_wm
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

#defisini batas
x_start = 0 #batas atas
x_stop = 1 #batas bawah
x_steps_interval = 1e-3 #ukuran langkah

#defisini array dari poin data
x_values = np.arange(x_start, x_stop, x_steps_interval)
y_values = 2 * x_values * np.exp(np.sin(x_values)) + np.cos(np.exp(x_values))

# lambda fungsi integral (doppelganger)
f = lambda x: 2 * x * np.exp(np.sin(x)) + np.cos(np.exp(x))

# hitung integral (abaikan error)
integral, _ = integrate.quad(f, x_start, x_stop)

# print hasil integral
print("Hasil integral:", integral)

# plotting kurva fungsi

plt.plot(x_values, y_values, label=r'$2xe^sin(x) +cos(e^x)$', color='red')
plt.fill_between(x_values, y_values, color='green', alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Kurva Fungsi 2x(e^sinx) + cos(e^x)')
plt.legend()
plt.grid(True)
plt.show()



import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

#defisini batas
x_start = 0 #batas atas
x_stop = 2 #batas bawah
x_steps_interval = 1e-3 #ukuran langkah

#defisini array dari poin data
x_values = np.arange(x_start, x_stop, x_steps_interval)
y_values = np.exp(-x_values**2)

# lambda fungsi integral (fungsi ideal)
f = lambda x: np.exp(-x**2)

# hitung integral (abaikan error)
integral, _ = integrate.quad(f, x_start, x_stop)

# print hasil integral
print("Hasil integral:", integral)

# plotting kurva fungsi
plt.plot(x_values, y_values, label=r'$e^{-x^2}$', color='black')
plt.fill_between(x_values, y_values, color='green', alpha=0.3)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Kurva Fungsi e^(-x^2)')
plt.grid(True)
plt.show()

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

#defisini batas
x_start = 0 #batas bawah
x_stop = np.radians(180) #batas atas
x_steps_interval = 1e-3 #ukuran langkah

#defisini array dari poin data
x_values = np.arange(x_start, x_stop, x_steps_interval)
y_values = (x_values ** 2)*np.cos(x_values) + 3*np.sin(2*x_values)

# lambda fungsi integral (doppelganger)
f = lambda x:(x ** 2)*np.cos(x) + 3*np.sin(2*x)

# hitung integral (abaikan error)
integral, _ = integrate.quad(f, x_start, x_stop)

# print hasil integral
print("Hasil integral:", integral)

# plotting kurva fungsi

plt.plot(x_values, y_values, label=r'$x^2 cos (x) + 3 sin (2x)$', color='red')
plt.fill_between(x_values, y_values, color='green', alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Kurva Fungsi x^2 cos (x) + 3 sin (2x))')
plt.legend()
plt.grid(True)
plt.show()