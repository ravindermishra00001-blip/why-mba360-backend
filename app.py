from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from twilio.rest import Client

app = FastAPI(title="WHY MBA 360 API")

# Twilio
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "test")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "test")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER", "+14155238886")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://why-mba-360.surge.sh", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health():
    return {"status": "ok"}

@app.post("/api/whatsapp/send")
async def send_whatsapp(phone: str, message: str):
    return {"success": True, "phone": phone, "message": message}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 3000))
    uvicorn.run(app, host="0.0.0.0", port=port)
