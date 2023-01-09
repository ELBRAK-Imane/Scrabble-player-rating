
# 1. Library imports
import uvicorn
from fastapi import FastAPI
from rating import Rating
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("myfile.pkl","rb")
regressor=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_banknote(data:Rating):
    data = data.dict()
 
    game_id=data['gane_id']
    user_score=data['user_score']
    bot_score=data['bit_score']
    bot_rating=data['bot_rating']
    user_freq=data['user_freq']
   # print(regressor.predict([[variance,skewness,curtosis,entropy]]))
    prediction = regressor.predict([[game_id,user_score,bot_score,bot_rating,user_freq]])
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)