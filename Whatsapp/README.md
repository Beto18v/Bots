# Whatsapp Bot

Este proyecto es un bot para WhatsApp que utiliza FastAPI y Groq para responder mensajes automáticamente a través de Twilio.

## Requisitos

- Python 3.8 o superior
- Instalar las dependencias:
  - [groq](https://pypi.org/project/groq/)
  - [python-dotenv](https://pypi.org/project/python-dotenv/)
  - [fastapi](https://pypi.org/project/fastapi/)
  - [uvicorn](https://pypi.org/project/uvicorn/)
  - [twilio](https://pypi.org/project/twilio/)
- Archivo `.env` con la configuración requerida

## Ejecución

1. Navegar a la carpeta `Whatsapp`:
   ```bash
   cd Whatsapp
   ```
2. Instalar dependencias:
   ```bash
   pip install groq python-dotenv fastapi uvicorn twilio
   ```
3. Configurar el archivo `.env` con la variable:
   ```env
   GROQ_API_KEY=api_key
   ```
4. Ejecutar el servidor con Uvicorn:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
5. Configurar tu webhook de Twilio para apuntar a `http://<TU_HOST>:8000/`.

## Archivos principales

- `main.py`: Servidor FastAPI que expone el endpoint para recibir mensajes de WhatsApp vía Twilio.
- `prompts.py`: Contiene los prompts o mensajes utilizados por el bot.
- `.env`: Variables de entorno necesarias para la configuración.

---

> **Nota:**
>
> - Configurar correctamente las variables de entorno antes de ejecutar el bot.
> - El bot está diseñado para recibir mensajes de WhatsApp a través de Twilio y responder usando Groq.
> - Se prueba localmente usando [ngrok](https://ngrok.com/) para exponer el servidor a internet y conectar con Twilio.
