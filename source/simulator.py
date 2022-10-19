import math 
import plotly.graph_objs as go

from utils import toRadians

layout = {
    'height': 400,
    'margin': {
        'l': 10,
        'r': 10,
        'b': 10,
        't': 20,
    },
    'scene': {
        'aspectmode': 'data',
        'camera_eye': {
            'x': -0.2,
            'y': -1.8,
            'z': 0.5,
        },
        'xaxis': {
            'visible': False,
        },
        'yaxis': {
            'visible': False,
        },
        'zaxis': {
            'visible': False,
        },
    },
}

colorscale = 'hsv'
photo_angle = 12
photo_range = 100

def simulate(drone):
    width, length = drone.ground
    
    ground = go.Mesh3d(
        x = [0, 0, width, width],
        y = [0, length, length, 0],
        z = [0, 0, 0, 0],
        i = [0, 0],
        j = [1, 2],
        k = [2, 3],
        colorscale = 'solar',
        cmin = 0,
        cmax = 1,
        intensity = [0.6, 0.8, 0.8, 0.6],
        showscale = False,
        hoverinfo = 'skip',
    )
    
    xs = [state[0] for state in drone.history]
    ys = [state[1] for state in drone.history]
    zs = [state[2] for state in drone.history]
    angles = [state[3] for state in drone.history]
    
    path = go.Scatter3d(
        x = xs,
        y = ys,
        z = zs,
        customdata = angles,
        mode = 'lines+markers',
        marker = {
            'size': 10,
            'colorscale': colorscale,
            'cmin': 0,
            'cmax':  360,
            'color': angles,
            'line': {
                'width': 2,
                'color': 'black',
            },
        },
        line = {
            'color': 'black',
        },
        opacity = 0.5,
        showlegend = False,
        hovertemplate = 'x: %{x}<br>y: %{y}<br>z: %{z}<br>a: %{customdata}<extra></extra>',
    )
    
    scale = go.Mesh3d(
        x = [0],
        y = [0],
        z = [0],
        i = [0],
        j = [0],
        k = [0],
        colorscale = colorscale,
        cmin = 0,
        cmax = 360,
        intensity = [0],
        hoverinfo = 'skip',
    )
    
    xs_photos = sum([[state[0], state[0] + math.sin(toRadians(state[3])) * photo_range, None] for state in drone.photos], [])
    ys_photos = sum([[state[1], state[1] + math.cos(toRadians(state[3])) * photo_range, None] for state in drone.photos], [])
    zs_photos = sum([[state[2], state[2] - math.sin(toRadians(photo_angle)) * photo_range, None] for state in drone.photos], [])
    angles_photos = sum([[state[3], '#ffffff', state[3]] for state in drone.photos], [])
    
    photos = go.Scatter3d(
        x = xs_photos,
        y = ys_photos,
        z = zs_photos,
        mode = 'lines',
        line = {
            'width': 8,
            'colorscale': colorscale,
            'cmin': 0,
            'cmax':  360,
            'color': angles_photos,
        },
        showlegend = False,
        hovertemplate = 'x: %{x}<br>y: %{y}<br>z: %{z}<extra></extra>',
    )

    data = [ground, path, scale, photos]

    figure = go.Figure(
        data = data,
        layout = layout,
    )

    figure.show()
