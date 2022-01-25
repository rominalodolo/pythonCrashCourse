
# 15.3 Molecular Motion
# Modify rw_visual.py by replacing plt.scatter() with plt.plot().
# To simulate the path of a pollen grain on the surface of a drop of water, pass in the
# rw.x_values and rw.y_values, and include a linewidth argument. Use 5000 instead of 50,000
# points.

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100, zorder=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100, zorder=2)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

# 15.4 Modified Random Walks
# In the RandomWalk class, x_step and y_step are generated
# from the same set of conditions. The direction is chosen randomly from the list [1, -1] and
# the distance from the list [0, 1, 2, 3, 4]. Modify the values in these lists to see what happens
# to the overall shape of your walks. Try a longer list of choices for the distance, such as 0
# through 8, or remove the –1 from the x or y direction list.


# 15.5 Refactoring
# The fill_walk() method is lengthy. Create a new method called
# get_step() to determine the direction and distance for each step, and then calculate the step.
# You should end up with two calls to get_step() in fill_walk():
# x_step = self.get_step()
# y_step = self.get_step()
# This refactoring should reduce the size of fill_walk() and make the method easier to read
# and understand.

# 15.6 Two D8s
#  Create a simulation showing what happens when you roll two eight-sided dice
# 1000 times. Try to picture what you think the visualization will look like before you run the
# simulation; then see if your intuition was correct. Gradually increase the number of rolls until
# you start to see the limits of your system’s capabilities.

# 15.7 Three Dice
#  When you roll three D6 dice, the smallest number you can roll is 3 and the
# largest number is 18. Create a visualization that shows what happens when you roll three D6
# dice.
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create three D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1_000_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results.
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 dice 1,000,000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='3d6.html')

# 15.8 Multiplication
# When you roll two dice, you usually add the two numbers together to
# get the result. Create a visualization that shows what happens if you multiply these numbers
# instead.
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1_000_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(
        title='Results of multiplying two D6 dice. (1,000,000 rolls)',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6*d6.html')

# 15.9
#  Die Comprehensions: For clarity, the listings in this section use the long form of for
# loops. If you’re comfortable using list comprehensions, try writing a comprehension for one or
# both of the loops in each of these programs.
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 dice.
die_1, die_2 = Die(), Die()

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]
    
# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]
    
# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')

# 15.10
#  Practicing with Both Libraries: Try using Matplotlib to make a die-rolling
# visualization, and use Plotly to make the visualization for a random walk. (You’ll need to
# consult the documentation for each library to complete this exercise.)