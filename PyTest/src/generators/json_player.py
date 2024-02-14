from pydantic import BaseModel, field_validator, PaymentCardNumber, EmailStr
from src.enums.user_enums import Statuses, UserErrors



PLAYER_URL = {
    'localize': {
        'en': {'nickname': 'Michael'},
        'ru': {'nickname': 'Самсон'}
    },
    'account_status': 'active',
    'avatar': 'https://google.com/',
    'balance': 0
}
class Nickname(BaseModel):
    nickname: str

class Localize(BaseModel):
    en: Nickname
    ru: Nickname

class Json_Player(BaseModel):
    localize: Localize
    account_status: Statuses
    avatar: str
    balance: int


# class Json_Player1(BaseModel):
#     localize: dict[str, dict[str, str]]
#     account_status: Statuses
#     avatar: str
#     balance: int

    @field_validator('balance')
    def check_validation_json(cls, balance):
        if balance >= 0:
            return balance
        else:
            raise ValueError(UserErrors.WRONG_BALANCE.value)






