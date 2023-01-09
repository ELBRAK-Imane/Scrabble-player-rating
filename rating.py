from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Rating(BaseModel):
    game_id:int
    user_score:int
    bot_score:int
    bot_rating:float
    user_freq:int