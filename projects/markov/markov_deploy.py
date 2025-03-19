from prefect import deploy
from markov import markov
from prefect.docker import DockerImage

if __name__ == "__main__":
    markov.deploy(
        name="markov",
        work_pool_name="default",
        image="docker.io/glynfinck/prefect-quantitative-trading/markov:latest",
        build=False,
        push=False
    )
