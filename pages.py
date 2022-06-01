import os
import time
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


def get_markdown_text(filename):
    with open('markdown/' + filename + '.md') as f:
        lines = f.readlines()
    return ''.join(lines)

def home_page():
    st.markdown(get_markdown_text("home_page"))

def histogram_page():
    st.markdown(get_markdown_text('histogram_page'))

    df = pd.read_csv("ankieta.csv")
    
    semester = st.selectbox('Semester', (2, 4, 6, 'wszystkie'))
    barmode = st.radio('Graph type', ('group', 'stack'))
    if semester != "wszystkie":
        _df = df[df["Semestr"] == semester]
    fig = px.histogram(_df, x="Ocena", color="Jestem", nbins=10, barmode=barmode,
                       color_discrete_sequence=["royalblue", "orange"])

    st.plotly_chart(fig, use_container_width=True)

def line_page():
    st.markdown(get_markdown_text('line_page'))

    #df = pd.read_csv("ankieta.csv")
    
    def set_state():
        st.session_state.active = not st.session_state.active

    st.button('Start/Stop', on_click=set_state)
    placeholder = st.empty()
    with placeholder.container():
        st.line_chart(st.session_state.popularity)
    while st.session_state.active:
        st.session_state.popularity = list(map(lambda x: 0 if x < 0  else x, st.session_state.popularity[:] + [st.session_state.popularity[-1] + np.random.randint(-10, 11)]))
        with placeholder.container():
            st.line_chart(st.session_state.popularity)
        time.sleep(.1)