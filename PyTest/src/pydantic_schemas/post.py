from pydantic import BaseModel, Field, validator, field_validator



class Post(BaseModel):
    id: int = Field(le=2)
    title: str
    # name: str = Field(alias="_name") if in json value = _name

    # @field_validator("id")
    # def check_that_id_is_less_than_two(cls, v):
    #     if v > 2:
    #         raise ValueError('Id is not less than two')
    #     else:
    #         return v


