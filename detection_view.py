### 分割结果可视化

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

points = np.loadtxt('0013.txt')
skip = 5   # Skip every n points

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
point_range = range(0, points.shape[0], skip) # skip points to prevent crash
x = points[point_range, 0]
z = points[point_range, 1]
y = points[point_range, 2]
map_color = {35.0:'r', 32.0:'g', 31.0:'b', 33:'y'}
Label = points[point_range, -1]
Color = list(map(lambda  x: map_color[x], Label))

# map_maker = {-1:'o', 1:'v'}
# makers = list(map(lambda x:map_maker[x], Label))

ax.scatter(x,   # x
           y,   # y
           z,   # z
           c=Color, # height data for color
        #    cmap='Blues',
           marker="o")
ax.axis('scaled')  # {equal, scaled}
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('part_seg')
ax.axis('off')          # 设置坐标轴不可见
ax.grid(False)          # 设置背景网格不可见
plt.show()
