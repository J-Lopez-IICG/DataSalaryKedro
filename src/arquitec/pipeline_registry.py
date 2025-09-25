from kedro.pipeline import Pipeline
from arquitec.pipelines import data_processing
from arquitec.pipelines import data_science
from arquitec.pipelines import reporting  # <-- 1. Importa el nuevo pipeline


def register_pipelines() -> dict[str, Pipeline]:
    # ...existing code...
    data_processing_pipeline = data_processing.create_pipeline()
    data_science_pipeline = data_science.create_pipeline()
    reporting_pipeline = reporting.create_pipeline()  # <-- 2. Crea una instancia

    return {
        "dp": data_processing_pipeline,
        "ds": data_science_pipeline,
        "report": reporting_pipeline,  # <-- 3. Añádelo al diccionario
        "__default__": (
            data_processing_pipeline
            + data_science_pipeline
            + reporting_pipeline  # <-- 4. Combínalos para la ejecución por defecto
        ),
    }
