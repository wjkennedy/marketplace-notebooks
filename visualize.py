# First, import the necessary libraries
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import pandas as pd
import pygal

# Next, read in your data from the CSV file
data = pd.read_csv("issues.csv")

# Use bokeh to create a scatter plot of the data
output_notebook()
p = figure()
p.scatter(data['date_last_commented'], data['priority'])
show(p)

# Use pygal to create a bar chart of the data
bar_chart = pygal.Bar()
bar_chart.add("Issues", data['project'].value_counts())
bar_chart.render_to_file("issues_by_project.svg")

