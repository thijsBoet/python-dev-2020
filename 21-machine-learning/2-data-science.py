import pandas as pd

# 1 - Import the data
data_frame = pd.read_csv('fifa19.csv')

# 2 - Clean the data
df1 = pd.DataFrame(data_frame, columns=['Name', 'Wage', 'Value'])

def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0

wage = df1['Wage'].replace('[\€,]', '', regex=True).apply(value_to_float)
value = df1['Value'].replace('[\€,]', '', regex=True).apply(value_to_float)

df1['Wage'] = wage
df1['Value'] = value

df1['difference'] = df1['Value'] - df1['Wage']
df1.sort_values('difference', ascending=False)

import seaborn as sns
sns.set()

graph = sns.scatterplot(x='Wage', y='Value', data=df1)
graph

from bokeh.plotting import figure, show
from bokeh.models import HoverTool

hover = HoverTool(tooltips=[
    ("index", "$index"),
    ("(Wage, Value)", "(@Wage, @Value)"),
    ("Name", "@Name"),
])

p = figure(title="Soccer 2019", x_axis_label='Wage', y_axis_label='Value', plot_width=1000, plot_height=1000, tools=[hover])
p.circle('Wage', 'Value', size=10, source=df1)
show(p)

# 3 - Split data in Training Set/Test Set
# 4 - Create/Import a Model
# 5 - Check the output
# 6 - Improve

# returns tuple with (rows, columns)
data_frame.shape

# Summary statistics for numerical columns
data_frame.describe()

# returns all values in an array
data_frame.values

# filters players over 40
data_frame[data_frame["Age"]>40].head()