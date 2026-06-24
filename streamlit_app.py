import streamlit as st

st.set_page_config(page_title="Portafolio Data Science — Gonzalo Salgado", layout="wide")

pg = st.navigation(
    [
        st.Page("views/inicio.py", title="Inicio", default=True),
        st.Page("views/01_fundamentos_ml.py", title="01 · Fundamentos ML"),
        st.Page("views/02_redes_neuronales.py", title="02 · Redes Neuronales"),
        st.Page("views/03_prediccion_ventas.py", title="03 · Predicción de Ventas"),
        st.Page("views/04_clasificacion_farmacos.py", title="04 · Clasificación de Fármacos"),
        st.Page("views/05_clasificacion_precio_celular.py", title="05 · Precio de Celular"),
    ]
)

pg.run()
