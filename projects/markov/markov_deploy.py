from prefect import deploy
from markov import markov
from prefect.docker import DockerImage

if __name__ == "__main__":
    markov.deploy(
        name="markov",
        work_pool_name="default",
        image=DockerImage(
            name="markov",
            tag="latest",
            dockerfile="../../deploy/Dockerfile"
        ),
        push=True,
    )