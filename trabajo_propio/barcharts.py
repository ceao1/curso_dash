import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


df = pd.read_csv('/home/carlos/Documentos/curso_dash/Data/2018WinterOlympics.csv')


gold = go.Bar(x=df['NOC'],
                y=df['Gold'],
                name='Gold',
                marker=dict(
                    color='rgb(218,165,32)'
                ))

silver = go.Bar(x=df['NOC'],
                y=df['Silver'],
                name='Silver',
                marker=dict(
                    color='rgb(208,210,209)'
                ))

bronze = go.Bar(x=df['NOC'],
                y=df['Bronze'],
                name='Bronze',
                marker=dict(
                    color='rgb(128,74,0)'
                ))

data = [gold, silver, bronze]
            
layout = go.Layout(title='Total Medals',
                    xaxis=dict(
                        title='Countries'
                    ),
                    yaxis=dict(
                        title='Quantity of medals'
                    ),
                    barmode='stack')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
