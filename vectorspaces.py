import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([1,2])
v2 = np.array([3,1])
v3 = np.array([2,4])

vectors = [v1, v2, v3]
colors = ["red", "blue", "green"]
labels = ["v1", "v2", "v3"]

plt.figure(figsize=(7,7))
plt.axhline(0, color = "gray", linewidth = 0.3)
plt.axvline(0, color = "gray", linewidth = 0.3)

for vec, color, label in zip(vectors, colors, labels):
    plt.quiver(0,0, vec[0], vec[1], angles= "xy", scale_units= "xy",scale =1 ,color = color, label = label )

vec_sum = v1 + v2 + v3
plt.quiver(0,0, vec_sum[0], vec_sum[1], angles = "xy", scale_units = "xy", scale = 1, color = "yellow", label = "vec_sum" )
plt.xlim(-5,7)
plt.ylim(-5,7)
plt.legend()
plt.grid()
plt.show()
