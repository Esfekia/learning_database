import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Keep making new walks, as long as the program is active.
while True:

	#Make a random walk.
	rw =RandomWalk(100_000)
	rw.fill_walk()

	#Plot the points in the walk.
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(10,6), dpi=144)
	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap =plt.cm.Blues, 
		edgecolors ='none', s=1)

	#Mark the starting and ending points.
	ax.scatter(0,0, c ='green', edgecolors ='none', s=10)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red',edgecolors ='none', s=10)
	
	#Remove the axes.
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
	plt.show()

	keep_running = input("Make another random walk?(y/n)")
	if keep_running == 'n':
		break