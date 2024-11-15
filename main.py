
from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel

model = joblib.load('knn_model2.joblib')
scaler = joblib.load('scaler2.joblib')

app = FastAPI()
# GET request
@app.get("/")
def read_root():
    return {"message": "Welcome to Tuwaiq Academy"}
# get request
@app.get("/items/")
def create_item(item: dict):
    return {"item": item}


class InputFeatures(BaseModel):
    age: float
    appearance: int

    goals: float
    assists: float
    award: int
    highest_value: int
    team_AS_Monaco: int
    team_Southampton_FC: int



def preprocessing(input_features: InputFeatures):
    dict_f = {
        'age': input_features.age,
        'appearance': input_features.appearance,
        'goals': input_features.goals,
        'assists': input_features.assists,
        'award': input_features.award,
        'highest_value': input_features.highest_value,
        'team_AS Monaco': input_features.team_AS_Monaco,
        'team_Southampton_FC': input_features.team_Southampton_FC,
    }

    features_list = [dict_f[key] for key in sorted(dict_f)]
    scaled_features = scaler.transform([features_list])
    return scaled_features



@app.get("/predict")
def predict(input_features: InputFeatures):
    return preprocessing(input_features)

@app.post("/predict")
async def predict(input_features: InputFeatures):
    data = preprocessing(input_features)
    y_pred = model.predict(data)
    return {"pred": y_pred.tolist()[0]}