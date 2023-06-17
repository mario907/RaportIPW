import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

data = pd.read_excel('Pytania raport.xlsx')
data = data[data['Kraj']=='Germany'].reset_index(drop=True)

st.set_page_config(page_title = 'LGBT and Refugee Rights in Germany', layout = 'wide', page_icon = 'ikona_uniwersytetu.png')
im1, im2, im3, im4, im5 = st.columns([1,1,1.5,1.5,1.5])
with im1:
    st.image('logo_fundacji.png')
with im2:
    st.image('logo_uniwersytetu.png')
h1,ind, h2 = st.columns([6, .25, 1])


with h2:
    st.image('pride.png', width = 75)
    st.metric(label = 'Acceptance of same-sex relationships', value = "{0:.0%}".format(data.loc[8, 'Tak']), label_visibility = 'collapsed')
    st.image('neighborhood.png', width = 75)
    st.metric(label = 'Acceptance of homosexuals as neighbors', value = "{0:.0%}".format(data.loc[2, 'Tak']), label_visibility = 'collapsed')
    st.image('family.png', width = 75)
    st.metric(label = 'Views on same-sex couples\' right to adopt', value = "{0:.0%}".format(data.loc[4, 'Tak']), label_visibility = 'collapsed')
    st.image('transgender.png', width = 75)
    st.metric(label = 'Support for transgender people', value = "{0:.0%}".format(data.loc[9, 'Tak']), label_visibility = 'collapsed')
with h1:
    st.title(':violet[Legal rights: Germany leads the way]')
    st.markdown('<div style="text-align: justify;"><br />Germany has the most progressive and supportive legal environment for LGBT and refugee people among the three countries. It has legalized same-sex marriage since 2017, allows same-sex couples to adopt children, bans discrimination and conversion therapy based on sexual orientation and gender identity, and allows transgender people to change their legal gender without surgery. These laws reflect the public opinion of Germans, who according to various surveys, support LGBT rights and accept homosexuality as a part of society (Rainbow Europe, 2021).<br /> Germany is also the fifth largest host country of refugees in the world and the second largest humanitarian donor globally. It has welcomed more than one million refugees and asylum seekers since 2015, mostly from Syria, Afghanistan and Iraq. It grants protection to refugees and asylum seekers based on the Geneva Convention and EU law. It also provides access to health care, education, integration and resettlement services. It has a high recognition rate and a low rejection rate for asylum applications (UNHCR, 2021). <br /> Based on the results of the survey published in 2023, authors stated that a majority of Germans living in cities engaged in some form of support for refugees in the years 2015–2020. What is more, attitudes towards diversity in Germany are strong predictors of pro-refugee engagement, regardless of other factors such as age, gender, education or religion. Authors observed support for refugees does not only stem from humanitarian motives, but also from a general acceptance of socio-cultural diversity in German society. It was also claimed that attitudes towards diversity are not homogeneous, but can be divided into five latent classes, which differ in their acceptance and rejection of different groups of immigrants and minorities. (Drouhot, L.G., Schönwälder, K., Petermann, S. et al., 2023).</div><br/ >', unsafe_allow_html=True)


    
st.markdown('''
<style>
/*center metric delta value*/
div[data-testid="metric-container"] > div[data-testid="stMetricDelta"] > div{
  justify-content: center;
  color: #01cefc;
}

/*center metric delta svg*/
[data-testid="stMetricDelta"] > svg {
  position: absolute;
  left: 30%;
  -webkit-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  transform: translateX(-50%);
}
</style>''', unsafe_allow_html=True)