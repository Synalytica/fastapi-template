from datetime import datetime, timezone

from bson.objectid import ObjectId
from pydantic import BaseConfig, BaseModel


class Base(BaseModel):
    class Config(BaseConfig):
        allow_population_by_alias = True
        json_encoders = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc)
            .isoformat()
            .replace("+00:00", "Z"),
            ObjectId: lambda _id: str(_id)
        }
