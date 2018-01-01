# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:46:00 2017

@author: Di LU
"""


#pip install dash==0.19.0  # The core dash backend
#pip install dash-renderer==0.11.1  # The dash front-end
#pip install dash-html-components==0.8.0  # HTML components
#pip install dash-core-components==0.14.0  # Supercharged components
#pip install plotly --upgrade  # Latest Plotly graphing library

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)