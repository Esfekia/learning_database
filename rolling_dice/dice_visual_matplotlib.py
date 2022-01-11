import matplotlib.pyplot as plt
from die import Die

#Create two D6 dice.
die_1 = Die()
die_2 = Die()

#Make somre rolls and store results in a list.
results =[]
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

#Visualize the results.
x_values = range(2, max_result+1)
y_values = [frequencies]
plt.style.use('_mpl-gallery')
# plot:
fig, ax = plt.subplots()

ax.hist(x_values, bins=8, linewidth=0.5, edgecolor="white")

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 56), yticks=np.linspace(0, 56, 9))

plt.show()



