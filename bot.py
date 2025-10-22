import asyncio
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ================================
# 🔰 Токен из Render Environment
# ================================
TOKEN = os.getenv("BOT_TOKEN")
DELAY_SECONDS = 1.0

# ================================
# 🔰 Шаги загрузки
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
# 🔰 Генератор прогресс-бара
# ================================
def make_progress_bar(percent: int, length: int = 20) -> str:
    filled = int(length * percent / 100)
    empty = length - filled
    return f"[{'█' * filled}{'▒' * empty}] {percent}%"

# ================================
# 🔰 Асинхронная установка (в отдельной задаче)
# ================================
async def run_installation(update: Update):
    """Эмулирует процесс загрузки в отдельном потоке"""
    msg = await update.message.reply_text("⚙️ Iniciando proceso...")

    for text, pct in LOADING_STEPS[:-1]:
        await asyncio.sleep(DELAY_SECONDS)
        bar = make_progress_bar(pct)
        try:
            await msg.edit_text(f"{text}\n{bar}")
        except Exception as e:
            print(f"⚠️ Edit error: {e}")
            continue

    # Финальный шаг
    final_text, _ = LOADING_STEPS[-1]
    await asyncio.sleep(DELAY_SECONDS)
    try:
        await msg.edit_text(final_text)
    except Exception as e:
        print(f"⚠️ Edit error (final): {e}")

# ================================
# 🔰 Команда /start
# ================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Создаёт отдельную задачу для каждого пользователя"""
    asyncio.create_task(run_installation(update))

# ================================
# 🔰 Точка входа
# ================================
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot started and listening (parallel progress mode)...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
