from src import sandbox
import streamlit as st
st.set_page_config(layout="wide")
hojas = {
    "Entorno de pruebas": sandbox,
}
st.markdown("""
    <style type="text/css">
    div[data-testid="stHorizontalBlock"] {
        border:10px;
        padding:30px;
        border-radius: 15px;
        background:#FFFFFF;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)
st.title('Cuadro de mando para análisis financiero 💹')
#st.sidebar.image('img/****.png')
st.sidebar.title('Contenido de la aplicación')

selection = st.sidebar.radio("", list(hojas.keys()))
page = hojas[selection]
page.app()

st.markdown("""   """)
st.markdown("""---""")
st.markdown("""   """)
st.write("### Link to Github repo:")
st.markdown("[GitHub Repository](https://github.com/carji/Finance-Dash-2.0)")