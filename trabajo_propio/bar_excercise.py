import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('/home/carlos/Documentos/curso_dash/Data/mocksurvey.csv', index_col=0)
data = [go.Bar(y=df.index, x=df[response], name=response, orientation='h') for response in df.columns]

layout = go.Layout(title='Percent response for each question', barmode='stack')
fig= go.Figure(data=data, layout=layout)
pyo.plot(fig)