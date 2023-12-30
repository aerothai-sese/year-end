import streamlit as st
import json
from util import * 
import pandas as pd

f = open('./data.json')
data = json.load(f)

st.header("Year-End review")

st.subheader("Traffic summary")
st.write("""Traffic was extracted from local flight table in jade tmcs database to visualize the trend in past 3 years.
	Here you can check the number of flights across the Thailand ATM network.""")
st.write("Traffic has grown from 2022 ~ 43.47 %")
st.warning("""Disclaimer : Data maybe not correct 100% but you can see the trend line from each chart
	eg. rise in Aug and Mar but drop in Febr and Sep""")

with st.container(border=True):
	fig_traffic = create_traffic(data)
	st.plotly_chart(fig_traffic,use_container_width=True)

st.subheader("Airline operator")
st.write("This section will summarize top 5 of Airline operator in our ATM operation.")

with st.container(border=True):
	col1,col2 = st.columns(2)
	with col1:
		fig_operator = create_operator(data)
		st.plotly_chart(fig_operator,use_container_width=True )
	with col2:
		st.write("")
		st.write("")
		st.write("")
		st.write("")
		st.write("")
		st.write("")
		st.write("")
		st.image("./aiq.jpg",caption='AIQ numba wannnnnn.')

st.subheader("Aircraft type")
st.write("This section will summarize top 5 of aircraft type which is the most used in 2023.")
with st.container(border=True):
	col3,col4 = st.columns(2)
	with col3:
		fig_aircraft = create_aircraft(data)
		st.plotly_chart(fig_aircraft,use_container_width=True )
	with col4:
		st.write("")
		st.write("")
		st.write("")
		st.write("")
		st.write("")
		st.image("./a320.jpg",caption='source : https://en.wikipedia.org/wiki/Airbus_A320_family')


st.subheader("Airport ranking")
with st.container(border=True):
	fig = create_airport(data)
	st.plotly_chart(fig,use_container_width=True)

st.subheader("Movement type")
st.write("Domestic flight is the majority of movement type in Thailand ATM with 330,705 flight")

with st.container(border=True):
	fig = create_movement(data)
	st.plotly_chart(fig,use_container_width=True)


st.subheader("Most active sector.")
st.write("Ranking of control sector was sorted by aggregation time.")
with st.container(border=True):
	col1,col2,col3 = st.columns(3)
	with col1:
		st.write("En-route")
		df = create_sector(data,'area')
		st.dataframe(df,hide_index=True)

	with col2:
		st.write("Approach")
		df = create_sector(data,'app')
		st.dataframe(df,hide_index=True)
	with col3:
		st.write("Tower")
		df = create_sector(data,'twr')
		st.dataframe(df,hide_index=True)



st.snow()

st.divider()
with st.expander("About us."):
	st.write("""
		Aeronautical Radio of Thailand Ltd. (AEROTHAI) 
		is a state enterprise under the Ministry of Transport .
		It was founded in 1948 by airlines with the consent of 
		the Royal Thai Government to provide air traffic control 
		and aeronautical communication services for airline operations. 
		Later in 1963, the Government acquired the majority of 
		the Company's share capital from the founding airlines 
		thereby altering the Company's status to that of a State Enterprise.
		""")