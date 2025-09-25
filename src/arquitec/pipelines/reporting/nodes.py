import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from typing import Dict


def create_regression_plot(
    regressor: LinearRegression,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    cleaned_data: pd.DataFrame,
    parameters: Dict,
):
    """Crea y guarda una gráfica de la regresión lineal."""

    # Extraer el nombre de la característica para los ejes
    feature_name = parameters["features"][0]
    target_name = parameters["target"]

    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))

    # 1. Dibuja los puntos de datos reales
    plt.scatter(
        X_test, y_test, color="#1f77b4", s=50, alpha=0.7, label="Salarios Reales"
    )

    # 2. Dibuja la línea de regresión
    # Usamos 'cleaned_data' para obtener el rango completo de X
    x_range = np.linspace(
        cleaned_data[feature_name].min(), cleaned_data[feature_name].max(), 100
    ).reshape(-1, 1)
    y_line = regressor.predict(x_range)

    plt.plot(
        x_range,
        y_line,
        color="red",
        linewidth=3,
        linestyle="--",
        label="Línea de Regresión",
    )

    # 3. Añade títulos y etiquetas
    plt.title(
        f"Modelo de Regresión: {target_name} vs {feature_name}", fontsize=16, pad=20
    )
    plt.xlabel(feature_name, fontsize=12)
    plt.ylabel(target_name, fontsize=12)
    plt.legend(loc="upper left", fontsize=10)
    plt.tight_layout()

    # En lugar de plt.show(), devolvemos la figura para que Kedro la guarde
    return plt.gcf()
