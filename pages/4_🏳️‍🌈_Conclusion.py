import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

data = pd.read_excel('Pytania raport.xlsx')

st.set_page_config(page_title = 'LGBT and Refugee Rights in Europe - Conclusion', layout = 'wide', page_icon = 'ikona_uniwersytetu.png')
im1, im2, im3, im4, im5 = st.columns([1,1,1.5,1.5,1.5])
with im1:
    st.image('logo_fundacji.png')
with im2:
    st.image('logo_uniwersytetu.png')
st.title(':violet[Conclusion]')

st.markdown('<div style="text-align: justify;">As we have seen, LGBT and refugee rights vary significantly across Europe, depending on the legal and social context of each country. While Germany is a role model for LGBT equality and inclusion as well as refugee support and protection, Poland and Bulgaria still have a long way to go to ensure the dignity and safety of their LGBT and refugee citizens. We hope that this article has helped you understand the differences and similarities between these three countries and has inspired you to take action for LGBT and refugee rights in your own community.</div><br/ >', unsafe_allow_html=True)

categories = data['Pytanie'].unique()
support = ['Support', 'Agree', 'Did not mention homosexuals', 'Justifable', 'Agree', 'Yes', 'Rare', 'Rare', 'Agree', 'Yes', 'Favor']
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
      r=data[data['Kraj']=='Germany']['Tak'],
      theta=categories,
      fill='toself',
      name='Germany',
    hovertemplate= '<b>Germany</b><br />%{theta}<br />Supportive answer: %{r:.0%}',
    fillcolor='#420773',
    line = dict(color = '#420773'),
    opacity=0.75 
))

fig.add_trace(go.Scatterpolar(
      r=data[data['Kraj']=='Poland']['Tak'],
      theta=categories,
      fill='toself',
      name='Poland',
    hovertemplate= '<b>Poland</b><br />%{theta}<br />Supportive answer: %{r:.0%}',
    fillcolor='#169e99',
    line = dict(color = '#169e99'),
    opacity=0.75 
))

fig.add_trace(go.Scatterpolar(
      r=data[data['Kraj']=='Bulgaria']['Tak'],
      theta=categories,
      fill='toself',
      name='Bulgaria',
    hovertemplate= '<b>Bulgaria</b><br />%{theta}<br />Supportive answer: %{r:.0%}',
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