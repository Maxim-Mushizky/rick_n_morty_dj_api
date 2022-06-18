from django.db import models
import pydantic
from pydantic import ValidationError, validator
from typing import List


class Character(models.Model):
    status: str = models.CharField(max_length=200)
    species: str = models.CharField(max_length=200)
    type: str = models.CharField(max_length=200)
    gender: str = models.CharField(max_length=200)
    episode: str = models.CharField(max_length=200)


class CharacterComparison(pydantic.BaseModel):
    name: str = pydantic.Field(default_factory=str)
    status: str = pydantic.Field(default_factory=str)
    species: str = pydantic.Field(default_factory=str)
    type: str = pydantic.Field(default_factory=str)
    gender: str = pydantic.Field(default_factory=str)
    episode: str = pydantic.Field(default_factory=str)

    @classmethod
    def get_attributes(cls) -> List[str]:
        return list(cls.schema()['properties'].keys())


class CSVFile(pydantic.BaseModel):
    path: str = pydantic.Field(default_factory=str)

    @validator('path')
    def must_be_valid_path(cls, v: str):
        _path = v.strip()  # removing all white spaces
        if isinstance(_path, str) and _path.endswith(".csv"):
            return _path
        raise ValidationError("The file has to be a csv file")
