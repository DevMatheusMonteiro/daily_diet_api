from pydantic import BaseModel
from models.user import User
class UserDTOInput(BaseModel):
    id:int=None
    email:str=None
    username:str=None
    password:str=None
    def map_object(self, data:dict):
        for key in self.model_dump().keys():
            setattr(self,key,data.get(key))
