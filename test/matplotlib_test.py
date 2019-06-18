from pylab import mpl
import matplotlib.pyplot as plt

import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# x = [5, 8, 10]
# y = [12, 16, 6]
# plt.bar(x, y, align='center')
# plt.title('标题')
# plt.ylabel('Y 轴')
# plt.xlabel('X 轴')
# plt.show()

# 计算正弦曲线上点的 x 和 y 坐标
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.title("sine wave form")
# 使用 matplotlib 来绘制点
plt.plot(x, y)
plt.show()
