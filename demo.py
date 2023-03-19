import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import plotly.express as px

st.set_page_config(layout= 'wide')
data = pd.read_csv('Ecommerce_clean.csv')
st.title('Ecommerce Dataset Analysis')
st.dataframe(data.sample(5))

def clean_dataset(df):
  df1 = df[df['UnitPrice'] <= 50 ]
  df2 = df1[df1['Quantit'] <= 30]
  return df2
data = clean_dataset(data)

col1 , col2 = st.columns(2)
with col1:
    st.subheader('Which ( Minor Category / Major Category/Country) in Ecommerce dataset are more in demand?' )
    option = st.selectbox('selsect an option' , ['Minor Category','Major Category','Country'])
    fig = px.bar(data_frame= data[option].value_counts() , x = option ,  text_auto='0.2s')
    fig.update_traces(textfont_size = 12 , textposition = 'outside')
    fig.update_layout(width = 510)
    st.plotly_chart(fig)
    

    st.subheader('What is The Best Order value in Major Category?')
    fig = px.pie(data_frame= data , names =data.groupby('Major Category')['OrderValue'].sum().index
    , values = data.groupby('Major Category')['OrderValue'].sum().values ,
    hole=0.3)
    fig.update_layout(width = 500)
    st.plotly_chart(fig)

    st.subheader('Which year of Ecommerce are more in demand?' )
    fig = px.pie(data_frame= data , names =data.groupby('year')['OrderValue'].count().index
    , values = data.groupby('year')['OrderValue'].count().values )
    fig.update_layout(width = 500)
    st.plotly_chart(fig)


    st.subheader('What is the best (OrderValue /  Quantit /UnitPrice) in Country?' )
    options= st.radio(
    "selsect an option",
    ('OrderValue','Quantit','UnitPrice'))
    fig = fig = px.bar(data_frame= data , x = 'Country' , y = options)
    fig.update_layout(width = 500)
    st.plotly_chart(fig)


st.subheader('What is the Time of the day that contributes to high Quantit?')
fig = px.pie(data_frame=data , names =data.groupby('OrderTimeOfDay')['Quantit'].count().index
    , values = data.groupby('OrderTimeOfDay')['Quantit'].count().values)
st.plotly_chart(fig)

with col2:
    st.subheader('In which range (OrderValue /  Quantit) lies, what is distribution look like?')
    option = st.selectbox('selsect an option' , ['OrderValue','Quantit','UnitPrice'])
    fig = px.histogram(data_frame= data , x = option )
    st.plotly_chart(fig)

    st.subheader('What is The Best Quantit in Major Category?')
    fig = px.pie(data_frame= data , names =data.groupby('Major Category')['Quantit'].sum().index
    , values = data.groupby('Major Category')['Quantit'].sum().values ,
    hole=0.3)
    st.plotly_chart(fig)

    st.subheader(' How (order value / Quantit) is distributed over the months for each year?' )
    option = st.selectbox('selsect an option' , ['OrderValue','Quantit'])
    fig = px.bar(data_frame=data.groupby(['month', 'year']).mean()
    [option].reset_index() 
    , x = 'month', y = option , color='year' ,  text_auto='0.2s')
    fig.update_traces(textfont_size = 12 , textposition = 'outside')
    st.plotly_chart(fig)

    st.subheader('What Hour recives high demand for Quantit?' )
    fig = fig = px.bar(data_frame= data , x = 'Hour' , y = 'Quantit')
    st.plotly_chart(fig)
   



   



 
