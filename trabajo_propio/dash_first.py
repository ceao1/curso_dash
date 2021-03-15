import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
                                html.H1('Hello Dash!', style={'textAlign':'center',
                                                              'color':'rgb(200,0,0)'}),
                                html.Div('Dash: Web dashboards using python'),
                                dcc.Graph(id='example',
                                          figure={'data':[
                                            {'x':[1,2,3], 'y':[4,1,5], 'type':'bar', 'name':''}
                                          ],
                                                  'layout':{
                                                      'title':'Bar chart!'
                                                  }})     
])

if __name__ == '__main__':
    app.run_server()