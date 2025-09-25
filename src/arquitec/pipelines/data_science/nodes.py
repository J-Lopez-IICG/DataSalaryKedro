import pandas as pd
from typing import Dict, Any
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import logging


def split_data(data: pd.DataFrame, parameters: Dict[str, Any]) -> Dict[str, Any]:
    """Divide los datos en conjuntos de entrenamiento y prueba."""
    X = data[parameters["features"]]
    y = data[parameters["target"]]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )

    return dict(
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
    )


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    """Entrena un modelo de regresión lineal."""
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return regressor


def evaluate_model(
    regressor: LinearRegression, X_test: pd.DataFrame, y_test: pd.Series
):
    """Evalúa el modelo entrenado e imprime los resultados."""
    y_pred = regressor.predict(X_test)
    score = r2_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info(f"Model R² score: {score:.2f}")
