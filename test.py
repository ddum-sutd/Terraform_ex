import logging,mlflow,sys,os
from prefect import task, flow

def workflow_main():
    print('defined workflow')

if __name__ == "__main__":
    # Call the load_config to get the configuration object
    cfg = load_config()

    # Set MLflow tracking URI
    mlflow.set_tracking_uri(cfg.mlflow.tracking_uri)

    # Set the experiment name from the configuration file
    mlflow.set_experiment(cfg.mlflow.experiment_name)

    workflow_main()