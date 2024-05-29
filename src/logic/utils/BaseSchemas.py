from fastapi import HTTPException, status
from pydantic import BaseModel, model_validator


class BaseSchema(BaseModel):
    class Config:
        from_attributes = True


class BaseModelWithValidation(BaseSchema):
    @model_validator(mode='after')
    def at_least_one_optional(self):
        optional_fields = {key: value for key, value in self.__dict__.items() if key != 'id'}

        if not any(value is not None for value in optional_fields.values()):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='At least one optional field must be provided'
            )
        return self
