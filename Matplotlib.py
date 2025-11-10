import numpy as np
import matplotlib.pyplot as plt

from matplotlib.image import imread

#简单图像
x = np.arange(0,6,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()

# 利用pyplot添加图例和标题
x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
# 画图
plt.plot(x,y1,label="sin")
plt.plot(x,y2,linestyle='--',label="cos")
plt.xlabel("x")#横轴标签
plt.ylabel("y")#纵轴标签
#图标
plt.title('sin & cos')
plt.legend()
# 显示
plt.show()

# 显示图像
img = imread(r'D:\Users\12700\Desktop\图片风格融合.png')
plt.imshow(img)

plt.show()