#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# Launch the application:
app = dash.Dash()

# Create a DataFrame from the .csv file:
# df = pd.read_csv('Data/input/OldFaithful.csv')
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [20, 10, 30, 25, 22, 35, 66, 45, 67, 55]

# Create a Dash layout that contains a Graph component:
app.layout = html.Div([
    dcc.Graph(
        id='old_faithful',
        figure={
            'data': [
                go.Scatter(
                    x=X,
                    y=Y,
                    mode='lines+markers'
                )
            ],
            'layout': go.Layout(
                title='Old Faithful Eruption Intervals v Durations',
                xaxis={'title': 'Duration of eruption (minutes)'},
                yaxis={'title': 'Interval to next eruption (minutes)'},
                hovermode='closest'
            )
        }
    )
])

# Add the server clause:
if __name__ == '__main__':
    app.run_server()
