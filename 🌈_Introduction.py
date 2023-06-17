import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title = 'LGBT and Refugee Rights in Europe', layout = 'wide', page_icon = 'ikona_uniwersytetu.png')


data = pd.read_excel('Pytania raport.xlsx')

im1, im2, im3, im4, im5 = st.columns([1,1,1.5,1.5,1.5])
with im1:
    st.image('logo_fundacji.png')
with im2:
    st.image('logo_uniwersytetu.png')
st.title(':violet[LGBT and Refugee Rights in Europe: A Tale of Three Countries]')    
    
st.markdown('<div style="text-align: justify;"><b>Introduction</b><br />LGBT and refugee rights are two important topics in Europe, especially in light of recent developments and controversies. But how do different countries compare when it comes to legal and social acceptance of LGBT and refugee people? In this article, we will look at the situation of LGBT and refugee people in Poland, Bulgaria and Germany, three countries that represent different levels of progress and challenges in these areas.</br/ ></div>', unsafe_allow_html=True)



    
