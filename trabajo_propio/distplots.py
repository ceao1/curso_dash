import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.figure_factory as ff
import numpy as np



x = np.random.randn(1000)
x1 = x + 10
x2 = x - 10

hist_data = [x, x1, x2]

data = ff.create_distplot(hist_data, ['x','x1','x2'], bin_size=[0.2, 0.5, 1])

pyo.plot(data)