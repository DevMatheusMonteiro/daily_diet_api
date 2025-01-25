from pydantic import BaseModel
from datetime import datetime
from tzlocal import get_localzone
from utils.app_error import AppError
import pytz
class MealDTOInput(BaseModel):
    id:int=None
    name:str=None
    description:str=None
    meal_datetime:datetime=None
    isOnDiet:bool=None
    user_id:int=None
    __local_tz=get_localzone()
    def convert_datetime(self, value):
        if isinstance(value, str):
            datetime_formats = [
                "%d/%m/%Y %H:%M:%S",      # Dia/Mês/Ano Horas:Minutos:Segundos
                "%Y-%m-%d %H:%M:%S",      # Ano-Mês-Dia Horas:Minutos:Segundos
                "%Y-%m-%dT%H:%M:%S%z",    # ISO 8601 com timezone
                "%Y-%m-%dT%H:%M:%S",      # ISO 8601 sem timezone
                "%d-%m-%Y %H:%M:%S",      # Dia-Mês-Ano Horas:Minutos:Segundos
                "%m/%d/%Y %H:%M:%S",      # Mês/Dia/Ano Horas:Minutos:Segundos (formato americano)
                "%Y/%m/%d %H:%M:%S",      # Ano/Mês/Dia Horas:Minutos:Segundos
                "%Y.%m.%d %H:%M:%S",      # Ano.Mês.Dia Horas:Minutos:Segundos
                "%d %b %Y %H:%M:%S",      # Dia Abrev_Mês Ano Horas:Minutos:Segundos (e.g., 25 Jan 2025 10:30:45)
                "%d %B %Y %H:%M:%S",      # Dia Nome_Mês Ano Horas:Minutos:Segundos (e.g., 25 Janeiro 2025 10:30:45)
                "%Y-%m-%d",               # Ano-Mês-Dia
                "%d/%m/%Y",               # Dia/Mês/Ano
                "%m/%d/%Y",               # Mês/Dia/Ano
                "%Y.%m.%d",               # Ano.Mês.Dia
                "%d-%m-%Y",               # Dia-Mês-Ano
                "%Y-%m-%dT%H:%M",         # ISO 8601 simplificado sem segundos
            ]
            for datetime_format in datetime_formats:
                try:
                    parsed_date = datetime.strptime(value, datetime_format)
                    return parsed_date.replace(tzinfo=self.__local_tz).astimezone(pytz.utc)
                except:
                    continue
            raise AppError(f"Formato de data inválido. Os formatos suportados são: {", ".join(datetime_formats)}")
        elif isinstance(value, datetime):
            return value.astimezone(pytz.utc)
        return value
    def map_object(self, data: dict):
        for key in self.model_dump().keys():
            if key == "meal_datetime":
                setattr(self, key, self.convert_datetime(data.get(key)))
            else:
                setattr(self, key, data.get(key))
        return self