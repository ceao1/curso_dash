import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np


df = pd.read_csv('/home/carlos/Documentos/curso_dash/Data/abalone.csv')

muestra1 = go.Box(y= np.random.choice(df['rings'], 30, replace=False))

muestra2 = go.Box(y= np.random.choice(df['rings'], 20, replace=False))


data = [muestra1, muestra2]
pyo.plot(data)