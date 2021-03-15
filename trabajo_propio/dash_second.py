import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np


app = dash.Dash()

np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = random_x + np.random.randint(1, 15, 100)

random_x2 = np.linspace(1,101,100)
random_y2 = random_x2 + np.random.randint(15, 30, 100)

app.layout = html.Div( [dcc.Graph(id='Scatterplot',
                                    figure= {'data':[
                                                    go.Scatter(x=random_x,
                                                                y=random_y,
                                                                mode='markers',
                                                                marker = {
                                                                          'size':8,
                                                                          'symbol':'pentagon'
                                                                          }
                                                                ),
                                                    go.Scatter(x=random_x2,
                                                                y=random_y2,
                                                                mode='lines',
                                                                marker = {
                                                                          'size':50
                                                                          }
                                                                )
                                                    ],
                                             'layout': go.Layout(title='Mi scatterplot')

                                    }),
                            html.H1('Hello Dash!', style={'textAlign':'center',
                                                          'color':'rgb(200,10,10)'
                                                          }),
                            html.P('Prueba de p')]


                        )


if __name__ == '__main__':
    app.run_server()