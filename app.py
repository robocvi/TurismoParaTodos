from fastapi import FastAPI
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware
from src.requests import TextToSpeechRequest, SpeechToTextRequest, ChatBotRequest
from src.controllers import TextToSpeechController, SpeechToTextController, ChatbotController
from src.settings import OPENAI_API_KEY

app = FastAPI()
client = OpenAI(api_key=OPENAI_API_KEY)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to TurismoParaTodos API!"}

@app.post("/text_to_speech", tags=["TextSpeech"]) 
async def text_to_speech(request: TextToSpeechRequest):
    text = request.text
    return TextToSpeechController.text_to_speech(text)

@app.post("/speech_to_text", tags=["TextSpeech"]) 
async def speech_to_text(request: SpeechToTextRequest):
    url = request.url
    return SpeechToTextController.speech_to_text(url)

@app.post("/chatbot", tags=["TextSpeech"]) 
async def chatbot(request: ChatBotRequest):
    prompt = request.prompt
    client_tag = request.client_tag
    return ChatbotController.chatbot_answer(prompt, client_tag)