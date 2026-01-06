import numpy as np
import matplotlib.pyplot as plt

v0 = 30             #initial velocity (m/s)
g = 9.81            #gravity
ang = 45            #launch angle


ang_rad = np.radians(ang)

t = np.linspace(0, 3, 300)
x = v0 * np.cos(ang) * t 
y = v0 * np.sin(ang) * t - 0.5 * g * t**2

plt.figure()
plt.plot(x, y)
plt.grid()
plt.xlabel("Horizontal distance (m)")
plt.ylabel("Vertical height (m)")
plt.title("Projectile motion without air resistance")

plt.savefig("plots/trajectory_basic_without_air_res.png")
plt.tight_layout()
plt.show()
