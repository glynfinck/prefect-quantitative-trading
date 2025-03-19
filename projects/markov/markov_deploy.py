from prefect import flow
from prefect_github import GitHubCredentials
from prefect.runner.storage import GitRepository
from prefect.docker import DockerImage

if __name__ == "__main__":
    source = GitRepository(
        url="https://github.com/glynfinck/prefect-quantitative-trading.git",
        credentials=GitHubCredentials.load("github-credentials"),
        branch="main"
    )
    flow.from_source(
        source=source,
        entrypoint="projects/markov/markov.py:markov"
    ).deploy(
        name="markov",
        work_pool_name="default",
        image=DockerImage(
            name="docker.io/glynfinck/prefect-quantitative-trading-markov",
            tag="latest"
        ),
        build=False,
        push=False
    )
