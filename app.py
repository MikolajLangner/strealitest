import streamlit as st
import numpy as np
from pages import home_page, histogram_page, line_page, get_markdown_text


st.set_page_config(layout="wide")

st.markdown('''
<style>
button {
    width: 100% !important
}
</style>''', unsafe_allow_html=True)

mapping = {
    "Home": home_page,
    "Histogram": histogram_page,
    "Line": line_page
}

def show_page(page):
    st.session_state.page = page    
    st.session_state.active = False
    st.session_state.popularity = list(np.random.randint(1, 100, size=100))

def show_app():
    st.sidebar.subheader("Menu")
    for t in mapping.keys():    
        st.sidebar.button(t, on_click=show_page, key='menu' + t, args=(t, ))
    st.sidebar.markdown(get_markdown_text("about"))

    if 'page' not in st.session_state:
        st.session_state.page = 'Home'
    page = st.session_state.page
    redirect = mapping[page]    
    redirect()


if __name__ == "__main__":
    show_app()
