# Purpose: This script initializes the API service for the MLOps pipeline. It sets up the FastAPI application and defines an endpoint to return the model's score.

from fastapi import FastAPI
from utils import return_score

app = FastAPI()



@app.get("/score")
def score_property():
    return return_score()




