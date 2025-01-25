from pydantic import BaseModel
from datetime import datetime
from tzlocal import get_localzone
import pytz
class MealDTOOutput(BaseModel):
    id:int=None
    name:str=None
    description:str=None
    meal_datetime:datetime=None
    isOnDiet:bool=None
    user_id:int=None
    __local_tz=get_localzone()
    def formatted_meal_datetime(self, value):
        return value.astimezone(self.__local_tz).isoformat()
    def map_object(self, data:dict):
        for key in self.model_dump().keys():
            if key == "meal_datetime" and data.get(key):
                setattr(self, key, self.formatted_meal_datetime(data.get(key).replace(tzinfo=pytz.utc)))
            else:
                setattr(self, key, data.get(key))
        return self