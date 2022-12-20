import joblib
import mlflow
from pprint import pprint
from mlflow.tracking import MlflowClient
from utils.read_params import readParams
from utils.get_args import getArguments


def log_production_model(config_path):
    config = readParams(config_path)
    mlflow_config = config["mlflow_config"]
    model_name = mlflow_config["registered_model_name"]
    model_dir = config["model_dir"]
    remote_server_uri = mlflow_config["remote_server_uri"]

    mlflow.set_tracking_uri(remote_server_uri)
    runs = mlflow.search_runs(experiment_ids=[1])
    max_accuracy = max(runs["metrics.accuracy"])
    max_accuracy_run_id = list(
        runs[runs["metrics.accuracy"] == max_accuracy]["run_id"])[0]
    # print(max_accuracy_run_id)
    client = MlflowClient()
    for mv in client.search_model_versions(f"name='{model_name}'"):
        mv = dict(mv)

        if mv["run_id"] == max_accuracy_run_id:
            current_version = mv["version"]
            logged_model = mv["source"]
            pprint(mv, indent=4)
            client.transition_model_version_stage(
                name=model_name,
                version=current_version,
                stage="Production"
            )
        else:
            current_version = mv["version"]
            client.transition_model_version_stage(
                name=model_name,
                version=current_version,
                stage="Staging"
            )

    loaded_model = mlflow.pyfunc.load_model(logged_model)
    joblib.dump(loaded_model, model_dir)


if __name__ == '__main__':
    parsed_args = getArguments()
    data = log_production_model(config_path=parsed_args.config)
