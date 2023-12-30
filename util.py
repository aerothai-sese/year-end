import plotly.graph_objects as go
import numpy as np
import calendar
import pandas as pd

def create_traffic(data):
	title = "Traffic year-end summary."
	labels = ['2021','2022','2023']
	colors = ['rgb(67,67,67)', 'rgb(115,115,115)', 'rgb(49,130,189)']
	
	mode_size = [6, 6, 8]
	line_size = [1, 1, 4]
	
	months = calendar.month_name[1:]
	months.append("")

	x_data = months
	y_data = np.array([
	    data['traffic']['2021'],
	    data['traffic']['2022'],
	    data['traffic']['2023']
	])

	fig = go.Figure()

	for i in range(0, 3):
	    fig.add_trace(go.Scatter(x=x_data, y=y_data[i], mode='lines',line_shape='spline',
	        name=labels[i],
	        line=dict(color=colors[i], width=line_size[i]),
	        connectgaps=True,
	    ))

	    # endpoints
	    fig.add_trace(go.Scatter(
	        x=x_data,
	        y=y_data[i],
	        mode='markers',
	        marker=dict(color=colors[i], size=mode_size[i])
	    ))

	fig.update_layout(
	    xaxis=dict(
	        showline=True,
	        showgrid=False,
	        showticklabels=True,
	        linecolor='rgb(204, 204, 204)',
	        linewidth=2,
	        ticks='outside',
	        tickfont=dict(
	            family='monospace',
	            size=12,
	            color='rgb(82, 82, 82)',
	        ),
	    ),
	    yaxis=dict(
	        showline=True,
	        showgrid=False,
	        showticklabels=True,
	        linecolor='rgb(204, 204, 204)',
	        linewidth=2,
	        ticks='outside',
	        tickfont=dict(
	            family='monospace',
	            size=12,
	            color='rgb(82, 82, 82)',
	        ),
	    ),
	    autosize=False,
	    margin=dict(
	        autoexpand=False,
	        l=100,
	        r=50,
	        t=110,
	    ),
	    showlegend=False,
	    plot_bgcolor='white'
	)

	fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',
                      paper_bgcolor='rgba(0, 0, 0, 0)',)
	annotations = []
	for y_trace, label, color in zip(y_data, labels, colors):
	    # labeling the left_side of the plot
	    annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
	                                  xanchor='right', yanchor='middle',
	                                  text=label,
	                                  font=dict(family='monospace',
	                                            size=12),
	                                  showarrow=False))
	    # labeling the right_side of the plot
	    annotations.append(dict(xref='paper', x=0.95, y=y_trace[11],
	                                  xanchor='left', yanchor='middle',
	                                  text=' {}'.format(sum(y_trace)),
	                                  font=dict(family='monospace',
	                                            size=16),
	                                  showarrow=False))
	# Title
	annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
	                              xanchor='left', yanchor='bottom',
	                              text='Year-End traffic review',
	                              font=dict(family='monospace',
	                                        size=30,
	                                        color='rgb(255,255,255)'),
	                              showarrow=False))

	annotations.append(dict(xref='paper', yref='paper', x=0.9, y=1.0,
	                              xanchor='left', yanchor='bottom',
	                              text='Total traffic',
	                              font=dict(family='monospace',
	                                        size=14,
	                                        color='rgb(150,150,150)'),
	                              showarrow=False))

	# Source
	annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
	                              xanchor='center', yanchor='top',
	                              text='Source: TMCS jade database',
	                              font=dict(family='monospace',
	                                        size=12,
	                                        color='rgb(150,150,150)'),
	                              showarrow=False))
	fig.update_layout(annotations=annotations)


	return fig


