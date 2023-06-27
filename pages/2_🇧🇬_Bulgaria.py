import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import skimage.io as skio


data = pd.read_excel('Pytania raport.xlsx')
data = data[data['Kraj']=='Bulgaria'].reset_index(drop=True)

st.set_page_config(page_title = 'LGBT and Refugee Rights in Bulgaria', layout = 'wide', page_icon = 'ikona_uniwersytetu.png')
im1, im2, im3, im4, im5 = st.columns([1,1,1.15,1.5,1.5])
with im1:
    st.image('logo_fundacji.png')
with im2:
    st.image('logo_uniwersytetu.png')
with im3:
    st.image('erasmus.png')
    
st.markdown('<p style = "color:#420773; font-size:38px"><b>Social acceptance: Bulgaria falls behind</b></p>', unsafe_allow_html=True)

pl1, pl2, pl3, pl4 = st.columns([5,5,5,5])
with pl1:
    img = skio.imread('pride.png')
    fig = px.imshow(img).update_xaxes(showticklabels = False).update_yaxes(showticklabels = False, showgrid = False).update_layout(plot_bgcolor='white').update_traces(hovertemplate="<b>{}</b><br><i>Source: {}</i><extra></extra>".format(data.loc[8, 'Pytanie'], data.loc[8, 'Source'])).update_layout(title={'text': "{0:.0%}".format(data.loc[8, 'Tak']),'y':0.18,'x':0.42,'xanchor': 'center','yanchor': 'top', 'font':dict(size=48,color="#420773")})
    st.plotly_chart(fig, use_container_width = True)
with pl2:
    img2 = skio.imread('neighborhood.png')
    fig2 = px.imshow(img2).update_xaxes(showticklabels = False).update_yaxes(showticklabels = False, showgrid = False).update_layout(plot_bgcolor='white').update_traces(hovertemplate="<b>{}</b><br><i>Source: {}</i><extra></extra>".format(data.loc[2, 'Pytanie'], data.loc[2, 'Source'])).update_layout(title={'text': "{0:.0%}".format(data.loc[2, 'Tak']),'y':0.18,'x':0.5,'xanchor': 'center','yanchor': 'top', 'font':dict(size=48,color="#420773")})
    st.plotly_chart(fig2, use_container_width = True)
with pl3:
    img3 = skio.imread('family.png')
    fig3 = px.imshow(img3).update_xaxes(showticklabels = False).update_yaxes(showticklabels = False, showgrid = False).update_layout(plot_bgcolor='white').update_traces(hovertemplate="<b>{}</b><br><i>Source: {}</i><extra></extra>".format(data.loc[4, 'Pytanie'], data.loc[4, 'Source'])).update_layout(title={'text': "{0:.0%}".format(data.loc[4, 'Tak']),'y':0.18,'x':0.55,'xanchor': 'center','yanchor': 'top', 'font':dict(size=48,color="#420773")})
    st.plotly_chart(fig3, use_container_width = True)
with pl4:
    img4 = skio.imread('transgender.png')
    fig4 = px.imshow(img4).update_xaxes(showticklabels = False).update_yaxes(showticklabels = False, showgrid = False).update_layout(plot_bgcolor='white').update_traces(hovertemplate="<b>{}</b><br><i>Source: {}</i><extra></extra>".format(data.loc[9, 'Pytanie'], data.loc[9, 'Source'])).update_layout(title={'text': "{0:.0%}".format(data.loc[9, 'Tak']),'y':0.18,'x':0.55,'xanchor': 'center','yanchor': 'top', 'font':dict(size=48,color="#420773")})
    st.plotly_chart(fig4, use_container_width = True)    


st.markdown('<div style="text-align: justify;"><br />Bulgaria has a limited capacity and resources to deal with the influx of refugees. It does not recognize same-sex marriage, but it recognizes foreign same-sex marriages since 2019. It allows single LGBT people to adopt children, but not same-sex couples. It bans discrimination based on sexual orientation and gender identity, but it does not ban conversion therapy or hate crimes. It does not allow transgender people to change their legal gender at all since 2023. According to various surveys, a majority of Bulgarians do not support LGBT rights and do not accept homosexuality as a part of society (Rainbow Europe, 2021).<br />Bulgaria is also one of the main entry points for refugees and migrants who want to reach the EU through the Balkan route. Most of them come from Syria, Afghanistan, Iraq and other countries affected by war and persecution. Refugees and migrants in Bulgaria face many difficulties and risks, such as poor living conditions, lack of access to health care, education and integration services, discrimination, violence, exploitation and human trafficking. Some of them also encounter hostility and harassment from local communities or vigilante groups who patrol the border with Turkey (UNICEF, 2022). It has a confirmation in surveys: according to a survey conducted by UNHCR in 2019, 43% of Bulgarians have a positive or neutral attitude towards refugees, and 57% have a negative or very negative one (UNHCR Bulgaria, 2019). Additionally, in a public opinion poll from 2017, 47% of adult Bulgarian citizens declared they are against the European Union (of which Bulgaria is a member state) helping refugees seeking asylum on its territory, and 28% support the opposite position (Open ended social studies, 2017). <br /> In a report from 2020, Bulgaria ranks 25th out of 32 European countries in terms of refugee integration, achieving low scores in education, labor market, health and citizenship (The Bulgarian Council on Refugees and Migrants, 2020). <br /> It can be concluded that the support for accepting refugees in Bulgaria is low and faces many challenges related to integration. At the same time, there are civil society organizations and initiatives that try to improve the situation of refugees and promote attitudes of tolerance and solidarity in Bulgarian society.</div><br />', unsafe_allow_html=True)
