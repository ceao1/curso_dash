import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

df = pd.read_csv('/home/carlos/Documentos/curso_dash/Data/2010YumaAZ.csv')

data = []

for day in df['DAY'].unique():
    temp=df[df['DAY']==day]
    trace = go.Scatter(x=temp['LST_TIME'],
                        y=temp['T_HR_AVG'],
                        mode='lines',
                        name=day
                        )
    data.append(trace)

layout = go.Layout(title='Avg by day and time',
                    xaxis={'title':'Time of day'},
                    yaxis={'title':'AVG temp'})

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)