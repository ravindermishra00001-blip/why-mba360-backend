from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from twilio.rest import Client

app = FastAPI(title="WHY MBA 360 API")

# Twilio
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER", "+14155238886")

twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) if TWILIO_ACCOUNT_SID else None

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
    return {"status": "ok", "message": "Cerebro backend running"}

@app.post("/api/whatsapp/send")
async def send_whatsapp(phone: str, message: str):
    try:
        if not twilio_client:
            return {"success": False, "error": "Twilio not configured"}
        
        if not phone.startswith("+"):
            phone = "+91" + phone if len(phone) == 10 else "+" + phone
        
        msg = twilio_client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            to=f"whatsapp:{phone}",
            body=message
        )
        return {"success": True, "phone": phone, "twilio_sid": msg.sid}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 3000))
    uvicorn.run(app, host="0.0.0.0", port=port)
