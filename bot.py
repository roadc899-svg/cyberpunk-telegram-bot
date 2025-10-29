import asyncio
import os
import threading
from flask import Flask, request, jsonify
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ================================
# 🔰 Токен и настройки
# ================================
TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 10000))
DELAY_SECONDS = 1.0

# ================================
# 🔰 Прогресс-бар и шаги
# ================================
LOADING_STEPS = [
    ("Conexión al sistema...", 0),
    ("Verificación de registro...", 12),
    ("Verificación de depósito...", 25),
    ("Análisis del historial de apuestas...", 40),
    ("Conexión de la cuenta a Lucky Mines...", 55),
    ("Recolección de datos del algoritmo de ubicación de minas...", 70),
    ("Creación de la primera señal...", 88),
    ("✅ Acceso al hackbot concedido.", 100),
]

def make_progress_bar(percent: int, length: int = 20) -> str:
    filled = int(length * percent / 100)
    empty = length - filled
    return f"[{'█' * filled}{'▒' * empty}] {percent}%"

# ================================
# 🔰 Telegram часть
# ================================
async def run_installation(update: Update):
    msg = await update.message.reply_text("⚙️ Iniciando proceso...")

    for text, pct in LOADING_STEPS[:-1]:
        await asyncio.sleep(DELAY_SECONDS)
        bar = make_progress_bar(pct)
        try:
            await msg.edit_text(f"{text}\n{bar}")
        except Exception as e:
            print(f"⚠️ Edit error: {e}")
            continue

    final_text, _ = LOADING_STEPS[-1]
    await asyncio.sleep(DELAY_SECONDS)
    try:
        await msg.edit_text(final_text)
    except Exception as e:
        print(f"⚠️ Edit error (final): {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    asyncio.create_task(run_installation(update))

def start_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Telegram Bot started...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

# ================================
# 🔰 Flask часть (для Chatterfy)
# ================================
flask_app = Flask(__name__)

@flask_app.route("/webhook", methods=["POST"])
def chatterfy_webhook():
    data = request.get_json()
    user_name = data.get("user_name", "amigo")
    event = data.get("event", "default")

    if event == "registro":
        message = f"👋 ¡Hola {user_name}! Tu registro fue exitoso ✅"
    elif event == "deposito":
        message = f"💰 {user_name}, tu depósito fue recibido correctamente. Prepárate para activar el HackBot ⚡"
    elif event == "codigo":
        message = f"🔐 {user_name}, introduce tu código de acceso para continuar."
    else:
        message = f"👋 {user_name}, bienvenido al sistema dinámico 🚀"

    return jsonify({
        "message": message,
        "button_text": "⚡ Continuar",
        "button_url": "https://t.me/SamirHackBot"
    })

def start_flask():
    print(f"✅ Flask server running on port {PORT}...")
    flask_app.run(host="0.0.0.0", port=PORT)

# ================================
# 🔰 Запуск обоих процессов
# ================================
if __name__ == "__main__":
    threading.Thread(target=start_bot).start()
    start_flask()
