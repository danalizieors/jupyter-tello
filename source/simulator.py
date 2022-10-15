import plotly.graph_objs as go

x=[0, 0, 50, 50, 50]
y=[0, 0, 0, 50, 50]
z=[0, 81, 81, 81, 0]

def simulate(drone):
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
            'opacity': 0.8,
            'color': 'pink'
        },
    
    )

    trace2 = go.Mesh3d(
        # 8 vertices of a cube
            x=[-100, -100, 100, 100],
            y=[-100, 100, 100, -100],
            z=[0, 0, 0, 0],
            colorscale='algae',
            # Intensity of each vertex, which will be interpolated and color-coded
            intensity = [1, 0, 0, 1],
            # i, j and k give the vertices of triangles
            i = [0, 0],
            j = [1, 2],
            k = [2, 3],
            hoverinfo='skip',
            opacity=0.80
    )

    # Configure the layout.
    layout = {}

    data = [trace1, trace2]

    plot_figure = go.Figure(data=data, layout=layout)
    plot_figure.update_layout(
        scene = dict(
            xaxis = dict(visible=False),
            yaxis = dict(visible=False),
            zaxis = dict(visible=False),
            camera_eye = {"x": 0, "y": -1, "z": 0.5},
            )
        )

    # Render the plot.
    plot_figure.show()
