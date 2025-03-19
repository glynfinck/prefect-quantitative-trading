from prefect import flow, get_run_logger, serve
from prefect.artifacts import create_table_artifact
import numpy as np
import pandas as pd
import getpass


@flow()
def markov():
    logger = get_run_logger()
    logger.info("Processing...")
    df = pd.DataFrame({"a": np.random.rand(10), "b": np.random.rand(10)})
    create_table_artifact(df.to_dict("records"),
                          key="sample-table", description="A sample table")
    return "Finished!"


if __name__ == "__main__":
    deployment1 = markov.to_deployment(
        name=f"{markov.name}_{getpass.getuser()}")
    serve(deployment1)
