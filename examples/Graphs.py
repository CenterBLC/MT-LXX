# %% example of multi-y plot
import matplotlib.pyplot as plt

x1 = [0,1,2,3,4,5]
y1 = [0,1,4,9,16,25]      # quadratic
y2 = [0,1,2,3,4,5]        # linear
y3 = [0,10,100,1000,10000,100000]  # exponential

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()   # second y-axis
ax3 = ax1.twinx()   # third y-axis

# Offset the third axis to the right
ax3.spines["right"].set_position(("axes", 1.2))

ax1.plot(x1, y1, 'b-')
ax2.plot(x1, y2, 'g-')
ax3.plot(x1, y3, 'r-')

ax1.set_xlabel("X axis")
ax1.set_ylabel("y1 quadratic", color='b')
ax2.set_ylabel("y2 linear", color='g')
ax3.set_ylabel("y3 exponential", color='r')

plt.show()
