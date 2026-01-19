from fastapi import FastAPI
from utils import return_score

app = FastAPI()



@app.get("/score")
def score_property():
    return return_score()




