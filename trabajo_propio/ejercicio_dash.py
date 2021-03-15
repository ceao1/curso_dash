import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


app = dash.Dash()

datos = pd.read_csv('/home/carlos/Documentos/curso_dash/Data/OldFaithful.csv')


app.layout = html.Div(children=[
                                html.H1('Dashboard para ejercicio'),
                                dcc.Graph(id='primer_grafica',
                                          figure={'data':[
                                                            go.Scatter(name='Primero',
                                                                       x=datos['X'],
                                                                       y=datos['Y'],
                                                                       mode='markers',
                                                                       marker={'size':10,
                                                                                'symbol':'pentagon'
                                                                               }
                                                                      )
                                                         ],

                                                  'layout': go.Layout(title='Titulo del Dashboard',
                                                                      xaxis={'title':'Eje X',
                                                                            },
                                                                      yaxis={'title':'Eje Y',
                                                                            },
                                                                     )
                                                 }

                                         )
                                

                                ]
                      )






if __name__ == '__main__':
    app.run_server()