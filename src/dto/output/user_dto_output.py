from pydantic import BaseModel
from models.user import User
class UserDTOOutput(BaseModel):
    id:int=None
    email:str=None
    username:str=None
    def map_object(self, data:dict):
        for key in self.model_dump().keys():
            setattr(self,key,data.get(key))
        return self