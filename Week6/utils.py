import plotly.io as pio
import plotly.graph_objects as go


def set_default():
    """
        Sets Dark Mode for Plotly Plots.
    """
    pio.templates.default = "plotly_dark"
    

def plot_clusters3d(X, labels, title='Clusters', xyz=['', '', '']):
    """
        Plots Clusters in 3D
        Input: 
            - X: 
                Pandas DataFrame with 3 columns
                Will visualize first 3 if more than 3 are given.
            - labels:
                Cluster number assigned by clustering algorithm.
            - title:
                Plot title.
            - xyz:
                Axis names.
        Returns:
            A 3D plot of type `plotly.graph_objs._figure.Figure`.
    """
    
    fig = go.Figure()

    fig.add_trace(go.Scatter3d(x=X.iloc[:,0],
                               y=X.iloc[:,1],
                               z=X.iloc[:,2],
                               mode='markers',
                               marker=dict(color=labels,
                                           size=20,
                                           line=dict(color=labels,
                                                     width=12),
                                           opacity=0.8)
                              )
                 )

    fig.update_layout(title=title,
                      scene=dict(xaxis=dict(title=xyz[0]),
                                 yaxis=dict(title=xyz[1]),
                                 zaxis=dict(title=xyz[2]))
                     )

    return fig