from fastapi import FastAPI
from transformers import pipeline
from googletrans import Translator
from models import Question, Sentence

app = FastAPI()

translator = Translator()

model_name = "deepset/roberta-base-squad2"

# download model
qa_model = pipeline('question-answering', model=model_name, tokenizer=model_name)

# test model
context = "Monstarlab is a global digital consulting firm that specializes in strategy, design, and technology. Originating from Japan, the company has expanded its reach with offices around the world. Monstarlab offers a wide array of services, ranging from digital product development, UX/UI design, and digital transformation strategies, to name a few. Their team consists of engineers, designers, and consultants who collaborate to create innovative digital solutions tailored to their clients' unique challenges. As digital transformation continues to be a priority for businesses across industries, Monstarlab's expertise positions them as a notable player in the global market, helping brands navigate the complexities of the digital landscape"

@app.get("/")
async def root():
    return {"hello": "world"}

@app.post("/api/v1/answer")
async def get_answer(params: Question):
    q_translation = translator.translate(params.question, dest="en")
    qa_response = qa_model(question = q_translation.text, context = context)
    translation = translator.translate(qa_response["answer"], dest=params.lang)
    return {"answer": translation.text, "lang": params.lang}

@app.post("/api/v1/translate")
async def get_answer(params: Sentence):
    translation = translator.translate(params.sentence, dest=params.lang)
    return {"translate": translation.text, "src": translation.src}