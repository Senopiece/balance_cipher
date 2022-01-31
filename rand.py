import matplotlib.pyplot as plt
import random

n = 100
slots = [0 for _ in range(n)]

for _ in range(1000):
    slots[int(random.betavariate(2, 2)*n)] += 1

plt.plot(slots)
plt.show()