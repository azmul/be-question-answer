from pydantic import BaseModel

class Question(BaseModel):
    question: str
    lang: str
    
class Sentence(BaseModel):
    sentence: str
    lang: str