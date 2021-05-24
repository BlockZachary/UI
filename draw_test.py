# _*_coding:utf-8_*_
# Author： Zachary

import matplotlib.pyplot as plt
import numpy as np
# 生成数据
X, Y = np.meshgrid(np.linspace(0, 10, 1000), np.linspace(0, 10, 1000))
temperature = X + (Y - 5) ** 2

# 作图
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
c = ax.pcolormesh(X, Y, temperature, cmap='Spectral_r')
cb = fig.colorbar(c)
cb.set_label('Temperature')
plt.savefig("fig.png")
plt.show()
