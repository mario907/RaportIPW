import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

data = pd.read_excel('Pytania raport.xlsx')

st.set_page_config(page_title = 'LGBT and Refugee Rights in Europe - Conclusion', layout = 'wide', page_icon = 'ikona_uniwersytetu.png')
im1, im2, im3, im4, im5 = st.columns([1,1,1.15,1.5,1.5])
with im1:
    st.image('logo_fundacji.png')
with im2:
    st.image('logo_uniwersytetu.png')
st.markdown('<p style = "color:#420773; font-size:38px"><b>Conclusion</b></p>', unsafe_allow_html=True)
with im3:
    st.image('erasmus.png')
    
st.markdown('<div style="text-align: justify;">As we have seen, LGBT and refugee rights vary significantly across Europe, depending on the legal and social context of each country. While Germany is a role model for LGBT equality and inclusion as well as refugee support and protection, Poland and Bulgaria still have a long way to go to ensure the dignity and safety of their LGBT and refugee citizens. We hope that this article has helped you understand the differences and similarities between these three countries and has inspired you to take action for LGBT and refugee rights in your own community.<br/ >Presented graph contains the comparison between three described country. Each point is depended from the ampunt of supprotive answers to certain question. Question is visible by moving the cursor to the point or in the below the plot. The more supprotive for LGBT community the country is, the bigger the polygon on the graph is.</div>', unsafe_allow_html=True)

categories = data['Pytanie'].unique()
support = ['Support', 'Agree', 'Did not mention homosexuals', 'Justifable', 'Agree', 'Yes', 'Rare', 'Rare', 'Agree', 'Yes', 'Favor']
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
      r=data[data['Kraj']=='Germany']['Tak'],
      theta=categories,
      fill='toself',
      name='Germany',
    hovertemplate= '<b>Germany</b><br />%{theta}<br />Supportive answer: %{r:.0%}<extra></extra>',
    fillcolor='#420773',
    line = dict(color = '#420773'),
    opacity=0.75 
))

fig.add_trace(go.Scatterpolar(
      r=data[data['Kraj']=='Poland']['Tak'],
      theta=categories,
      fill='toself',
      name='Poland',
    hovertemplate= '<b>Poland</b><br />%{theta}<br />Supportive answer: %{r:.0%}<extra></extra>',
    fillcolor='#169e99',
    line = dict(color = '#169e99'),
    opacity=0.75 
))

fig.add_trace(go.Scatterpolar(
      r=data[data['Kraj']=='Bulgaria']['Tak'],
      theta=categories,
      fill='toself',
      name='Bulgaria',
    hovertemplate= '<b>Bulgaria</b><br />%{theta}<br />Supportive answer: %{r:.0%}<extra></extra>',
    fillcolor='#fefeff',
    line = dict(color = '#fefeff'),
    opacity=0.75 
))

fig.update_layout(
    #width=6000, 
    #height=600,
    polar=dict(
      radialaxis=dict(
      visible=False,
      range=[0, 1]
    )),
  showlegend=False
)

st.plotly_chart(fig, use_container_width = True)

view_data = data[data['Kraj']=='Germany'].copy().reset_index(drop = True)
view_data.index += 1
view_data = view_data.drop(columns = ['Kraj', 'Tak', 'Nie ', 'Nie mam zdania']).iloc[:-1,:]
view_data.columns = ['Country', 'Full question', 'Description', 'Source']
view_data['Country'] = view_data['Country'].str.replace('<br />', ' ')

st.dataframe(view_data)
st.markdown('Source: Equaldex.com')