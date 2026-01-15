from fastapi import FastAPI
from utils import return_score

app = FastAPI()



@app.get("/score")
def score_property():
    #score = property.surface
    #if property.rooms:
    #    score += property.rooms * 10
    return return_score()




