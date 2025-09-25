from kedro.pipeline import Pipeline, node
from .nodes import clean_data


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=clean_data,
                inputs="raw_salary_data",
                outputs="cleaned_salary_data",
                name="clean_data_node",
            )
        ]
    )
