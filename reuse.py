import numpy as np
import matplotlib.pyplot as plt

i, j, R = 2, 1, 2

N = i*i + i*j + j*j
D = np.sqrt(3*N) * R

print("Cluster Size =", N)
print("Reuse Distance =", round(D, 2))

A = np.array([0, 0])
B = np.array([i*3**0.5*R + j*3**0.5*R/2, j*3*R/2])
C = np.array([-j*3*R/2, i*3**0.5*R + j*3**0.5*R/2])

towers = [A, B, C]

for idx, (x, y) in enumerate(towers):
    hx = [x-R*0.866, x, x+R*0.866, x+R*0.866, x, x-R*0.866, x-R*0.866]
    hy = [y+R/2, y+R, y+R/2, y-R/2, y-R, y-R/2, y+R/2]

    plt.fill(hx, hy, color="lightgrey", edgecolor="black")
    plt.text(x, y, f"Tower {idx+1}", ha="center")

plt.plot([A[0], B[0]], [A[1], B[1]], "b--", label=f"D={D:.2f}")
plt.plot([A[0], C[0]], [A[1], C[1]], "g--")

plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color="red")
plt.title(f"Hexagonal Frequency Reuse (N={N})")
plt.axis("equal")
plt.grid()
plt.legend()
plt.show()
