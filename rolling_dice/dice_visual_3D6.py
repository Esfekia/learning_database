from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

#Create three D6 dice.
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

#Make some rolls and store results in a list.
results =[]
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)

#Analyze the results.
frequencies = []
max_result = die_1.num_sides+die_2.num_sides+die_3.num_sides
for value in range(3,max_result+1):
	frequency= results.count(value)
	frequencies.append(frequency)

#Visualize the results.
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title="Results of rolling three D6 dice 1,000 times",
	xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data':data, 'layout': my_layout}, filename ='3d6.html')