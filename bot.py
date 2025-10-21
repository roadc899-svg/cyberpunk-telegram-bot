import asyncio
import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

CYBER_STEPS = [
    "[BOOT SEQUENCE INITIATED] █▒▒▒▒▒▒▒▒▒",
    "Step 1/10: Scanning neural grids... █▒▒▒▒▒▒▒▒",
    "Step 2/10: Decrypting cortex shard... ██▒▒▒▒▒▒▒",
    "Step 3/10: Injecting synth-protocols... ███▒▒▒▒▒▒",
    "Step 4/10: Overclocking cyber-threads... ████▒▒▒▒",
    "Step 5/10: Patching memory splinters... █████▒▒▒",
    "Step 6/10: Syncing black-ops node... ██████▒▒",
    "Step 7/10: Calibrating holo-interface... ███████▒",
    "Step 8/10: Seeding phantom drivers... ████████",
    "Step 9/10: Finalizing spectral handshake... ████████▒",
    "Step 10/10: Stabilizing matrix core... █████████",
    "✅ SYSTEM ONLINE — ACCESS GRANTED"
]

DELAY_SECONDS = 1.2


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text("Initializing protocol...")
    for step in CYBER_STEPS:
        await asyncio.sleep(DELAY_SECONDS)
        try:
            await msg.edit_text(step)
        except Exception as e:
            print(f"⚠️ Edit error: {e}")
            continue
    await msg.reply_text("✅ Installation complete. System ready.")


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot started and listening...")
    app.run_polling()


# -----------------------------
# ✅ Flask-заглушка для Render
# -----------------------------
def keep_alive():
    app = Flask('')

    @app.route('/')
    def home():
        return "Bot is running"

    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# Запускаем Flask в отдельном потоке
threading.Thread(target=keep_alive).start()
# -----------------------------


if __name__ == "__main__":
    main()
