from pydantic import BaseModel


class TTSItem(BaseModel):
    text: str
    gender: str
