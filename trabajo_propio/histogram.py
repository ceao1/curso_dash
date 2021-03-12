import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv('/home/carlos/Documentos/curso_dash/Data/abalone.csv')

data = [go.Histogram(x=df['length'], xbins=dict(
                                                start=0,
                                                end=1,
                                                size=0.02
                                                ))]

pyo.plot(data)