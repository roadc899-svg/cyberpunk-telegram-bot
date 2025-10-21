import asyncio
import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Получаем токен из Render Environment
TOKEN = os.getenv("BOT_TOKEN")
DELAY_SECONDS = 0.8

# ================================
# 🔰 Тема загрузки
# ================================
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

# ================================
# 🔰 /start команда
# ================================
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


# ================================
# 🔰 Запуск приложения
# ================================
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot started and listening...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
