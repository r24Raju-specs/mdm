i = 2
j = 1

N = i*i + i*j + j*j
print("Cluster Size =", N)

R = 2
D = np.sqrt(3*N) * R
print("Calculated minimum safe reuse distance (D):", round(D, 2))

tower_A = np.array([0, 0])

tower_B = np.array([
    i*np.sqrt(3)*R + j*np.sqrt(3)*R*0.5,
    j*3*R/2
])

tower_C = np.array([
    -j*3*R/2,
    i*np.sqrt(3)*R + j*np.sqrt(3)*R*0.5
])


towers = [tower_A, tower_B, tower_C]

def draw_hexa(x, y, r):
    hx = [
        x-r*0.866, x, x+r*0.866,
        x+r*0.866, x, x-r*0.866,
        x-r*0.866
    ]

    hy = [
        y+r*0.5, y+r, y+r*0.5,
        y-r*0.5, y-r, y-r*0.5,
        y+r*0.5
    ]

    plt.fill(
        hx, hy,
        color="lightgrey",
        edgecolor="black",
        linewidth=1.5
    )


for idx, tower in enumerate(towers):
    draw_hexa(tower[0], tower[1], R)

    plt.text(
        tower[0], tower[1],
        f"Tower {idx+1}",
        ha="center",
        va="center",
        fontsize=10
    )


plt.plot(
    [tower_A[0], tower_B[0]],
    [tower_A[1], tower_B[1]],
    "b--",
    linewidth=1.5,
    label=f"D = {D:.2f}"
)

plt.plot(
    [tower_A[0], tower_C[0]],
    [tower_A[1], tower_C[1]],
    "g--",
    linewidth=2
)

plt.scatter(
    [tower_A[0], tower_B[0], tower_C[0]],
    [tower_A[1], tower_B[1], tower_C[1]],
    color="red"
)

plt.title(f"Hexagonal Frequency Reuse (N = {N})")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()
