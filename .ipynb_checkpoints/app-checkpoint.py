import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

#Step 1. Launch Application
app = dash.Dash(__name__, external_stylesheets=None)

#Step 2. Import Data
vets = pd.read_csv('vets_coords.csv')
merged = pd.read_csv('merged_df_dash.csv')

#Step 3. Create Dropdown options
branches = merged['Branch'].unique()[:4]
branches= [{'label': val, 'value': val} for val in branches]
tribes = merged['Tribe'].unique()
tribes = [{'label': val, 'value': val} for val in tribes]


#Step 4. Create figure
fig = go.Figure(data=go.Scattergeo(
        locationmode = 'USA-states',
        lon = vets['longitude'],
        lat = vets['latitude'],
        text = vets['text'],
        mode = 'markers',
        hoverinfo='text',
        marker = dict(
            size = vets['scaled'],
            opacity = 0.8,
            reversescale = False,
            autocolorscale = False,
            symbol = 'circle',
            line = dict(
                width=0.5,
                color='rgb(40,40,40)'
            ),
            colorscale = 'portland',
            cmin = 0,
            color = vets['Combined'],
            cmax = vets['Combined'].max(),
            colorbar_title="# of Members"
        )))

fig.update_layout(
        title = 'Elite Meet National Distribution',
        title_font_family='Garamond',
        title_font_size=40,
        title_x=0.5,
        title_y=0.9,
        geo = dict(
            scope='usa',
            projection_type='albers usa',
            showland = True,
            landcolor = "rgb(217, 217, 217)",
            #subunitcolor = "rgb(217, 217, 217)",
            #countrycolor = "rgb(217, 217, 217)",
            countrywidth = 1.5,
            subunitwidth = 1.5
        )
    )

#Step 5. Create a Dash Layout
app.layout = html.Div([
    html.Div([
        html.Div([

        #Branch drop down menu
            html.P([
            html.Label("Branch", style={'fontfamily':'Garamond', 'fontSize': 20}),
            dcc.Dropdown(
                id='Branches',
                options=branches,
                value='Navy')
            ],
        style={'width': 200})
        ]),

        #Tribe drop down menu
        html.Div([
            html.P([
            html.Label("Tribe", style={'fontfamily':'Garamond', 'fontSize': 20}),
            dcc.Dropdown(
                id='Tribes',
                options=tribes,
                value='SEAL')
            ],
        style={'width': 200})
        ]),
    dcc.Graph(id='map', figure=fig, style={"height": 750}),
    ])
])

#Step 6. Create call back function
@app.callback(
    Output('map', 'figure'),
    [Input('Branches', 'value')]
)

def update_map(branch_name):
    #create data for updated map
    df = merged[merged['Branch'] == branch_name]
    grouped = df.groupby(['CityState', 'latitude', 'longitude'])['Id'].count().reset_index()

    #update new figure
    fig = go.Figure(data=go.Scattergeo(
        locationmode='USA-states',
        lon=grouped['longitude'],
        lat=grouped['latitude'],
        text=grouped['CityState'] + ': ' + str(grouped['Id']),
        mode='markers',
        hoverinfo='text',
        marker=dict(
            size=grouped['Id']/5,
            opacity=0.8,
            reversescale=False,
            autocolorscale=False,
            symbol='circle',
            line=dict(
                width=0.5,
                color='rgb(40,40,40)'
            ),
            colorscale='portland',
            cmin=0,
            color=grouped['Id'],
            cmax=grouped['Id'].max(),
            colorbar_title="# of Members"
        )))

    fig.update_layout(
        title='Elite Meet National Distribution',
        title_font_family='Garamond',
        title_font_size=40,
        title_x=0.5,
        title_y=0.9,
        geo=dict(
            scope='usa',
            projection_type='albers usa',
            showland=True,
            landcolor="rgb(217, 217, 217)",
            # subunitcolor = "rgb(217, 217, 217)",
            # countrycolor = "rgb(217, 217, 217)",
            countrywidth=1.5,
            subunitwidth=1.5
        )
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)