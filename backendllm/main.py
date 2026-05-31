from fastapi import FastAPI,Request
from openai import OpenAI
import os
app=FastAPI()
@app.get("/")
def home():
    return{
        "msg":"you are on Home"
    }
client=OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

@app.post("/generate")
async def prompt_rec_function(req :Request):
    data= await req.json()
    p=data["prompt"]

    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role":"user",
            "content":p
            }
        ]
    )
    return {
    "answer": response.choices[0].message.content
    }
