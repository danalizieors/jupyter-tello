import plotly.graph_objs as go

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
            'y': -1.80,
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

def simulate(drone):
    width, length = drone.ground
    
    ground = go.Mesh3d(
        x = [0, 0, width, width],
        y = [0, length, length, 0],
        z = [0, 0, 0, 0],
        i = [0, 0],
        j = [1, 2],
        k = [2, 3],
        colorscale = 'algae',
        cmin = 0,
        cmax = 1,
        intensity = [0.8, 0.2, 0.2, 0.8],
        opacity = 0.80,
        showscale = False,
        hoverinfo = 'skip',
    )
    
    xs = [state[0] for state in drone.history]
    ys = [state[1] for state in drone.history]
    zs = [state[2] for state in drone.history]
    angles = [state[3] for state in drone.history]
    
    trace1 = go.Scatter3d(
        showlegend=False,
        x=xs,  # <-- Put your data instead
        y=ys,  # <-- Put your data instead
        z=zs,  # <-- Put your data instead
        mode='lines+markers',
        marker={
            'size': 10,
            'color': 'pink'
        },
    
    )

    data = [trace1, ground]

    figure = go.Figure(
        data=data,
        layout=layout,
    )

    figure.show()
