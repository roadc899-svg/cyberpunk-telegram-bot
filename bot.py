from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# 🔹 Webhook Chatterfy (из Render Environment Variables)
CHATTERFY_WEBHOOK = os.getenv("CHATTERFY_WEBHOOK_URL")

@app.route('/')
def home():
    return "✅ Bot is running on Render", 200

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_id = data.get("user_id")
    step = data.get("step", 0)

    steps = [
        ("Conexión al sistema...", 0),
        ("Verificación de registro...", 12),
        ("Verificación de depósito...", 25),
        ("Análisis del historial de apuestas...", 40),
        ("Conexión de la cuenta a Lucky Mines...", 55),
        ("Recolección de datos del algoritmo de minas...", 70),
        ("Creación de la primera señal...", 88),
        ("✅ Acceso al hackbot concedido.", 100)
    ]

    if step < len(steps):
        text, progress = steps[step]
        payload = {
            "user_id": user_id,
            "text": f"{text} ({progress}%)"
        }
        requests.post(CHATTERFY_WEBHOOK, json=payload)
        return jsonify({"next_step": step + 1})
    else:
        return jsonify({"status": "done"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
