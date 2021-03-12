import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv('/home/carlos/Documentos/curso_dash/Data/mpg.csv')

data = [go.Scatter(x=df['displacement'],
                    y=df['acceleration'],
                    text=df['name'],
                    mode='markers',
                    marker=dict(
                        size=df['weight']/200,
                        color=df['mpg'],
                        showscale=True
                    ))]

layout = go.Layout(title='Scatter plot', hovermode='closest')


fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)