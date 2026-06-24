# Portafolio de Data Science — Gonzalo Salgado Durán

App desplegada: *(pendiente — agregar link de Streamlit Cloud cuando esté disponible)*

Cinco proyectos de Machine Learning corregidos y documentados, a partir de trabajo de
Diplomado en IA (FEN, Universidad de Chile) y bootcamp de Data Science. Cada proyecto
tiene su notebook completo (análisis, decisiones, conclusiones) y su página
correspondiente en la app interactiva.

## Proyectos

| # | Proyecto | Técnica | Notebook |
|---|---|---|---|
| 01 | Fundamentos ML | Regresión lineal, regresión logística, PCA | [`01_Fundamentos_ML_Regresion_Clasificacion_PCA.ipynb`](notebooks/01_Fundamentos_ML_Regresion_Clasificacion_PCA.ipynb) |
| 02 | Redes Neuronales | 5 arquitecturas de red neuronal comparadas (MNIST) | [`02_Redes_Neuronales_Clasificacion_MNIST.ipynb`](notebooks/02_Redes_Neuronales_Clasificacion_MNIST.ipynb) |
| 03 | Predicción de Ventas | Regresión Lineal vs. Árbol de Decisión | [`03_Prediccion_Ventas_Regresion_Arbol_Decision.ipynb`](notebooks/03_Prediccion_Ventas_Regresion_Arbol_Decision.ipynb) |
| 04 | Clasificación de Fármacos | Random Forest, KNN, Regresión Logística + GridSearchCV | [`04_Clasificacion_Farmacos_RF_KNN_LogReg.ipynb`](notebooks/04_Clasificacion_Farmacos_RF_KNN_LogReg.ipynb) |
| 05 | Precio de Celular | XGBoost (RFECV + GridSearchCV) vs. Red Neuronal | [`05_Clasificacion_Precio_Celular_XGBoost_RedNeuronal.ipynb`](notebooks/05_Clasificacion_Precio_Celular_XGBoost_RedNeuronal.ipynb) |

## Estructura del repositorio

```
streamlit_app.py     Entrypoint de la app (st.navigation)
views/                Páginas de la app (una por proyecto, + inicio)
src/                  Funciones reutilizables, separadas por proyecto
artifacts/            Modelos entrenados y métricas ya calculadas (no se recalculan en la app)
notebooks/            Notebooks completos, con el análisis y storytelling
data/                 Datasets crudos usados por los notebooks
```

## Cómo correr localmente

```bash
git clone <url-del-repo>
cd portafolio-data-science
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Estado de avance

- [ ] 01 · Fundamentos ML
- [ ] 02 · Redes Neuronales
- [ ] 03 · Predicción de Ventas
- [ ] 04 · Clasificación de Fármacos
- [ ] 05 · Precio de Celular

*(Marcar cada casilla al cerrar la etapa de "Adaptación GitHub" de ese proyecto.)*
