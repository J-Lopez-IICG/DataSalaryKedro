import pandas as pd


def clean_data(raw_salary_data: pd.DataFrame) -> pd.DataFrame:
    """
    Toma el DataFrame de salarios y realiza una limpieza básica.
    """
    print("Datos recibidos exitosamente:")
    print(raw_salary_data.head())

    # Lógica de limpieza: eliminar filas con valores nulos.
    cleaned_df = raw_salary_data.dropna()

    return cleaned_df
