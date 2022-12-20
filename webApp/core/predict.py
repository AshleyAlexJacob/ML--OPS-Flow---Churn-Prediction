import joblib
from webApp.utils.read_params import readParams

def predict(data,params_path):
    config = readParams(params_path)
    model_dir_path = config["model_webapp_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data).tolist()[0]
    return prediction 
    