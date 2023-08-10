import logging,mlflow,sys,os
from prefect import task, flow

def workflow_main():
    print('defined workflow')

if __name__ == "__main__":

    # Set MLflow tracking URI
    mlflow.set_tracking_uri('sqlite:///mlflow.db')

    # Set the experiment name from the configuration file
    mlflow.set_experiment('myname')

    workflow_main()
