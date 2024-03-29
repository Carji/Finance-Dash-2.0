import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
from streamlit_ace import st_ace


def app():
    st.markdown("""---""") 
    st.header('Entorno de pruebas')
    st.markdown("""---""") 
    display, editor = st.columns((2, 1))


    hello_world = """
    """

    with editor:
        st.write('### Introduce tu código aquí')
        code = st_ace(
            value=hello_world,
            language="python",
            theme="gruvbox",
            auto_update=True,
            key="vscode"
        )
        st.write(""" Librerías disponibles
- Pandas (pd)
- Numpy (np)
- Seaborn (sns)
- Matplotlib.pyplot (plt)
- Plotly.express (px)
""")
    with display:
        exec(code)