def create_operator(data):
	colors = ['lightslategray',] * 10
	colors[0] = 'crimson'

	fig = go.Figure(data=[go.Bar(
	    x=list(data['operator'].keys()),
	    y=list(data['operator'].values()),
	    marker_color=colors # marker color can be a single color value or an iterable
	)])
	fig.update_layout(xaxis=dict(showgrid=False),
	              yaxis=dict(showgrid=True)
	)

	annotations = []

	annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
	                              xanchor='left', yanchor='bottom',
	                              text='Top 5 airline operator',
	                              font=dict(family='monospace',
	                                        size=30,
	                                        color='rgb(255,255,255)'),
	                              showarrow=False))

	# Source
	annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
	                              xanchor='center', yanchor='top',
	                              text='Airline Name',
	                              font=dict(family='monospace',
	                                        size=12,
	                                        color='rgb(150,150,150)'),
	                              showarrow=False))

	annotations.append(dict(xref='paper', yref='paper', x=-0.05, y=0.6,
	                        textangle=-90,
	                              xanchor='center', yanchor='top',
	                              text='Number of flight',
	                              font=dict(family='monospace',
	                                        size=12,
	                                        color='rgb(150,150,150)'),
	                              showarrow=False))


	annotations.append(dict(xref='paper', yref='paper', x=0.5, y=0.9,
	                              xanchor='center', yanchor='top',
	                              text="AIQ is the winner !!",
	                              font=dict(family='monospace',
	                                        size=16,
	                                        color='rgb(255,255,255)'),
	                              showarrow=False))

	fig.update_layout(annotations=annotations)
	return fig


def create_aircraft(data):

	colors = ['lightslategray',] * 10
	colors[0] = 'darkgreen'

	fig = go.Figure(data=[go.Bar(
	    x=list(data['aircraft_type'].keys()),
	    y=list(data['aircraft_type'].values()),
	    marker_color=colors # marker color can be a single color value or an iterable
	)])
	fig.update_layout(xaxis=dict(showgrid=False),
	              yaxis=dict(showgrid=True)
	)

	annotations = []

	annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
	                              xanchor='left', yanchor='bottom',
	                              text='Top 5 aircraft type',
	                              font=dict(family='monospace',
	                                        size=30,
	                                        color='rgb(255,255,255)'),
	                              showarrow=False))

	# Source
	annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
	                              xanchor='center', yanchor='top',
	                              text='Aircraft type.',
	                              font=dict(family='monospace',
	                                        size=12,
	                                        color='rgb(150,150,150)'),
	                              showarrow=False))

	annotations.append(dict(xref='paper', yref='paper', x=-0.05, y=0.6,
	                        textangle=-90,
	                              xanchor='center', yanchor='top',
	                              text='Number of aircraft type',
	                              font=dict(family='monospace',
	                                        size=12,
	                                        color='rgb(150,150,150)'),
	                              showarrow=False))


	annotations.append(dict(xref='paper', yref='paper', x=0.5, y=0.9,
	                              xanchor='center', yanchor='top',
	                              text="A320 ! (As we thought)",
	                              font=dict(family='monospace',
	                                        size=16,
	                                        color='rgb(255,255,255)'),
	                              showarrow=False))

	fig.update_layout(annotations=annotations)
	return fig

def create_sector(data,control):
	no = np.arange(1,6)
	sector = data['sector_rank'][control]
	df = pd.DataFrame({"Rank":no,"sector":sector})
	#df = df.reset_index(drop=True)
	return df


def create_movement(data):
	import plotly.express as px 
	labels = ['Overfly', 'Inbound', 'Outbound', 'Domestic']
	values = list(data['movement_type'].values())
	fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0, 0.2, 0],textinfo='label+percent',marker_colors=px.colors.sequential.RdBu)])
	
	return fig

def create_airport(data):
	Airport = ["VTBS","VTBD","VTSP", "VTCC","VTSM"]
	y_data_dep = [int(i) for i in data['airport_ranking']['adep']]
	y_data_des = [int(i) for i in data['airport_ranking']['ades']]

	fig = go.Figure(data=[
	    go.Bar(name='Departure', x=Airport, y=y_data_dep,
	          marker_color='rgb(55, 83, 109)'),
	    go.Bar(name='Arrival', x=Airport, y=y_data_des,
	          marker_color='rgb(26, 118, 255)')
	])

	fig.update_layout(barmode='stack',bargap=0.3,
	        legend=dict(
	        x=.8,
	        y=1.0,
	        bgcolor='rgba(255, 255, 255, 0)',
	        bordercolor='rgba(255, 255, 255, 0)'
	    ),)
	anno = []
	anno.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
	                              xanchor='left', yanchor='bottom',
	                              text='Top 5 hottest airport.',
	                              font=dict(family='monospace',
	                                        size=30,
	                                        color='rgb(255,255,255)'),
	                              showarrow=False))
	fig.update_layout(annotations=anno)
	return fig
