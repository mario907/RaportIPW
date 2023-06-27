import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import skimage.io as skio

data = pd.read_excel('Pytania raport.xlsx')
data = data[data['Kraj']=='Poland'].reset_index(drop=True)

st.set_page_config(page_title = 'LGBT and Refugee Rights in Poland', layout = 'wide', page_icon = 'ikona_uniwersytetu.png')
im1, im2, im3, im4, im5 = st.columns([1,1,1.15,1.5,1.5])
with im1:
    st.image('logo_fundacji.png')
with im2:
    st.image('logo_uniwersytetu.png')
with im3:
    st.image('erasmus.png')

st.markdown('<p style = "color:#420773; font-size:38px"><b>Challenges and risks: Poland faces backlash</b></p>', unsafe_allow_html=True)

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



st.markdown('<div style="text-align: justify;"><br />Poland has a restrictive and conservative approach to LGBT and refugee protection. It does not recognize any form of same-sex union, does not allow same-sex couples to adopt children, does not protect LGBT people from discrimination or hate crimes, and does not allow transgender people to change their legal gender without surgery. According to various surveys, a large proportion of Poles oppose LGBT rights and reject homosexuality as a part of society. Poland also has some regions that have declared themselves as “LGBT-free zones” (Rainbow Europe, 2021). <br />Poland has been a transit country for refugees and migrants who want to reach the EU through the eastern route. Most of them come from Ukraine, Chechnya, Afghanistan and other countries affected by war and persecution. Refugees and asylum seekers in Poland face many difficulties and risks, which are similar to Bulgarian case: poor living conditions, lack of access to legal aid, discrimination, violence, exploitation and human trafficking. Some of them also encounter hostility and harassment from far-right groups or anti-immigration movements. (RFE/RL, 2021) Refugees and asylum seekers in Poland also face uncertainty and frustration due to the slow and complex asylum procedures, the lack of solidarity and responsibility sharing among EU member states, and the frequent pushbacks and deportations to Belarus or their countries of origin (DW, 2023). On the other hand, according to a survey conducted by Kantar for UNHCR in January 2021, a majority of Poles declare a favorable attitude towards accepting refugees in the country, and 77% of the respondents agree that Poland should support those who are forced to flee their country. The survey also shows that Poles are motivated by humanitarian, economic and historical reasons to support refugees, and that they recognize the benefits of diversity for the society (“Kantar survey for UNHCR: Majority of Poles now in favour of accepting refugees”). <br />Of particular note in the analysis of the refugee situation is the issue of refugees from Ukraine. According to UNICEF, Poland has received almost 1.6 million refugees from Ukraine since the conflict escalated in February 2022, and around 90% of them are women and children (“UNICEF Refugee Response Office in Poland”). As it was observed  by The Guardian, Poland has worked a refugee miracle by welcoming and integrating a large number of refugees from Ukraine, but it faces challenges such as rising public debt, social tensions, political instability and EU pressure. The article also highlights the role of local initiatives, volunteers and NGOs in supporting refugees and promoting solidarity. It can be concluded that the support for refugees in Poland is high and reflects a sense of responsibility and compassion among Poles, but it also faces difficulties and uncertainties due to the scale and complexity of the refugee situation. There are also various actors and stakeholders involved in the refugee response, which require coordination and cooperation. (Rice, 2022)</div><br/ >', unsafe_allow_html=True)