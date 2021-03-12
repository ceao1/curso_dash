import plotly.offline as pyo
import plotly.graph_objs as go

y = [1,14,14,10,5,20,55,57,5,12,13,11,8,9,10]

y2 = [25,12,5,18,52,32,12,26,95,78,12,13,14,15,17,18,-50]
data = [go.Box(y=y,
                name='y',
                boxpoints='outliers',
                pointpos=0,
                jitter=0.07),
                
                go.Box(y=y2,
                name='y2',
                boxpoints='outliers',
                pointpos=0,
                jitter=0.07)]
pyo.plot(data)