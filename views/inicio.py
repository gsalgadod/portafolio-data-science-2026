import streamlit as st

st.title("Portafolio de Data Science")
st.subheader("Gonzalo Salgado Durán")

st.markdown(
    """
Cinco proyectos de Machine Learning, corregidos y documentados a partir de trabajo de
Diplomado en IA (FEN, Universidad de Chile) y bootcamp de Data Science. Cada página
incluye un demo interactivo y una pestaña con el detalle metodológico (comparación de
modelos, ajuste de hiperparámetros, métricas). El notebook completo de cada proyecto,
con el razonamiento paso a paso, está disponible en la carpeta `notebooks/` del
[repositorio en GitHub](#).
"""
)

st.divider()

proyectos = [
    {
        "orden": "01",
        "nombre": "Fundamentos ML",
        "tecnica": "Regresión lineal, regresión logística, PCA",
        "dataset": "CLTV de clientes, Titanic, MNIST",
    },
    {
        "orden": "02",
        "nombre": "Redes Neuronales",
        "tecnica": "5 arquitecturas de red neuronal comparadas",
        "dataset": "MNIST (dígitos escritos a mano)",
    },
    {
        "orden": "03",
        "nombre": "Predicción de Ventas",
        "tecnica": "Regresión lineal vs. Árbol de Decisión",
        "dataset": "Ventas por ítem y tienda (retail)",
    },
    {
        "orden": "04",
        "nombre": "Clasificación de Fármacos",
        "tecnica": "Random Forest, KNN y Regresión Logística + GridSearchCV",
        "dataset": "Perfil de paciente → fármaco recomendado",
    },
    {
        "orden": "05",
        "nombre": "Precio de Celular",
        "tecnica": "XGBoost (RFECV + GridSearchCV) vs. Red Neuronal",
        "dataset": "Especificaciones técnicas de celulares",
    },
]

for p in proyectos:
    with st.container(border=True):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.markdown(f"### {p['orden']}")
        with col2:
            st.markdown(f"**{p['nombre']}**")
            st.caption(f"Técnica: {p['tecnica']}")
            st.caption(f"Dataset: {p['dataset']}")
