import streamlit as st
import numpy as np
import pandas as pd

data = pd.read_excel('Pytania raport.xlsx')
data = data[data['Kraj']=='Bulgaria'].reset_index(drop=True)

st.set_page_config(page_title = 'LGBT and Refugee Rights in Bulgaria', layout = 'wide', page_icon = 'ikona_uniwersytetu.png')
im1, im2, im3, im4, im5 = st.columns([1,1,1.5,1.5,1.5])
with im1:
    st.image('logo_fundacji.png')
with im2:
    st.image('logo_uniwersytetu.png')
    
h1,ind, h2 = st.columns([6, .25, 1])  
with h1:
    st.title(':violet[Social acceptance: Bulgaria falls behind]')
    st.markdown('<div style="text-align: justify;"><br />Bulgaria has a limited capacity and resources to deal with the influx of refugees. It does not recognize same-sex marriage, but it recognizes foreign same-sex marriages since 2019. It allows single LGBT people to adopt children, but not same-sex couples. It bans discrimination based on sexual orientation and gender identity, but it does not ban conversion therapy or hate crimes. It does not allow transgender people to change their legal gender at all since 2023. According to various surveys, a majority of Bulgarians do not support LGBT rights and do not accept homosexuality as a part of society (Rainbow Europe, 2021).<br />Bulgaria is also one of the main entry points for refugees and migrants who want to reach the EU through the Balkan route. Most of them come from Syria, Afghanistan, Iraq and other countries affected by war and persecution. Refugees and migrants in Bulgaria face many difficulties and risks, such as poor living conditions, lack of access to health care, education and integration services, discrimination, violence, exploitation and human trafficking. Some of them also encounter hostility and harassment from local communities or vigilante groups who patrol the border with Turkey (UNICEF, 2022). It has a confirmation in surveys: according to a survey conducted by UNHCR in 2019, 43% of Bulgarians have a positive or neutral attitude towards refugees, and 57% have a negative or very negative one (UNHCR Bulgaria, 2019). Additionally, in a public opinion poll from 2017, 47% of adult Bulgarian citizens declared they are against the European Union (of which Bulgaria is a member state) helping refugees seeking asylum on its territory, and 28% support the opposite position (Open ended social studies, 2017). <br /> In a report from 2020, Bulgaria ranks 25th out of 32 European countries in terms of refugee integration, achieving low scores in education, labor market, health and citizenship (The Bulgarian Council on Refugees and Migrants, 2020). <br /> It can be concluded that the support for accepting refugees in Bulgaria is low and faces many challenges related to integration. At the same time, there are civil society organizations and initiatives that try to improve the situation of refugees and promote attitudes of tolerance and solidarity in Bulgarian society.</div><br />', unsafe_allow_html=True)

with h2:
    st.image('pride.png', width = 75)
    st.metric(label = 'Acceptance of same-sex relationships', 
              value = "{0:.0%}".format(data.loc[8, 'Tak']), 
              label_visibility = 'collapsed')
    st.image('neighborhood.png', width = 75)
    st.metric(label = 'Acceptance of homosexuals as neighbors', 
              value = "{0:.0%}".format(data.loc[2, 'Tak']), 
              label_visibility = 'collapsed')
    st.image('family.png', width = 75)
    st.metric(label = 'Views on same-sex couples\' right to adopt', 
              value = "{0:.0%}".format(data.loc[4, 'Tak']), 
              label_visibility = 'collapsed')
    st.image('transgender.png', width = 75)
    st.metric(label = 'Support for transgender people', 
              value = "{0:.0%}".format(data.loc[9, 'Tak']), 
              label_visibility = 'collapsed')  