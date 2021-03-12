import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go


random_x = np.random.randint(1, 101, 100)
random_y = random_x  + np.random.randint(0,25,100)



data = [go.Scatter(name='Scatter', x=random_x, 
                    y=random_y, 
                    mode='markers',
                    marker=dict(
                        size=12,
                        color='rgb(51,204,153)',
                        symbol='pentagon',
                        line={'width':2}
                    )), go.Scatter(name='Lines', x=np.linspace(0,101,100), 
                    y=np.linspace(0,101,100)  + np.random.randint(0,25,100), 
                    mode='lines',
                    marker=dict(
                        color='rgb(200,204,153)',
                    ))]
                    
layout = go.Layout(title='First plot',
                    xaxis={'title':'My X axis'},
                    yaxis=dict(title='My Y axis'),
                    hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='temp-plot.html')