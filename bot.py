import asyncio
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Получаем токен из Render Environment
TOKEN = os.getenv("BOT_TOKEN")
DELAY_SECONDS = 0.8

# ================================
# 🔰 Шаги загрузки (исп.) с процентами
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

# ================================
# 🔰 Команда /start
# ================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text("⚙️ Iniciando proceso...")
    for text, pct in LOADING_STEPS:
        await asyncio.sleep(DELAY_SECONDS)
        try:
            # Для финального шага не добавляем "(100%)" дважды, но можно оставить — здесь показываем проценты у всех
            await msg.edit_text(f"{text} ({pct}%)")
        except Exception as e:
            print(f"⚠️ Edit error: {e}")
            continue

    await msg.reply_text("✅ Proceso completado. Acceso concedido al hackbot.")


# ================================
# 🔰 Точка входа
# ================================
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot started and listening (Spanish progress mode)...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
