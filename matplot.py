# Simple graph plotting using matplotlib
import matplotlib.pyplot as plt # pyright: ignore[reportMissingModuleSource]

x = [1, 2, 3, 4, 5]
y = [0, 12, 5, 18 ,45]

plt.plot(x, y, maker='o')
         
plt.show()