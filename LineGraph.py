import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
x = ['a', 'b', 'c']
y = [5000, 33, 1]
y2 = [23, 44, 66]
plt.plot(x, y, 'g', label = 'LineOne', linewidth = 1)
plt.plot(x, y2, 'b', label = 'LineTwo', linewidth = 1)
plt.title("Jatin fucks Minors")
plt.xlabel("Minor Name")
plt.ylabel("Axis")
plt.grid(True, color = 'k')
plt.legend()
plt.show()