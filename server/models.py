from pydantic import BaseModel

class InputData(BaseModel):
    system_prompt: str
    conversation: list
