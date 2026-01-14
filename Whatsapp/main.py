import os
from fastapi import FastAPI, Request
from fastapi.responses import Response
from twilio.twiml.messaging_response import MessagingResponse
from groq import Groq
from dotenv import load_dotenv
from prompts import BUSINESS_PROMPTS

# Cargar variables de entorno
load_dotenv()

app = FastAPI()

# Cliente Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.post("/")
async def whatsapp_webhook(request: Request):
    # Twilio envía datos como x-www-form-urlencoded
    form = await request.form()
    user_message = form.get("Body", "").strip()

    # Fallback por seguridad
    if not user_message:
        twilio_response = MessagingResponse()
        twilio_response.message("Hola 👋 ¿En qué puedo ayudarte?")
        return Response(
            content=str(twilio_response),
            media_type="application/xml"
        )

    prompt = BUSINESS_PROMPTS["default"]

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ]
    )

    reply = completion.choices[0].message.content.strip()

    twilio_response = MessagingResponse()
    twilio_response.message(reply)

    # Devolver XML (TwiML)
    return Response(
        content=str(twilio_response),
        media_type="application/xml"
    )