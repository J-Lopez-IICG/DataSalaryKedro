from kedro.pipeline import Pipeline, node, pipeline
from .nodes import create_regression_plot


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=create_regression_plot,
                inputs=[
                    "regressor",
                    "X_test",
                    "y_test",
                    "cleaned_salary_data",
                    "params:model_options",
                ],
                outputs="regression_plot",
                name="create_regression_plot_node",
            )
        ]
    )
