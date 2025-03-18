from prefect import flow, get_run_logger, serve
import getpass

@flow()
def markov():
    logger = get_run_logger()
    logger.info("Markov chain has been deployed!")

if __name__ == "__main__":
    deployment1 = markov.to_deployment(name=f"{markov.name}_{getpass.getuser()}")
    serve(deployment1)