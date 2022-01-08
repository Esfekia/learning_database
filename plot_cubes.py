import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**3 for x in x_values]
plt.style.use ('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter (x_values, y_values, c=y_values,cmap=plt.cm.YlOrRd, s=2)

#Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize =36)
ax.set_xlabel("Value", fontsize =18)
ax.set_ylabel("Cube of Value", fontsize =18)
ax.tick_params(axis ='both', which = "major", labelsize = 14)

#Set the range for each axis.
ax.axis ([0,1100,0, 1100000000])

plt.savefig('cubes_plot.png', bbox_inches = 'tight')
plt.show()
