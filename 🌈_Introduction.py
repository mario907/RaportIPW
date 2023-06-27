import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title = 'LGBT and Refugee Rights in Europe', layout = 'wide', page_icon = 'ikona_uniwersytetu.png')


data = pd.read_excel('Pytania raport.xlsx')

im1, im2, im3, im4, im5 = st.columns([1,1,1.15,1.5,1.5])
with im1:
    st.image('logo_fundacji.png')
with im2:
    st.image('logo_uniwersytetu.png')
with im3:
    st.image('erasmus.png')
    
st.markdown('<p style = "color:#420773; font-size:38px"><b>LGBT and Refugee Rights in Europe: A Tale of Three Countries</b></p>', unsafe_allow_html=True)    
    
st.markdown('<div style="text-align: justify;"><b>Introduction</b><br />LGBT and refugee rights are two important topics in Europe, especially in light of recent developments and controversies. But how do different countries compare when it comes to legal and social acceptance of LGBT and refugee people? In this article, we will look at the situation of LGBT and refugee people in Poland, Bulgaria and Germany, three countries that represent different levels of progress and challenges in these areas.</br/ > On the forthcoming pages we will describe the situation of the refugee and LGBT people basing on publication of European and world organisations, as well as regional polls.<br />  The report is organised as follows. Each section can be selected on the left side of the report. If agenda is hidden, please click on the <b>\'>\'</b> sign. There are three sections describing each country. By moving the cursor to each image full question and the source of the data is visible. Conclusion section contains summary of the comparison and the plot which compare the situation of LGBT community in these countries. In the last section all of the references are listed.</div>', unsafe_allow_html=True)



    