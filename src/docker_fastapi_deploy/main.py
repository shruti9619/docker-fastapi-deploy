from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pathlib

app = FastAPI()


def load_model():
    model_path = pathlib.Path(__file__).parent / "model.pkl"
    return joblib.load(model_path)


class InputData(BaseModel):
    data: list[float]


@app.post("/predict")
def predict(input_data: InputData):
    model = load_model()
    pred = model.predict([input_data.data])[0]
    return {"prediction": int(pred)}
